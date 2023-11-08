from selenium.webdriver.common.by import By


class Main:
    class MainPage:
        PRODUCT_TITLES_LIST = (By.CSS_SELECTOR, "h5[data-test='product-name']")
        SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-test='search-query']")
        SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test='search-submit']")

    class Header:
        pass
