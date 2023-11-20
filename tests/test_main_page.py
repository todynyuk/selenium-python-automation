import sys
import pytest
from pages.MainPage import MainPage
from functools import partialmethod
import time
from datetime import datetime


@pytest.mark.incremental
class TestMainPage:

    def test_main_page_search(self, driver):
        main_page = MainPage(driver)
        main_page.fill_search_input_field("Drill")
        main_page.search_button_click()
        assert main_page.get_search_items_list_size() > 0, "Search items list have zero size"
        main_page.print_all_search_items_text()
        assert main_page.verify_is_search_think_present_in_goods_title(
            "Drill"), "Items are not contains search text"

    def test_sort_from_low_to_high_price(self, driver):
        main_page = MainPage(driver)
        main_page.click_sort_dropdown_menu()
        main_page.click_by_sort_filter_dropdown_menu("asc")
        assert main_page.is_all_goods_sorted_from_low_to_high_price(driver), \
            "All items are not sorted from low to high price"

    def test_sort_from_high_to_low_price(self, driver):
        main_page = MainPage(driver)
        main_page.click_sort_dropdown_menu()
        main_page.click_by_sort_filter_dropdown_menu("desc")
        assert main_page.is_all_goods_sorted_from_high_to_low_price(driver), \
            "All items are not sorted from high to low price"

    def test_filter_items_by_name(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_checkbox_filter(driver, "Hammer")
        assert main_page.verify_is_search_think_present_in_goods_title(
            "Hammer"), "Items are not contains search text"

    def test_example(self, driver):
        main_page = MainPage(driver)
        # assert "hvjhjh" in "0010000"
        # main_page.get_main_text(driver)

