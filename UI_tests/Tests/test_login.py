from UI_tests.Pages.LoginPage import LoginHelper
from UI_tests.Pages.HomePage import HoverHelper, ToMenPart
from UI_tests.Pages.MenPage import MenPageHelper


def test_login(browser):
    login_page = LoginHelper(browser)
    login_page.go_to_site()
    home_page = HoverHelper(browser)
    home_page.click_on_sign_in()
    login_page.fill_the_fields()
    login_page.click_on_keep_me_signed()
    login_page.click_on_the_sign_in_button()
    login_page.click_on_close_button()
    login_page.click_on_main_logo()
    assert home_page.my_account_displayed()


# choose the jeans and the shoes
def test_choosing_the_products(browser):
    men_page = ToMenPart(browser)
    men_page.choose_men()
    assert MenPageHelper(browser).get_title() == 'Men | H&M GB'


# add a few goods to shopping bag, assert valid cash $
def test_adding_to_shopping_bag(browser):
    assert True


# to decline buy good & back to main page
def test_decline_shopping():
    assert True
