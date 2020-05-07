from selenium.webdriver.support import expected_conditions as expcon
from selenium.webdriver.support.wait import WebDriverWait


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
