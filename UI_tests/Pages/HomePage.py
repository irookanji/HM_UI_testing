from .BaseApp import BasePage
from selenium.webdriver.common.by import By

from .MenPage import MenPageHelper


class SignInLocators:
    SIGN_IN = (By.CSS_SELECTOR, ".account.parbase > a:nth-of-type(1)")
    MEN = (By.XPATH, "//a//*[text()='Men']")
    MY_ACCOUNT = (By.XPATH, "//div[@class='account parbase']//a[@data-signin-state='signedin']")


class HoverHelper(BasePage):
    def click_on_sign_in(self):
        return self.find_element(SignInLocators.SIGN_IN).click()

    def my_account_displayed(self):
        return self.find_element(SignInLocators.MY_ACCOUNT).is_displayed()


class ToMenPart(BasePage):
    def choose_men(self):
        self.find_element(SignInLocators.MEN).click()
        return MenPageHelper(BasePage)

