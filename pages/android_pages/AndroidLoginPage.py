from appium import webdriver
import time
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.android_locators.AndroidLoginPageLocators import AndroidLoginPageLocators


class AndroidLoginPage(BasePage):

    def fill_input_field(self, element, mobile_driver, param):
        WebDriverWait(mobile_driver, 5).until(
            EC.presence_of_element_located(
                element)).send_keys(param)

    def login_button_click(self, mobile_driver):
        WebDriverWait(mobile_driver, 5).until(
            EC.presence_of_element_located(AndroidLoginPageLocators.Body.LOGIN_BUTTON)).click()
