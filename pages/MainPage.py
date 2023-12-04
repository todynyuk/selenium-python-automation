import string

from pages.BasePage import BasePage
from pages.locators import MainPageLocators
import time
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def get_main_text(self, driver):
        return driver.find_element(By.CSS_SELECTOR,
                                   "h4[class='grid']").text

    def click_sign_in_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.Main.Header.SIGN_IN_BUTTON)).click()

    def click_on_item_by_index(self, driver, index):
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,
                            f"div[class='col-md-9']>div[class='container']>:nth-child({index})>div[class='card-body']").click()
        time.sleep(5)

    def fill_search_input_field(self, search_item):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.Main.MainPage.SEARCH_INPUT_FIELD)).send_keys(search_item)

    def search_button_click(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.Main.MainPage.SEARCH_BUTTON)).click()

    def click_on_checkbox_filter(self, driver, param):
        time.sleep(5)
        driver.find_element(By.XPATH, f"//label[contains(text(),'{param}')]").click()
        time.sleep(5)

    def get_search_items_list_size(self):
        items_list_size = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(MainPageLocators.Main.MainPage.PRODUCT_TITLES_LIST))
        return len(items_list_size)

    def print_all_search_items_text(self):
        index = 0
        items_list_size = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(MainPageLocators.Main.MainPage.PRODUCT_TITLES_LIST))
        print("\n=====Search items text:=====")
        for item in items_list_size:
            index += 1
            print(index, ": ", item.text)

    def get_goods_title_text(self):
        goods_title_texts = []
        items_list = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(MainPageLocators.Main.MainPage.PRODUCT_TITLES_LIST))
        for elem in items_list:
            goods_title_texts.append(elem.text)
        return goods_title_texts

    def get_item_title_text_by_index(self, driver, index):
        time.sleep(5)
        return driver.find_element(By.CSS_SELECTOR,
                                   f"div[class='col-md-9']>div[class='container']>:nth-child({index})>div[class='card-body']").text

    def verify_is_search_think_present_in_goods_title(self, think_name):
        goods_title_texts = [x.lower() for x in MainPage.get_goods_title_text(self)]
        res = all([ele for ele in str(think_name).lower() if (ele in goods_title_texts)])
        return res

    def click_sort_dropdown_menu(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.Main.MainPage.SORT_DROPDOWN_MENU)).click()
        time.sleep(5)

    def click_by_sort_filter_dropdown_menu(self, param):
        if param == "asc":
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    MainPageLocators.Main.MainPage.DROPDOWN_MENU_SORT_PRICE_ASCENDING_OPTION)).click()
            time.sleep(5)
        if param == "desc":
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    MainPageLocators.Main.MainPage.DROPDOWN_MENU_SORT__PRICE_DESCENDING_OPTION)).click()
            time.sleep(5)

    def get_prices_list(self, driver):
        chosen_price_devices = []
        time.sleep(5)
        for elem in driver.find_elements(By.XPATH, "//span[@data-test='product-price']"):
            time.sleep(5)
            buffer = str(elem.text).replace("$", "")
            chosen_price_devices.append(float(buffer))
        return chosen_price_devices

    def is_all_goods_sorted_from_low_to_high_price(self, driver):
        low_to_high_price_list = self.get_prices_list(driver)
        return all(low_to_high_price_list[j] <= low_to_high_price_list[j + 1] for j in
                   range(len(low_to_high_price_list) - 1))

    def is_all_goods_sorted_from_high_to_low_price(self, driver):
        high_to_low_price_list = self.get_prices_list(driver)
        return all(high_to_low_price_list[j] >= high_to_low_price_list[j + 1] for j in
                   range(len(high_to_low_price_list) - 1))
