from .BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductPageLocators:
    SELECT_SIZE = (By.CSS_SELECTOR, "#picker-1 > button")
    ADD = (By.XPATH, "//span[@class='icon icon-shopping-bag-white']")


class ProductPageHelper(BasePage):
    def select_size(self):
        select = Select(self.find_element(ProductPageLocators.SELECT_SIZE))
        select.select_by_visible_text('30/30')
        return

    def add_to_bag(self):
        return self.find_element(ProductPageLocators.ADD).click()
