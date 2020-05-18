from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class ShoppingBagPageLocators:
    LOCATOR_CLOSE_CARD = (By.XPATH, "//*[@class='close']")
    PAGE_TITLE = (By.XPATH, "//h1[text()='Shopping bag']")


class ShoppingBagHelper(BasePage):
    def refuse_purchase(self):
        elements = self.find_element(ShoppingBagPageLocators.LOCATOR_CLOSE_CARD)
        for el in elements:
            el.click()

    def shopping_bag_title(self):
        return self.find_element(ShoppingBagPageLocators.PAGE_TITLE).text
