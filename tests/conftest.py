import pytest
import os
import pytest
from selenium import webdriver

# import undetected_chromedriver as uc
from selenium import webdriver as wd
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
#     parser.addoption("--url", "-U", action="store", default="https://powerslide.com/", help="select your required URL")
#
# @pytest.fixture
# def url(request):
#     return request.config.getoption("--url")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     # options = uc.ChromeOptions()
#     # options.add_argument('--disable-notifications')
#     # options.add_argument('--user-data-dir=C:\\Users\\Evgeny\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
#     # options.add_argument('--headless')
#     # options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
#
#     url = request.config.getoption("--url")
#     browser = request.config.getoption("--browser")
#     print("\nStart work browser")
#     if browser == "chrome":
#         # driver = uc.Chrome(options=options)
#         driver = wd.Chrome
#         driver.maximize_window()
#     elif browser == "firefox":
#         driver = wd.Firefox()
#     elif browser == "safari":
#         driver = wd.Safari()
#     else:
#         raise Exception(f"{request.param} is not supported!")
#     driver.get(url)
#     # driver.get(request)
#     yield driver
#     print("\nEnd work browser")
#     driver.close()
#
# # @pytest.fixture(scope="function")
# # def driver():
# #     zebrunner_selenium_grid = os.getenv("ZEBRUNNER_SELENIUM_GRID", "http://127.0.0.1:4444")
# #     options = webdriver.ChromeOptions()
# #     options.platform_name = "linux"
# #     options.browser_version = "119.0"
# #     options.set_capability("enableVideo", "true")
# #     driver = webdriver.Remote(
# #         command_executor=zebrunner_selenium_grid,
# #         options=options
# #     )
# #     driver.implicitly_wait(10)
# #     driver.maximize_window()
# #     yield driver
# #     driver.quit()


 # в conftest живет конфигурация тестов по типу: chrome options, setup...
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def chrome_options():
    options = Options()
    # options.add_argument('--window-size=200,200')
    # options.add_argument('--headless')
    return options

# @pytest.fixture
# #с неявным ожиданием
# def driver1(chrome_options):
#     driver1 = webdriver.Chrome(options=chrome_options)
#     driver1.implicitly_wait(10)
#     yield driver1
#     driver1.quit()

# @pytest.fixture
#с явным,sleep ожиданием
# def driver(chrome_options):
@pytest.fixture(scope="function")
def driver(request):
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    # marker = request.node.get_closest_marker("fixt_data")
    # driver.get("https://powerslide.com/")
    driver.get("https://practicesoftwaretesting.com/#/")
    # driver.get(marker)

    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait
    # yield driver #в отличии от return возвращает объект-генератор
    # driver.quit()