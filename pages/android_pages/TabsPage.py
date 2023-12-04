from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class TabsPage(BasePage):

    def get_tabs_list_length(self, mobile_driver):
        return mobile_driver.find_elements(By.ID, 'com.android.chrome:id/card_view').__len__()

    def click_create_new_tab(self, mobile_driver):
        mobile_driver.find_element(By.ID, 'com.android.chrome:id/new_tab_view').click()
        time.sleep(3)

    def click_on_tab_by_index(self, mobile_driver, index):
        mobile_driver.find_element(By.XPATH,
                                   f'(//android.widget.RelativeLayout[@resource-id="com.android.chrome:id/card_view"])[{index}]').click()
