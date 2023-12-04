from selenium.webdriver.common.by import By


class AndroidMainPageLocators:
    class Body:
        FILTER_BUTTON = (By.XPATH, '//*[contains(@text,"Filters")]')
        SEARCH_INPUT_FIELD = (By.XPATH, '//android.widget.Button[@text="X"]/preceding-sibling::android.widget.EditText')
        SEARCH_BUTTON = (By.XPATH, '//android.widget.Button[@text="Search"]')

    class Header:
        BURGER_MENU_BUTTON = (By.XPATH, '//android.view.ViewGroup[@content-desc="test-Menu"]')
        CART_BUTTON = (By.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]')
