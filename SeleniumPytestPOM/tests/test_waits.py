import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Test_waits:

    def test_waits(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )

        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        driver.maximize_window()

        # -------------------------------
        # Implicit Wait
        # -------------------------------
        driver.implicitly_wait(5)

        # Click Start button
        driver.find_element(By.XPATH, "//button").click()

        # -------------------------------
        # Explicit Wait
        # -------------------------------
        wait = WebDriverWait(driver, 10)
        hello_text = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h4[text()='Hello World!']")
            )
        )

        print("Text appeared:", hello_text.text)

        # -------------------------------
        # Fluent Wait
        # -------------------------------
        fluent_wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException]
        )

        fluent_wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "finish"),
                "Hello World!"
            )
        )

        print("Fluent wait successful")

        driver.quit()