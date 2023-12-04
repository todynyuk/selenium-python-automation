# email="noges93919@ikanid.com"
# password="Noges93919"
import pytest
from pages.SignInPage import SignInPage
from pages.MainPage import MainPage
from pages.UserAccountPage import UserAccountPage
import pages.locators.SignInPageLocators as SignInLocators
import pages.locators.UserAccountPageLocators as UserAccountLocators
import time


class TestLoginPage:

    def test_login_user_and_check(self, driver):
        main_page = MainPage(driver)
        main_page.click_sign_in_button()
        login_page = SignInPage(driver)
        login_page.fill_input_field(SignInLocators.SignInPageLocators.Body.EMAIL_INPUT_FIELD, "noges93919@ikanid.com")
        login_page.fill_input_field(SignInLocators.SignInPageLocators.Body.PASSWORD_INPUT_FIELD, "Noges93919")
        login_page.click_login_button()
        user_account_page = UserAccountPage(driver)
        profile_button_status = user_account_page.check_is_element_presented(
            UserAccountLocators.UserAccountPageLocators.Body.PROFILE_BUTTON)
        invoices_button_status = user_account_page.check_is_element_presented(
            UserAccountLocators.UserAccountPageLocators.Body.INVOICES_BUTTON)
        messages_button_status = user_account_page.check_is_element_presented(
            UserAccountLocators.UserAccountPageLocators.Body.MESSAGES_BUTTON)
        my_favourites_button_status = user_account_page.check_is_element_presented(
            UserAccountLocators.UserAccountPageLocators.Body.MY_FAVOURITES_BUTTON)
        assert profile_button_status, "profile_button_status is not presented"
        assert invoices_button_status, "invoices_button_status is not presented"
        assert messages_button_status, "messages_button_status is not presented"
        assert my_favourites_button_status, "my_favourites_button_status is not presented"
