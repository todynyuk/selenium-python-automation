from selenium.webdriver.common.by import By


class AndroidLoginPageLocators:
    class Body:
        EMAIL_INPUT_FIELD = (By.XPATH, '/android.widget.EditText[@resource-id="email"]')
        PASSWORD_INPUT_FIELD = (By.XPATH, '//android.widget.EditText[@resource-id="password"]')
        LOGIN_BUTTON = (By.XPATH, '//android.widget.Button[@text = "Login"]')
