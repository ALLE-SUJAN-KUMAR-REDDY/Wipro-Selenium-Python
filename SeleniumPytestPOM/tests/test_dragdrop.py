import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager


class Test_DragDrop:
    def test_dd(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        time.sleep(2)

        actions = ActionChains(driver)

        source = driver.find_element(By.XPATH, "//div[@id='column-a']")
        dest = driver.find_element(By.XPATH, "//div[@id='column-b']")

        actions.drag_and_drop(source, dest).perform()
        time.sleep(2)

        driver.close()