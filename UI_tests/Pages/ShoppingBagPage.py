from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class CloseGoodiesCardLocators:
    LOCATOR_CLOSE_CARD = (By.XPATH, "//*[@class='close']")


class ShoppingBagHelper(BasePage):
    def click_on_sign_in(self):
        elements = self.find_elements(CloseGoodiesCardLocators.LOCATOR_CLOSE_CARD).click()
        for el in elements:
            el.click()
