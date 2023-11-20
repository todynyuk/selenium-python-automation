import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome import service
from selenium.webdriver.common.utils import free_port
import subprocess



# def test_start_remote(server):
#     pass
#
#
# def test_uploads(server):
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Remote(command_executor=server, options=options)
#
#     driver.get("https://the-internet.herokuapp.com/upload")
#     upload_file = os.path.abspath(
#         os.path.join(os.path.dirname(__file__), "..", "selenium-snapshot.png"))
#
#     driver.file_detector = LocalFileDetector()
#     file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
#     file_input.send_keys(upload_file)
#     driver.find_element(By.ID, "file-submit").click()
#
#     file_name_element = driver.find_element(By.ID, "uploaded-files")
#     file_name = file_name_element.text
#
#     assert file_name == "selenium-snapshot.png"
#
#
# def test_downloads(server, temp_dir):
#     options = webdriver.ChromeOptions()
#     options.enable_downloads = True
#     driver = webdriver.Remote(command_executor=server, options=options)
#
#     file_names = ["file_1.txt", "file_2.jpg"]
#     driver.get('https://www.selenium.dev/selenium/web/downloads/download.html')
#     driver.find_element(By.ID, "file-1").click()
#     driver.find_element(By.ID, "file-2").click()
#     WebDriverWait(driver, 3).until(lambda d: "file_2.jpg" in d.get_downloadable_files())
#
#     files = driver.get_downloadable_files()
#
#     assert files == file_names
#     downloadable_file = files[0]
#     target_directory = temp_dir
#
#     driver.download_file(downloadable_file, target_directory)
#
#     target_file = os.path.join(target_directory, downloadable_file)
#     with open(target_file, "r") as file:
#         assert "Hello, World!" in file.read()
#
#     driver.delete_downloadable_files()
#
#     assert not driver.get_downloadable_files()

import pytest

# @pytest.mark.usefixtures("browser")
# class TestWebsite:
#
#     def test_scenario_1(self, browser):
#         browser.get("https://practicesoftwaretesting.com/#")
#         # Add your test steps for scenario 1
#
#     def test_scenario_2(self, browser):
#         browser.get("https://practicesoftwaretesting.com/#")
#         # Add your test steps for scenario 2

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Define the remote WebDriver URL
# REMOTE_URL = "http://localhost:4444/wd/hub"
# NEW_REMOTE_URL =  "http://192.168.0.101:4444"
#
# # Test data (you can extend this with more test data)
# test_data = [
#     {"search_term": "Selenium testing"},
#     {"search_term": "Parallel testing"},
#     # Add more test data as needed
# ]
#
# @pytest.mark.parametrize("data", test_data)
# def test_search_functionality(data):
#     options = ChromeOptions()
#     options.browser_version = '119'
#     # options.platform_name = 'Windows 10'
#     # cloud_options = {}
#     # cloud_options['build'] = my_test_build
#     # cloud_options['name'] = my_test_name
#     # options.set_capability('cloud:options', cloud_options)
#     driver = webdriver.Remote(REMOTE_URL, options=options)
#     # Navigate to the practice website
#     driver.get("https://practicesoftwaretesting.com/#")
#
#     # Perform the search using the provided data
#     search_box = driver.find_element("class", "form-control ng-untouched ng-pristine ng-invalid")
#     search_box.send_keys(data["Drill"])
#     search_box.send_keys(Keys.RETURN)
#
#     # Example assertion: Check if the search results page contains the search term
#     assert data["Drill"].lower() in driver.title.lower()
#
#     # Close the browser
#     driver.quit()
#
#
# def get_web_driver():
#     options = ChromeOptions()
#     options.add_argument("--start-maximized")
#     driver = webdriver.Remote(command_executor=REMOTE_URL, options=options)
#     driver.set_script_timeout(300)
#     driver.set_page_load_timeout(300)
#     return driver
#
# def test_web():
#     driver = get_web_driver()
#     driver.get("https://practicesoftwaretesting.com/#")
#     search_box = driver.find_element("class", "form-control ng-untouched ng-pristine ng-invalid")
#     search_box.send_keys("Drill")
#     search_box.send_keys(Keys.RETURN)
#     time.sleep(5)
#     assert "Drill".lower() in driver.title.lower()

