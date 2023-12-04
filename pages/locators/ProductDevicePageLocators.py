from selenium.webdriver.common.by import By


class ProductDevicePageLocators:
    class Body:
        PRODUCT_TITLE_TEXT = (By.CSS_SELECTOR,"h1[data-test='product-name']")
        ITEM_PRICE_TEXT = (By.CSS_SELECTOR,"span[data-test='unit-price']")
        ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,"button[data-test='add-to-cart']")
        ADD_TO_CART_FAVOURITES_BUTTON = (By.CSS_SELECTOR,"button[data-test='add-to-favorites']")
        ITEM_QUANTITY_INPUT_FIELD = "input[data-test='quantity']"
        PLUS_QUANTITY_BUTTON = (By.CSS_SELECTOR,"button[data-test='increase-quantity']")
        MINUS_QUANTITY_BUTTON = (By.CSS_SELECTOR,"button[data-test='decrease-quantity']")

    class Header:
        SHOPPING_CARD_BUTTON = (By.CSS_SELECTOR,"a[data-test='nav-cart']")
        SHOPPING_CARD_COUNTER = (By.CSS_SELECTOR,"span[data-test='cart-quantity']")