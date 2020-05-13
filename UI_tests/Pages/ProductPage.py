from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .BaseApp import BasePage


class ProductPageLocators:
    SELECT_SIZE = "picker-1"
    FIRST_ELEMENT = (By.XPATH, "(//ul[contains(@class,'picker-list')]//li)[2]")
    ADD = (By.XPATH, "//span[@class='icon icon-shopping-bag-white']")
    SHOPPING_BAG = (By.XPATH, "//a[@href='/en_gb/cart' and contains(@class,'menu__bag')]")


class ProductPageHelper(BasePage):
    def select_size(self):
        self.wait_for_time(5)
        element = self.driver.find_element_by_id(ProductPageLocators.SELECT_SIZE)
        self.driver.execute_script("arguments[0].click();", element)
        return

    def add_to_bag(self):
        return self.find_element(ProductPageLocators.ADD).click()

    def scroll_to_select_size(self):
        return self.scroll_to(ProductPageLocators.SELECT_SIZE)

    def go_to_shopping_bag(self):
        return self.find_element(ProductPageLocators.SHOPPING_BAG).click()
