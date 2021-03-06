import pytest
from retry import retry
from selenium.common.exceptions import WebDriverException

from UI_tests.Pages.HomePage import HomePageHelper
from UI_tests.Pages.LoginPage import LoginHelper


@retry(WebDriverException, tries=2, delay=0.3)
@pytest.mark.parametrize("login, passwd, rez",
                         [
                             ("wrongLogin@mail.com", "Murderer1", "Sign In"),
                             ("abu-company@mail.ru", "wrongPass", "Sign In"),
                             ("abu-company@mail.ru", "Murderer1", "My Account")
                         ])
def test_ui_login(browser, login, passwd, rez):
    home_page = HomePageHelper(browser)
    home_page.go_to_site()
    home_page.click_on_sign_in()
    login_page = LoginHelper(browser)
    login_page.fill_the_fields(login, passwd)
    login_page.click_on_the_sign_in_button()
    login_page.click_on_close_button()
    login_page.click_on_main_logo()
    assert home_page.my_account_displayed()


def test_invalid_login():
    pass


def test_logout():
    pass
