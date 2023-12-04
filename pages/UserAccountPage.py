import string

from pages.BasePage import BasePage
from pages.locators import UserAccountPageLocators
import time
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UserAccountPage(BasePage):

    def check_is_element_presented(self,element_path):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element_path)).is_enabled()

    def click_home_page_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(UserAccountPageLocators.UserAccountPageLocators.Header.HOME_BUTTON)).click()