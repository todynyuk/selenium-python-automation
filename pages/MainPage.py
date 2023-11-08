from pages.BasePage import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def fill_search_input_field(self, search_item):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.Main.MainPage.SEARCH_INPUT_FIELD)).send_keys(search_item)

    def search_button_click(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.Main.MainPage.SEARCH_BUTTON)).click()

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

    def verify_is_search_think_present_in_goods_title(self, think_name):
        goods_title_texts = [x.lower() for x in MainPage.get_goods_title_text(self)]
        res = all([ele for ele in str(think_name).lower() if (ele in goods_title_texts)])
        return res
