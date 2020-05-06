from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class LoginLocators:
    LOCATOR_EMAIL_FIELD = (By.ID, "modal-txt-signin-email")
    LOCATOR_PASSWORD_FIELD = (By.ID, "modal-txt-signin-password")
    LOCATOR_KEEP_ME_SIGNED_IN = (By.CSS_SELECTOR, "#modal-spring_security_remember_me")
    LOCATOR_SIGN_IN_BUTTON = (By.XPATH,
                              "//button[contains(text(),'Sign in') and @type='submit']")
    LOCATOR_CLOSE_SIGN_IN = (By.XPATH, "//*[@data-remodal-action='close']")
    LOCATOR_MAIN_LOGO = (By.XPATH, "//*[@class='menu__hm']")
    LOCATOR_MY_ACCOUNT = (By.XPATH, "//div[@class='account parbase']//a[@data-signin-state='signedin']")


class SearchHelper(BasePage):

    def fill_the_fields(self, email="abu-company@mail.ru", password="Murderer1"):
        fill_email = self.find_element(LoginLocators.LOCATOR_EMAIL_FIELD)
        fill_email.send_keys(email)
        fill_password = self.find_element(LoginLocators.LOCATOR_PASSWORD_FIELD)
        fill_password.send_keys(password)
        return

    def click_on_keep_me_signed(self):
        return self.find_element(LoginLocators.LOCATOR_KEEP_ME_SIGNED_IN).click()

    def click_on_the_sign_in_button(self):
        return self.find_element(LoginLocators.LOCATOR_SIGN_IN_BUTTON).click()

    def click_on_close_button(self):
        return self.find_element(LoginLocators.LOCATOR_CLOSE_SIGN_IN).click()

    def click_on_main_logo(self):
        return self.find_element(LoginLocators.LOCATOR_MAIN_LOGO).click()

    def my_account_displayed(self):
        return self.find_element(LoginLocators.LOCATOR_MY_ACCOUNT).is_displayed()