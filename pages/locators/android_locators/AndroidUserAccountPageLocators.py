from selenium.webdriver.common.by import By


class AndroidUserAccountPageLocators:
    class Body:
        MY_ACCOUNT_TEXT = (By.XPATH, '/android.widget.TextView[@text="My account"]')
        # MY_FAVOURITES_BUTTON = (By.XPATH, '//android.widget.Button[@text=" Favorites"]')
        MY_FAVOURITES_BUTTON = (By.XPATH, '//*[contains(@text,"Favorites")]')
        # PROFILE_BUTTON = (By.XPATH, '/android.widget.Button[@text=" Profile"]')
        PROFILE_BUTTON = (By.XPATH, '//*[contains(@text,"Profile")]')
        # INVOICES_BUTTON = (By.XPATH, '//android.widget.Button[@text=" Invoices"]')
        INVOICES_BUTTON = (By.XPATH, '//*[contains(@text,"Invoices")]')
        # MESSAGES_BUTTON = (By.XPATH, '//android.widget.Button[@text=" Messages"]')
        MESSAGES_BUTTON = (By.XPATH, '//*[contains(@text,"Messages")]')
