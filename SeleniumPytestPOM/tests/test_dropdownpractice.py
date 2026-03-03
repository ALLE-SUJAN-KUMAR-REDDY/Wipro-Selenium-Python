import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


class Test_DropDown:

    def test_dropdown(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )
        driver.maximize_window()

        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(3)

        # ---------- Single Select Dropdown ----------
        single_dropdown = driver.find_element(By.ID, "option")
        sel1 = Select(single_dropdown)

        sel1.select_by_visible_text("Option 1")
        time.sleep(2)

        # ---------- Multi Select Dropdown ----------
        multi_dropdown = driver.find_element(By.ID, "owc")
        sel2 = Select(multi_dropdown)

        sel2.select_by_visible_text("Option 1")
        time.sleep(2)

        sel2.select_by_visible_text("Option 2")
        time.sleep(2)

        sel2.select_by_visible_text("Option 3")
        time.sleep(2)

        # ---------- Deselect ----------
        sel2.deselect_by_visible_text("Option 2")
        time.sleep(2)

        sel2.deselect_all()
        time.sleep(2)

        driver.quit()