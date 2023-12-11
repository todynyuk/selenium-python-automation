from selenium.webdriver.common.by import By

class IOSMainPageLocators:
    class Body:
        ITEM_TEXT = (By.XPATH, "//h1[@data-test='product-name']")
        ITEM_PRICE_TEXT = (By.XPATH, "//span[@data-test='unit-price']")
        ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='btn-add-to-cart']")
        BURGER_MENU_BUTTON = (By.XPATH, "//button[@class='navbar-toggler']")
