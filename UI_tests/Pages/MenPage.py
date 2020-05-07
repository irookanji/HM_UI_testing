from .BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MenCatalogLocators:
    JEANS_CATALOG = (By.XPATH,
                     "//*[@href='/en_gb/men/shop-by-product/jeans.html' and @role='menuitem']")
    SKINNY_JEANS = (By.XPATH, "//a[contains(@href,'productpage.0720504001.html')]")
    SELECT_SIZE = (By.CSS_SELECTOR, "#picker-1 > button")


class MenPageHelper(BasePage):
    def get_title(self):
        return self.driver.title

    def click_on_jeans_catalog(self):
        return self.find_element(MenCatalogLocators.JEANS_CATALOG).click()

    def click_on_skinny_jeans(self):
        return self.find_element(MenCatalogLocators.SKINNY_JEANS).click()

    def select_size(self):
        select_size = self.find_element(MenCatalogLocators.SELECT_SIZE)
        select_size.select_by_visible_text('30')
