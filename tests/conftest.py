import sys

import pytest
import os
import pytest
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


# в conftest живет конфигурация тестов по типу: chrome options, setup...


# --------------------------------------
@pytest.fixture
def chrome_options():
    options = Options()
    return options


# -----------------------------------------------------------
@pytest.fixture(scope="function")
def driver(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practicesoftwaretesting.com/#/")
    yield driver
    driver.quit()


# -----------------------------------------------------------
# -----------------------------------------------------------
@pytest.fixture(scope="function")
def remote_driver(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor="http://192.168.0.101:4444/wd/hub",
                              options=options
                              )

    driver.get("https://practicesoftwaretesting.com/#")
    driver.maximize_window()
    yield driver
    driver.close()


# -----------------------------------------------------------


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait
    # yield driver #в отличии от return возвращает объект-генератор
    # driver.quit()


def take_screenshot(driver):
    # Define the screenshot filename (you may want to make it dynamic)
    screenshot_filename = f"screenshot{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}.png"
    # Save the screenshot
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'driver' in item.fixturenames:  # assume this is fixture with webdriver
                    driver = item.funcargs['driver']
                else:
                    print('Fail to take screen-shot')
                    return
            take_screenshot(driver)

        except Exception as e:
            print(f'Fail to take screen-shot: {e}')
