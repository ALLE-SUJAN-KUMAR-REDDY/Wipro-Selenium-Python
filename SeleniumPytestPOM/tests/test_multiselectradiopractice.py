import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_Gender_Days:

    def test_select_gender_and_days(self):
        # Launch browser
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )
        driver.maximize_window()

        # Open URL
        driver.get("https://testautomationpractice.blogspot.com/")
        time.sleep(3)

        # ---------- Select Gender (Female) ----------
        female_radio = driver.find_element(By.ID, "female")
        female_radio.click()
        time.sleep(2)

        # ---------- Select Days (All Checkboxes) ----------
        days_checkboxes = driver.find_elements(
            By.XPATH, "//input[@type='checkbox']"
        )

        print("Total days checkboxes:", len(days_checkboxes))

        for day in days_checkboxes:
            if not day.is_selected():
                day.click()
                time.sleep(1)

        # Close browser
        driver.quit()