def test_search(remote_driver):
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Remote(command_executor="http://192.168.0.101:4444/wd/hub",
    #                           options=options
    #                           )
    #
    # driver.get("https://practicesoftwaretesting.com/#")
    # driver.maximize_window()
    search_box = remote_driver.find_element(By.CSS_SELECTOR, "input[data-test='search-query']")
    search_box.send_keys("Drill")
    remote_driver.find_element(By.CSS_SELECTOR, "button[data-test='search-submit']").click()
    time.sleep(3)
    search_title_text = remote_driver.find_element(By.CSS_SELECTOR,"div[class='col-md-9']>h3").text
    assert "Drill".lower() in search_title_text.lower()
    # driver.close()
    # driver.quit()

def test_search_and_verify_non_empty_items_list(remote_driver):
    search_box = remote_driver.find_element(By.CSS_SELECTOR, "input[data-test='search-query']")
    search_box.send_keys("Drill")
    remote_driver.find_element(By.CSS_SELECTOR, "button[data-test='search-submit']").click()
    time.sleep(3)
    items_title_list_size= len(remote_driver.find_elements(By.CSS_SELECTOR, "h5[data-test='product-name']"))
    time.sleep(3)
    assert items_title_list_size > 0, "Search items list have zero size"

def test_search_and_verify_item_title_texts(remote_driver):
    search_box = remote_driver.find_element(By.CSS_SELECTOR, "input[data-test='search-query']")
    search_box.send_keys("Drill")
    remote_driver.find_element(By.CSS_SELECTOR, "button[data-test='search-submit']").click()
    time.sleep(3)
    first_item_title_text = remote_driver.find_element(By.CSS_SELECTOR,"div[class='col-md-9']>div[class='container']>:nth-child(1)>div[class='card-body']>h5[class='card-title']").text
    time.sleep(3)
    assert ("Drill").lower() in first_item_title_text.lower()

def test_web_sort_by_asc(remote_driver):
    remote_driver.find_element(By.CSS_SELECTOR, "select[data-test='sort']").click()
    remote_driver.find_element(By.CSS_SELECTOR, "option[value='price,asc']").click()
    first_item_price_text=remote_driver.find_element(By.CSS_SELECTOR,"div[class='col-md-9']>div[class='container']>:nth-child(1)>div[class='card-footer']>span>span[data-test='product-price']")
    second_item_price_text=remote_driver.find_element(By.CSS_SELECTOR,"div[class='col-md-9']>div[class='container']>:nth-child(2)>div[class='card-footer']>span>span[data-test='product-price']")
    first_buffer = str(first_item_price_text.text).replace("$","")
    second_buffer = str(second_item_price_text.text).replace("$","")
    assert first_buffer<second_buffer,"All items are not sorted from low to high price"

def test_web_sort_by_asc(remote_driver):
    remote_driver.find_element(By.CSS_SELECTOR, "select[data-test='sort']").click()
    remote_driver.find_element(By.CSS_SELECTOR, "option[value='price,desc']").click()
    first_item_price_text=remote_driver.find_element(By.CSS_SELECTOR,"div[class='col-md-9']>div[class='container']>:nth-child(1)>div[class='card-footer']>span>span[data-test='product-price']")
    second_item_price_text=remote_driver.find_element(By.CSS_SELECTOR,"div[class='col-md-9']>div[class='container']>:nth-child(2)>div[class='card-footer']>span>span[data-test='product-price']")
    first_buffer = str(first_item_price_text.text).replace("$","")
    second_buffer = str(second_item_price_text.text).replace("$","")
    assert first_buffer>second_buffer,"All items are not sorted from high to low price"

def test_shopping_basket(remote_driver):
    remote_driver.find_element(By.CSS_SELECTOR, "select[data-test='sort1']").click()




