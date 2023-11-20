from selenium.webdriver.common.by import By


class SignInPageLocators:
    class Body:
        EMAIL_INPUT_FIELD = (By.CSS_SELECTOR,"input[data-test='email']")
        PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR,"input[data-test='password']")
        LOGIN_BUTTON = (By.CSS_SELECTOR,"input[data-test='login-submit']")