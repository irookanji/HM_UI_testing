from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_FIELD = (By.ID, "modal-txt-signin-email")
    PASSWORD_FIELD = (By.ID, "modal-txt-signin-password")
    KEEP_ME_SIGNED_IN = (By.CSS_SELECTOR, "#modal-spring_security_remember_me")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign in') and @type='submit']")
    CLOSE_SIGN_IN = (By.XPATH, "//*[@data-remodal-action='close']")
    MAIN_LOGO = (By.XPATH, "//*[@class='menu__hm']")
    MY_ACCOUNT = (By.XPATH, "//div[@class='account parbase']//a[@data-signin-state='signedin']")
    ALERT = (By.XPATH, "//span[contains(text(), 'Wrong email or password, please try again.')]")


class LoginHelper(BasePage):
    def fill_the_fields(self, email="abu-company@mail.ru", password="Murderer1"):
        fill_email = self.find_element(LoginLocators.EMAIL_FIELD)
        fill_email.send_keys(email)
        fill_password = self.find_element(LoginLocators.PASSWORD_FIELD)
        fill_password.send_keys(password)
        return

    def click_on_keep_me_signed(self):
        return self.find_element(LoginLocators.KEEP_ME_SIGNED_IN).click()

    def click_on_the_sign_in_button(self):
        return self.find_element(LoginLocators.SIGN_IN_BUTTON).click()

    def click_on_close_button(self):
        return self.find_element(LoginLocators.CLOSE_SIGN_IN).click()

    def click_on_main_logo(self):
        main_logo = self.find_element(LoginLocators.MAIN_LOGO)
        main_logo.click()
        self.wait_for_time(2)

    # def my_account_displayed(self):
    #     return self.find_element(LoginLocators.MY_ACCOUNT).is_displayed()

    def verify_login_failed(self):
        return self.find_element(LoginLocators.ALERT).is_displayed()
