from selenium.webdriver.common.by import By


class ShoppingBasketPageLocators:
    class Body:
        ITEM_DESCRIPTION_TEXT = (By.CSS_SELECTOR,"span[class='product-title']")
        ITEMS_COUNTER_INPUT_FIELD = (By.CSS_SELECTOR,"input[class='form-control quantity']")
        ITEM_PRICE_TEXT = (By.CSS_SELECTOR,"table[class='table table-hover']>tbody>tr>:nth-child(4)>span")
        TOTAL_COST_TEXT = (By.CSS_SELECTOR,"table[class='table table-hover']>tfoot>tr>:nth-child(5)")
        DELETE_ITEM_BUTTON = (By.CSS_SELECTOR,"a[class='btn btn-danger']")
        ORGANIZE_CHECKOUT_BUTTON = (By.CSS_SELECTOR,"button[data-test='proceed-1']")