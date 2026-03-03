import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


class Test_Actions:
    def test_actions(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )

        driver.set_window_size(1920, 1080)

        wait = WebDriverWait(driver, 20)
        actions = ActionChains(driver)

        driver.get("https://www.amazon.in/")
        time.sleep(4)

        # -------- BEST SELLERS --------
        bestsellers = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Best')]"))
        )
        driver.execute_script("arguments[0].click();", bestsellers)
        time.sleep(3)

        driver.back()
        time.sleep(3)

        # -------- MOBILES (RIGHT CLICK) --------
        mobiles = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Mobiles')]"))
        )
        actions.context_click(mobiles).perform()
        time.sleep(3)

        # -------- PRIME (JS HOVER – FIX) --------
        prime = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Prime')]"))
        )
        driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles:true}));",
            prime
        )
        time.sleep(3)

        driver.quit()