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
        time.sleep(3)
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element_path)).is_enabled()
    def get_item_title_text(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(BasketLocators.ShoppingBasketPageLocators.Body.ITEM_DESCRIPTION_TEXT)).text

    def click_checkout_button(self,checkout_button):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(checkout_button)).click()

    def fill_payment(self,account_name,account_number):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(BasketLocators.ShoppingBasketPageLocators.Body.PAYMENT_METHOD_DROPDOWN_MENU)).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                BasketLocators.ShoppingBasketPageLocators.Body.METHOD_PAYMENT_OPTION)).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                BasketLocators.ShoppingBasketPageLocators.Body.USER_NAME_INPUT_FIELD)).send_keys(account_name)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                BasketLocators.ShoppingBasketPageLocators.Body.USER_NUMBER_INPUT_FIELD)).send_keys(account_number)

