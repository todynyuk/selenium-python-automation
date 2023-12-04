from appium import webdriver
import time
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AndroidUserAccountPage(BasePage):
    def check_is_element_presented(self, mobile_driver, element_path):
        time.sleep(3)
        return mobile_driver.find_element(element_path).is_enabled()
