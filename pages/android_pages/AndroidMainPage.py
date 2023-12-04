from appium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.android_locators import AndroidMainPageLocators


class AndroidMainPage(BasePage):

    def click_tabs_button(self, mobile_driver):
        mobile_driver.find_element(By.XPATH,
                                   '//android.widget.ImageButton[@content-desc="Switch or close tabs"]').click()
        time.sleep(3)

    def click_filter_button(self, mobile_driver):
        time.sleep(5)
        mobile_driver.find_element(AndroidMainPageLocators.AndroidMainPageLocators.Body.FILTER_BUTTON).click()
        time.sleep(5)

    def fill_search_input_field(self, mobile_driver, search_item):
        WebDriverWait(mobile_driver, 5).until(
            EC.presence_of_element_located(
                AndroidMainPageLocators.AndroidMainPageLocators.Body.SEARCH_INPUT_FIELD)).send_keys(search_item)

    def search_button_click(self, mobile_driver):
        WebDriverWait(mobile_driver, 10).until(
            EC.presence_of_element_located(AndroidMainPageLocators.AndroidMainPageLocators.Body.SEARCH_BUTTON)).click()

    def get_items_title_text(self, mobile_driver, param):
        goods_title_texts = []
        actions = ActionChains(mobile_driver)
        actions.w3c_actions = ActionBuilder(mobile_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        items_list = mobile_driver.find_element(By.XPATH,
                                                f"//*[@class='android.widget.TextView' and contains(@text,'{param}')]")
        for elem in items_list:
            goods_title_texts.append(elem.text)
        return goods_title_texts

    def verify_is_search_think_present_in_goods_title(self, mobile_driver, think_name):
        goods_title_texts = [x.lower() for x in AndroidMainPage.get_items_title_text(self, mobile_driver, think_name)]
        res = all([ele for ele in str(think_name).lower() if (ele in goods_title_texts)])
        return res
