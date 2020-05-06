from UI_tests.Pages.LoginPage import SearchHelper
from UI_tests.Pages.HomePage import HoverHelper


def test_login(browser):
    login_page = SearchHelper(browser)
    login_page.go_to_site()
    home_page = HoverHelper(browser)
    home_page.click_on_sign_in()
    login_page.fill_the_fields()
    login_page.click_on_keep_me_signed()
    login_page.click_on_the_sign_in_button()
    login_page.click_on_close_button()
    login_page.click_on_main_logo()
    assert login_page.my_account_displayed() == True


# 111
# add a few goods to shopping bag, assert valid cash $
def test_adding_to_shopping_bag():
    assert True


# to decline buy good & back to main page
def test_decline_shopping():
    assert True
