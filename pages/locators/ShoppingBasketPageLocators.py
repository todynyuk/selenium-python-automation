from selenium.webdriver.common.by import By


class ShoppingBasketPageLocators:
    class Body:
        ITEM_DESCRIPTION_TEXT = (By.CSS_SELECTOR, "span[class='product-title']")
        ITEMS_COUNTER_INPUT_FIELD = (By.CSS_SELECTOR, "input[class='form-control quantity']")
        ITEM_PRICE_TEXT = (By.CSS_SELECTOR, "table[class='table table-hover']>tbody>tr>:nth-child(4)>span")
        TOTAL_COST_TEXT = (By.CSS_SELECTOR, "table[class='table table-hover']>tfoot>tr>:nth-child(5)")
        DELETE_ITEM_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-danger']")
        CONFIRM_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-test='proceed-1']")
        CONFIRM_SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[data-test='proceed-2']")
        CONFIRM_ADDRESS_BUTTON = (By.CSS_SELECTOR, "button[data-test='proceed-3']")
        SUCCESS_PAYMENT_TEXT = (By.CSS_SELECTOR, "div[class='help-block']")
        PAYMENT_METHOD_DROPDOWN_MENU = (By.CSS_SELECTOR, "select[id='payment-method']")
        METHOD_PAYMENT_OPTION = (By.CSS_SELECTOR, "option[value='3: Credit Card']")
        USER_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "input[id='account-name']")
        USER_NUMBER_INPUT_FIELD = (By.CSS_SELECTOR, "input[id='account-number']")
        CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "button[data-test='finish']")
        USER_LOGIN_STATUS_TEXT = (By.XPATH, "//p[contains(text(),'already logged in')]")
        ADDRESS_INPUT_FIELD = (By.CSS_SELECTOR, "input[id='address']")
