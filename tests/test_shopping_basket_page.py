import pytest
from pages.MainPage import MainPage
from pages.SignInPage import SignInPage
from pages.ProductDevicePage import ProductDevicePage
from pages.ShoppingBasketPage import ShoppingBasketPage
import pages.locators.ProductDevicePageLocators as PDPLocators
import pages.locators.SignInPageLocators as SignInLocators
import pages.locators.ShoppingBasketPageLocators as BasketLocators
import time

from pages.UserAccountPage import UserAccountPage


class TestShoppingBasketPage:

    def test_compare_device_text(self, driver):
        main_page = MainPage(driver)
        item_title_text = main_page.get_item_title_text_by_index(driver, 1)
        main_page.click_on_item_by_index(driver, 1)
        pdp = ProductDevicePage(driver)
        pdp_item_text = pdp.get_item_title_text()
        assert item_title_text == pdp_item_text, "Item title texts are not equals"
        pdp.add_to_cart_button_click()
        basket_status = pdp.check_is_element_presented(
            PDPLocators.ProductDevicePageLocators.Header.SHOPPING_CARD_BUTTON)
        card_counter_status = pdp.check_is_element_presented(
            PDPLocators.ProductDevicePageLocators.Header.SHOPPING_CARD_COUNTER)
        assert basket_status, "basket button is not presented"
        assert card_counter_status, "card_counter is not presented"
        pdp.shopping_basket_click()
        basket_page = ShoppingBasketPage(driver)
        assert basket_page.check_is_element_presented(
            BasketLocators.ShoppingBasketPageLocators.Body.ITEM_DESCRIPTION_TEXT), "ITEM_DESCRIPTION_TEXT is not presented"
        assert basket_page.check_is_element_presented(
            BasketLocators.ShoppingBasketPageLocators.Body.TOTAL_COST_TEXT), "TOTAL_COST_TEXT is not presented"
        assert basket_page.check_is_element_presented(
            BasketLocators.ShoppingBasketPageLocators.Body.ITEM_PRICE_TEXT), "ITEM_PRICE_TEXT is not presented"
        assert basket_page.check_is_element_presented(
            BasketLocators.ShoppingBasketPageLocators.Body.DELETE_ITEM_BUTTON), "DELETE_ITEM_BUTTON is not presented"
        assert basket_page.check_is_element_presented(
            BasketLocators.ShoppingBasketPageLocators.Body.ORGANIZE_CHECKOUT_BUTTON), "ORGANIZE_CHECKOUT_BUTTON is not presented"
        basket_item_title_text = basket_page.get_item_title_text()
        assert item_title_text in basket_item_title_text, "Item title texts are not equals"
        assert pdp_item_text in basket_item_title_text, "Item title texts are not equals"

    def test_checkout(self, driver):
        main_page = MainPage(driver)
        main_page.click_sign_in_button()
        login_page = SignInPage(driver)
        login_page.fill_input_field(SignInLocators.SignInPageLocators.Body.EMAIL_INPUT_FIELD, "noges93919@ikanid.com")
        login_page.fill_input_field(SignInLocators.SignInPageLocators.Body.PASSWORD_INPUT_FIELD, "Noges93919")
        login_page.click_login_button()
        time.sleep(3)
        user_account_page = UserAccountPage(driver)
        user_account_page.click_home_page_button()
        main_page.click_on_item_by_index(driver, 1)
        pdp = ProductDevicePage(driver)
        pdp.add_to_cart_button_click()
        pdp.shopping_basket_click()
        basket_page = ShoppingBasketPage(driver)
        basket_page.click_checkout_button(BasketLocators.ShoppingBasketPageLocators.Body.CONFIRM_CHECKOUT_BUTTON)
        assert basket_page.check_is_element_presented(
            BasketLocators.ShoppingBasketPageLocators.Body.USER_LOGIN_STATUS_TEXT),\
            "USER_LOGIN_STATUS_TEXT is not presented"
        basket_page.click_checkout_button(BasketLocators.ShoppingBasketPageLocators.Body.CONFIRM_SIGN_IN_BUTTON)
        assert basket_page.check_is_element_presented(
            BasketLocators.ShoppingBasketPageLocators.Body.ADDRESS_INPUT_FIELD), \
            "ADDRESS_INPUT_FIELD is not presented"
        basket_page.click_checkout_button(BasketLocators.ShoppingBasketPageLocators.Body.CONFIRM_ADDRESS_BUTTON)
        basket_page.fill_payment("John","1107686745345")
        basket_page.click_checkout_button(BasketLocators.ShoppingBasketPageLocators.Body.CONFIRM_ORDER_BUTTON)
        assert basket_page.check_is_element_presented(
            BasketLocators.ShoppingBasketPageLocators.Body.SUCCESS_PAYMENT_TEXT), \
            "SUCCESS_PAYMENT_TEXT is not presented"


