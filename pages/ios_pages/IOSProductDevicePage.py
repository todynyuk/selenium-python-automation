from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage
from pages.locators.ios_locators.IOSProductDevicePageLocators import IOSMainPageLocators


class IOSProductDevicePage(BasePage):

    def get_item_text(self, ios_driver):
        return ios_driver.find_element(By.XPATH, "//h1[@data-test='product-name']").text
