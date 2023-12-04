from selenium.webdriver.common.by import By


class Main:
    class MainPage:
        PRODUCT_TITLES_LIST = (By.CSS_SELECTOR, "h5[data-test='product-name']")
        SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-test='search-query']")
        SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test='search-submit']")
        SORT_DROPDOWN_MENU = (By.CSS_SELECTOR, "select[data-test='sort']")
        DROPDOWN_MENU_SORT__PRICE_DESCENDING_OPTION = (By.CSS_SELECTOR, "option[value='price,desc']")
        DROPDOWN_MENU_SORT_PRICE_ASCENDING_OPTION = (By.CSS_SELECTOR, "option[value='price,asc']")
        PRODUCT_PRICES_LIST = (By.CSS_SELECTOR, "span[data-test='product-price']")

    class Header:
        SIGN_IN_BUTTON = (By.CSS_SELECTOR,"a[data-test='nav-sign-in']")
