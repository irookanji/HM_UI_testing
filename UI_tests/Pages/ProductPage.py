from .BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductPageLocators:
    SELECT_SIZE = "picker-1"
    FIRST_ELEMENT = (By.XPATH, "(//ul[contains(@class,'picker-list')]//li)[2]")
    ADD = (By.XPATH, "//span[@class='icon icon-shopping-bag-white']")


class ProductPageHelper(BasePage):
    def select_size(self):
        self.driver.find_element_by_id(ProductPageLocators.SELECT_SIZE).click()
        self.find_element(ProductPageLocators.FIRST_ELEMENT).click()
        return

    def add_to_bag(self):
        return self.find_element(ProductPageLocators.ADD).click()

    def scroll_to_select_size(self):
        return self.scroll_to(ProductPageLocators.SELECT_SIZE)
