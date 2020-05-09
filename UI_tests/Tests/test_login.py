from retry import retry
from selenium.common.exceptions import WebDriverException

from UI_tests.Pages.HomePage import HomePageHelper
from UI_tests.Pages.LoginPage import LoginHelper
from UI_tests.Pages.MenPage import MenPageHelper
import time


@retry(WebDriverException, tries=3, delay=0.3)
def test_valid_login(browser):
    home_page = HomePageHelper(browser)
    home_page.go_to_site()
    home_page.click_on_sign_in()
    login_page = LoginHelper(browser)
    login_page.fill_the_fields()
    login_page.click_on_keep_me_signed()
    login_page.click_on_the_sign_in_button()
    login_page.click_on_close_button()
    login_page.click_on_main_logo()
    assert home_page.my_account_displayed()


# go to Men catalog
def test_go_to_men_catalog(browser):
    home_page = HomePageHelper(browser)
    home_page.choose_men()
    men_page = MenPageHelper(browser)
    assert men_page.get_title() == 'Men | H&M GB'


# add a few goods to shopping bag, assert valid cash $
def test_adding_to_shopping_bag(browser):
    men_page = MenPageHelper(browser)
    men_page.click_on_jeans_catalog()
    men_page.choose_skinny_jeans()
    men_page.select_size()
    men_page.add_to_bag()


# to decline buy good & back to main page
def test_decline_shopping():
    assert True
