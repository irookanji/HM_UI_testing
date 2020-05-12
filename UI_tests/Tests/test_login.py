from retry import retry
from selenium.common.exceptions import WebDriverException

from UI_tests.Pages.HomePage import HomePageHelper
from UI_tests.Pages.LoginPage import LoginHelper
from UI_tests.Pages.MenPage import MenPageHelper
from UI_tests.Pages.ProductPage import ProductPageHelper
from UI_tests.Pages.ShoppingBagPage import ShoppingBagHelper
from UI_tests.conftest import browser


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
    home_page.close_cookie()
    men_page = MenPageHelper(browser)
    assert men_page.get_title() == 'Men | H&M GB'


# add a few goods to shopping bag, assert valid cash $
@retry(WebDriverException, tries=2, delay=0.3)
def test_adding_to_shopping_bag(browser):
    men_page = MenPageHelper(browser)
    men_page.click_on_jeans_catalog()
    men_page.choose_skinny_jeans()

    product_page = ProductPageHelper(browser)
    product_page.scroll_to_select_size()
    product_page.select_size()
    product_page.add_to_bag()
    product_page.wait_for_time(2)
    product_page.go_to_shopping_bag()
    shopping_bag = ShoppingBagHelper(browser)
    assert shopping_bag.shopping_bag_title() == 'SHOPPING BAG'


# to decline buy good & back to main page
def test_decline_shopping():
    bag_page = ShoppingBagHelper(browser)
    bag_page.refuse_purchase()


def go_to_favorites():
    pass
