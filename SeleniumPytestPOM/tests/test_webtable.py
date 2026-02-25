import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_Radio:

    def test_radio(self):
        # Launch Firefox browser
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )
        driver.maximize_window()

        # Open Web Tables page
        driver.get("https://the-internet.herokuapp.com/tables")
        driver.implicitly_wait(10)

        # ===============================
        # Number of rows
        # ===============================
        rows = driver.find_elements(
            By.XPATH, "//table[@id='table1']/tbody/tr"
        )
        print("No of rows:", len(rows))
        for row in rows:
            print(row.text)

        time.sleep(2)

        # ===============================
        # Number of columns
        # ===============================
        cols = driver.find_elements(
            By.XPATH, "//table[@id='table1']/tbody/tr[1]/td"
        )
        print("No of columns:", len(cols))
        for col in cols:
            print(col.text)

        time.sleep(2)

        # ===============================
        # Fetch specific cell data
        # (Row 3, Column 4 → $100.00)
        # ===============================
        celldata = driver.find_element(
            By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[4]"
        )
        print("Cell Data:", celldata.text)

        # Assertion
        assert "$100.00" in celldata.text

        # Close browser
        driver.quit()