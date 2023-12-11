from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pages.ios_pages.IOSMainPage import IOSMainPage
from pages.ios_pages.IOSProductDevicePage import IOSProductDevicePage


class TestAndroidMainPage:

    def test_verify_items_data_and_basket_counter(self, ios_driver):
        time.sleep(3)
        main_page = IOSMainPage(ios_driver)
        main_page.swipe_by_coordinates(ios_driver, 10, 521, 10, 410)
        plp_item_text = str(main_page.get_item_text_by_index(ios_driver, 1))
        time.sleep(3)
        main_page.click_on_item_by_index(ios_driver, 1)
        time.sleep(3)
        pdp = IOSProductDevicePage(ios_driver)
        time.sleep(3)
        pdp_item_text = pdp.get_item_text(ios_driver)
        assert pdp_item_text == plp_item_text

