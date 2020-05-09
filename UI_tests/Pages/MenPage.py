from .BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MenCatalogLocators:
    JEANS_CATALOG = (By.XPATH,
                     "//*[@href='/en_gb/men/shop-by-product/jeans.html' and @role='menuitem']")
    SKINNY_JEANS = (By.XPATH, "//a[contains(@href,'productpage.0720504001.html')]")


class MenPageHelper(BasePage):
    def click_on_jeans_catalog(self):
        return self.find_element(MenCatalogLocators.JEANS_CATALOG).click()

    def choose_skinny_jeans(self):
        return self.find_element(MenCatalogLocators.SKINNY_JEANS).click()
