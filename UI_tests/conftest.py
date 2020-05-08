import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import logging
from _pytest.runner import CallInfo

DEFAULT_WAIT_TIME = 10


@pytest.fixture(scope="session")
def browser():
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(DEFAULT_WAIT_TIME)
    driver.maximize_window()
    yield driver
    driver.quit()
    # Teardown
    print("\n\tI am tearing down this browser")


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)
