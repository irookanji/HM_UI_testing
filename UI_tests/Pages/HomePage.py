from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from .BaseApp import BasePage


class SignInLocators:
    SIGN_IN = (By.CSS_SELECTOR, ".account.parbase > a:nth-of-type(1)")
    SIGN_OUT = (By.XPATH, "//*[@href='/en_gb/logout' and text()='Sign out']")
    MEN = (By.XPATH, "//a//*[text()='Men']")
    MY_ACCOUNT = (By.XPATH, "//div[@class='account parbase']//a[@data-signin-state='signedin']")
    CLOSE_COOKIE = (By.XPATH, "//div[contains(@class, 'cookie-notification')]//button")


class HomePageHelper(BasePage):
    def click_on_sign_in(self):
        return self.find_element(SignInLocators.SIGN_IN).click()

    def my_account_displayed(self):
        return self.find_element(SignInLocators.MY_ACCOUNT).is_displayed()

    def choose_men(self):
        return self.find_element(SignInLocators.MEN).click()

    def close_cookie(self):
        if self.find_element(SignInLocators.CLOSE_COOKIE).is_displayed():
            return self.find_element(SignInLocators.CLOSE_COOKIE).click()

    def sign_out(self):
        hover = ActionChains(self).move_to_element(self.find_element(SignInLocators.MY_ACCOUNT))
        hover.perform()
        self.find_element(SignInLocators.SIGN_OUT).click()
        return
