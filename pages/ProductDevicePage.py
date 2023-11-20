import string
import pages.locators.ProductDevicePageLocators as PDPLocators
from pages.BasePage import BasePage
import time
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductDevicePage(BasePage):

    def check_is_element_presented(self, element_path):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element_path)).is_enabled()

    def get_item_title_text(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(PDPLocators.ProductDevicePageLocators.Body.PRODUCT_TITLE_TEXT)).text

    def add_to_cart_button_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(PDPLocators.ProductDevicePageLocators.Body.ADD_TO_CART_BUTTON)).click()

    def shopping_basket_click(self):
        # driver.find_element(By.CSS_SELECTOR,"button[data-test='add-to-cart']").click()
        # driver.find_element(PDPLocators.ProductDevicePageLocators.Body.ADD_TO_CART_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PDPLocators.ProductDevicePageLocators.Header.SHOPPING_CARD_BUTTON)).click()

    def click_plus_item_count(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(PDPLocators.ProductDevicePageLocators.Body.PLUS_QUANTITY_BUTTON)).click()

    def click_minus_item_count(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(PDPLocators.ProductDevicePageLocators.Body.MINUS_QUANTITY_BUTTON)).click()

    def fill_item_count_input_field(self, value):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                PDPLocators.ProductDevicePageLocators.Body.ITEM_QUANTITY_INPUT_FIELD)).send_keys(value)

    def is_shopping_basket_counter_presented(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                PDPLocators.ProductDevicePageLocators.Header.SHOPPING_CARD_COUNTER)).is_enabled()

    def get_basket_counter_text(self):
        buffer = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(PDPLocators.ProductDevicePageLocators.Header.SHOPPING_CARD_COUNTER)).text
        return int(buffer)
