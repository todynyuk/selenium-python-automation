import sys
import pytest
import os
from os import path
import pytest
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from appium.options.android import UiAutomator2Options
from appium import webdriver
import time

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
# -----------------------------------------------------------
def take_screenshot(driver):
    # Define the screenshot filename (you may want to make it dynamic)
    screenshot_filename = f"screenshot{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}.png"
    # Save the screenshot
    file_dir = path.join(os.getcwd(), "resources/screenshots/")
    os.makedirs(file_dir, exist_ok=True)

    file_path = path.join(file_dir, screenshot_filename)
    driver.save_screenshot(file_path)
    print(f"Screenshot saved as {screenshot_filename}")
# -----------------------------------------------------------
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
# -----------------------------------------------------------
@pytest.fixture(scope="function")
def mobile_driver(request):
    global mobile_driver
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "14.0",
        "deviceName": "Pixel_3a_API_34_extension_level_7_x86_64"
    }
    appium_server_url = 'http://127.0.0.1:4723/wd/hub'
    capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
    mobile_driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
    time.sleep(8)
    mobile_driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Chrome"]').click()
    time.sleep(15)
    yield mobile_driver
    mobile_driver.quit()
