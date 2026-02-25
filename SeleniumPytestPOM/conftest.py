import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
    # driver set locally is passed to request at class level
    # so that drive for other testcases in the tests folder


    request.cls.driver = driver
    yield driver
    driver.quit()

