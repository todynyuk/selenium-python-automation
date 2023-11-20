import string

from pages.BasePage import BasePage
import pages.locators.ProductDevicePageLocators as PDPLocators
import pages.locators.ShoppingBasketPageLocators as BasketLocators
import time
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ShoppingBasketPage(BasePage):

    def check_is_element_presented(self,element_path):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element_path)).is_enabled()
    def get_item_title_text(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(BasketLocators.ShoppingBasketPageLocators.Body.ITEM_DESCRIPTION_TEXT)).text

