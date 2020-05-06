from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class SignInLocators:
    LOCATOR_SIGN_IN = (By.CSS_SELECTOR, ".account.parbase > a:nth-of-type(1)")


class HoverHelper(BasePage):
    def click_on_sign_in(self):
        return self.find_element(SignInLocators.LOCATOR_SIGN_IN).click()
