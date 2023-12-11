from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage


class IOSMainPage(BasePage):

    def swipe_by_coordinates(self, ios_driver, start_x, start_y, end_x, end_y):
        actions = ActionChains(ios_driver)
        actions.w3c_actions = ActionBuilder(ios_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def get_item_text_by_index(self, ios_driver, index):
        return ios_driver.find_element(By.XPATH,
                                       f"(//h5[@data-test='product-name'])[{index}]").text

    def click_on_item_by_index(self, ios_driver, index):
        ios_driver.find_element(By.XPATH, f"(//a[@class='card'])[{index}]").click()
