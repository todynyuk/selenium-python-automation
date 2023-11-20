from selenium.webdriver.common.by import By


class UserAccountPageLocators:
    class Body:
        MY_FAVOURITES_BUTTON = (By.CSS_SELECTOR,"a[data-test='nav-favorites']")
        PROFILE_BUTTON = (By.CSS_SELECTOR,"a[data-test='nav-profile']")
        INVOICES_BUTTON = (By.CSS_SELECTOR,"a[data-test='nav-invoices']")
        MESSAGES_BUTTON = (By.CSS_SELECTOR,"a[data-test='nav-messages']")

    class Header:
        USER_NAME_TEXT = (By.CSS_SELECTOR,"a[data-test='nav-user-menu']")
        SIGN_OUT_BUTTON = (By.CSS_SELECTOR,"a[data-test='nav-sign-out']")