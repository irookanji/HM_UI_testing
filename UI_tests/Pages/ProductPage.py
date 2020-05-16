from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .BaseApp import BasePage


class ProductPageLocators:
    SELECT_SIZE = (By.XPATH,
                   "//div[@id='picker-1']//button[contains(@class,'trigger-button')]//span[contains(text(),'Select size')]")
    FIRST_ELEMENT = (By.XPATH, "(//ul[contains(@class,'picker-list')]//li)[2]")
    ADD = (By.XPATH, "//span[@class='icon icon-shopping-bag-white']")
    SHOPPING_BAG = (By.XPATH, "//a[@href='/en_gb/cart' and @class='goto-shopping-bag']")
    MAIN_LOGO = (By.XPATH, "//*[@class='menu__hm']")


class ProductPageHelper(BasePage):
    def select_size(self):
        self.wait_for_time(5)
        self.find_element(ProductPageLocators.SELECT_SIZE).click()
        self.find_element(ProductPageLocators.FIRST_ELEMENT).click()
        return

    def add_to_bag(self):
        return self.find_element(ProductPageLocators.ADD).click()

    def go_to_shopping_bag(self):
        return self.find_element(ProductPageLocators.SHOPPING_BAG).click()

    def click_on_main_logo(self):
        main_logo = self.find_element(ProductPageLocators.MAIN_LOGO)
        main_logo.click()
        self.wait_for_time(2)
