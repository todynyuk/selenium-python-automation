import string

from pages.BasePage import BasePage
from pages.locators import SignInPageLocators
import time
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SignInPage(BasePage):

    def fill_input_field(self,element,data):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element)).send_keys(data)

    def click_login_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(SignInPageLocators.SignInPageLocators.Body.LOGIN_BUTTON)).click()