import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_frame:

    def test_frame(self):
        # Launch Firefox browser
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )

        # Open jQuery UI DatePicker page
        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()
        time.sleep(2)
        driver.implicitly_wait(10)

        # Locate iframe and switch to it
        frame = driver.find_element(
            By.XPATH, "//iframe[@class='demo-frame']"
        )
        driver.switch_to.frame(frame)

        # Locate datepicker input box and click
        datepicker = driver.find_element(
            By.XPATH, "//input[@id='datepicker']"
        )
        datepicker.click()

        time.sleep(2)

        # Close browser
        driver.close()
        