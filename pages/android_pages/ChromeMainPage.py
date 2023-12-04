from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.android_locators import AndroidMainPageLocators


class ChromeMainPage(BasePage):

    def click_tabs_button(self, mobile_driver):
        mobile_driver.find_element(By.XPATH,
                                   '//android.widget.ImageButton[@content-desc="Switch or close tabs"]').click()
        time.sleep(3)

    def fill_search_input_field(self, mobile_driver, search_item):
        WebDriverWait(mobile_driver, 5).until(
            EC.presence_of_element_located(
                AndroidMainPageLocators.AndroidMainPageLocators.Body.SEARCH_INPUT_FIELD)).send_keys(search_item)