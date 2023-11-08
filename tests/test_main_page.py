import pytest
from pages.MainPage import MainPage


class TestMainPage:

    def test_main_page_search(self, driver):
        main_page = MainPage(driver)
        main_page.fill_search_input_field("Drill")
        main_page.search_button_click()
        assert main_page.get_search_items_list_size() > 0, "Search items list have zero size"
        main_page.print_all_search_items_text()
        assert main_page.verify_is_search_think_present_in_goods_title(
            "Drill"), "Items are not contains search text"
