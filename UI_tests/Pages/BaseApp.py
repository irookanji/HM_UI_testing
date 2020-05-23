import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as expcon
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www2.hm.com/en_gb/index.html"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expcon.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expcon.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_title(self):
        return self.driver.title

    @staticmethod
    def wait_for_time(seconds):
        time.sleep(seconds)

    def scroll_to(self, locator):
        element = self.find_element(locator)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_with_diapason(self):
        self.driver.execute_script("window.scrollTo(0, 906)")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 1)")

    def options(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('start-maximized')
        return chrome_options
