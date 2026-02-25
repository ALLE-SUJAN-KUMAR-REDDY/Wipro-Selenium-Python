import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


class Test_OrangeHRM_PIM:

    def test_select_from_second_checkbox(self):
        # Firefox options (IMPORTANT)
        options = Options()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options
        )

        wait = WebDriverWait(driver, 20)

        # Open login page FIRST
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Now maximize (safe)
        driver.maximize_window()

        # -------- Login --------
        wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # -------- Go to PIM --------
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
        time.sleep(3)

        # -------- Select checkboxes from SECOND --------
        checkboxes = driver.find_elements(
            By.XPATH, "//div[@role='row']//input[@type='checkbox']"
        )

        print("Total checkboxes found:", len(checkboxes))

        for checkbox in checkboxes[1:]:  # start from second
            driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            time.sleep(1)
            if not checkbox.is_selected():
                checkbox.click()
                time.sleep(1)

        driver.quit()