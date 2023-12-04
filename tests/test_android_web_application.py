from pages.android_pages.AndroidMainPage import AndroidMainPage
from pages.android_pages.AndroidLoginPage import AndroidLoginPage
from pages.android_pages.AndroidUserAccountPage import AndroidUserAccountPage
from pages.android_pages.TabsPage import TabsPage
from pages.android_pages.ChromeMainPage import ChromeMainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pages.locators.android_locators.AndroidLoginPageLocators import AndroidLoginPageLocators
from pages.locators.android_locators.AndroidUserAccountPageLocators import AndroidUserAccountPageLocators


class TestAndroidMainPage:

    def test_search_and_check(self, mobile_driver):
        mobile_driver.find_element(By.XPATH,
                                   '//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]').send_keys(
            'https://practicesoftwaretesting.com')
        mobile_driver.find_element(By.XPATH, '(//android.widget.LinearLayout)[4]').click()
        mobile_driver.switch_to.context('NATIVE_APP')
        time.sleep(3)
        main_page = AndroidMainPage(mobile_driver)
        mobile_driver.find_element(By.XPATH, '//*[contains(@text,"Filters")]').click()
        time.sleep(3)
        main_page.fill_search_input_field(mobile_driver, "Drill")
        time.sleep(3)
        main_page.search_button_click(mobile_driver)
        time.sleep(3)
        mobile_driver.find_element(By.XPATH, '//*[contains(@text,"Filters")]').click()
        assert main_page.verify_is_search_think_present_in_goods_title(mobile_driver, "Drill")

    def test_login_user(self, mobile_driver):
        mobile_driver.find_element(By.XPATH,
                                   '//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]').send_keys(
            'https://practicesoftwaretesting.com/#/auth/login')
        mobile_driver.find_element(By.XPATH, '(//android.widget.LinearLayout)[4]').click()
        mobile_driver.switch_to.context('NATIVE_APP')
        time.sleep(3)
        login_page = AndroidLoginPage(mobile_driver)
        time.sleep(5)
        login_page.fill_input_field(AndroidLoginPageLocators.Body.EMAIL_INPUT_FIELD, mobile_driver,
                                    "noges93919@ikanid.com")
        login_page.fill_input_field(AndroidLoginPageLocators.Body.PASSWORD_INPUT_FIELD, mobile_driver, "Noges93919")
        login_page.login_button_click(mobile_driver)
        time.sleep(3)
        user_account_page = AndroidUserAccountPage(mobile_driver)
        assert user_account_page.check_is_element_presented(mobile_driver,
                                                            AndroidUserAccountPageLocators.Body.MY_ACCOUNT_TEXT), \
            "MY_ACCOUNT_TEXT is not presented"
        assert user_account_page.check_is_element_presented(mobile_driver,
                                                            AndroidUserAccountPageLocators.Body.MY_FAVOURITES_BUTTON), \
            "MY_FAVOURITES_BUTTON is not presented"
        assert user_account_page.check_is_element_presented(mobile_driver,
                                                            AndroidUserAccountPageLocators.Body.PROFILE_BUTTON), \
            "PROFILE_BUTTON is not presented"
        assert user_account_page.check_is_element_presented(mobile_driver,
                                                            AndroidUserAccountPageLocators.Body.INVOICES_BUTTON), \
            "INVOICES_BUTTON is not presented"
        assert user_account_page.check_is_element_presented(mobile_driver,
                                                            AndroidUserAccountPageLocators.Body.MESSAGES_BUTTON), \
            "MESSAGES_BUTTON is not presented"

    def test_login_user_web(self, mobile_driver):
        webview = mobile_driver.contexts[1]
        mobile_driver.switch_to.context(webview)
        time.sleep(3)
        mobile_driver.get("https://practicesoftwaretesting.com/#/auth/login")
        time.sleep(3)
        mobile_driver.find_element(By.XPATH, "//input[@data-test='email']").send_keys("noges93919@ikanid.com")
        mobile_driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("Noges93919")
        mobile_driver.find_element(By.XPATH, "//input[@data-test='login-submit']").click()
        mobile_driver.find_element(By.XPATH, "//input[@data-test='login-submit']").send_keys(Keys.ENTER)
        time.sleep(10)
        my_favourites_button_status = mobile_driver.find_element(By.XPATH,
                                                                 "//a[@data-test='nav-favorites']").is_enabled()
        profile_button_status = mobile_driver.find_element(By.XPATH, "//a[@data-test='nav-profile']").is_enabled()
        invoices_button_status = mobile_driver.find_element(By.XPATH, "//a[@data-test='nav-invoices']").is_enabled()
        messages_button_status = mobile_driver.find_element(By.XPATH, "//a[@data-test='nav-messages']").is_enabled()
        assert my_favourites_button_status, "MY_FAVOURITES_BUTTON is not presented"
        assert profile_button_status, "PROFILE_BUTTON is not presented"
        assert invoices_button_status, "INVOICES_BUTTON is not presented"
        assert messages_button_status, "MESSAGES_BUTTON is not presented"

    def test_switching_context(self, mobile_driver):
        default_context = mobile_driver.context
        webview = mobile_driver.contexts[1]
        mobile_driver.switch_to.context(webview)
        new_context = mobile_driver.context
        assert str(default_context) != str(new_context)
        mobile_driver.get("https://practicesoftwaretesting.com")
        time.sleep(3)
        mobile_driver.find_element(By.XPATH, '//a[@data-test="filters"]').click()
        time.sleep(3)
        mobile_driver.find_element(By.XPATH, '//a[@data-test="filters"]').click()
        time.sleep(5)
        mobile_driver.switch_to.context(mobile_driver.contexts[0])
        second_default_context = mobile_driver.context
        assert str(default_context) == str(second_default_context), "Contexts are not equals"
        main_page = AndroidMainPage(mobile_driver)
        main_page.click_tabs_button(mobile_driver)
        tabs_page = TabsPage(mobile_driver)
        first_tabs_list_length = tabs_page.get_tabs_list_length(mobile_driver)
        assert first_tabs_list_length == 1, "first_tabs_list have zero or more than one element"
        tabs_page.click_create_new_tab(mobile_driver)
        search_input_field_status = mobile_driver.find_element(By.ID,
                                                               'com.android.chrome:id/search_box_text').is_enabled()
        assert search_input_field_status, "search_input_field_status is not presented"
        chrome_main_page = ChromeMainPage(mobile_driver)
        chrome_main_page.click_tabs_button(mobile_driver)
        time.sleep(3)
        second_tabs_list_length = tabs_page.get_tabs_list_length(mobile_driver)
        assert second_tabs_list_length != 1, "second_tabs_list have zero or one element"
        tabs_page.click_on_tab_by_index(mobile_driver, 1)
        time.sleep(3)
        website_logo_status = mobile_driver.find_element(By.XPATH,
                                                         '//android.widget.Image[@resource-id="Layer_1"]').is_enabled()
        assert website_logo_status, "website_logo_status is not presented"
