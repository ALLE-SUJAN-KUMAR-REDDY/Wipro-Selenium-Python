import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


class Test_Keyboard:
    def test_keyboard_copy_paste(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )

        # ✅ FORCE Facebook login layout
        driver.set_window_position(0, 0)
        driver.set_window_size(1366, 768)

        wait = WebDriverWait(driver, 20)
        actions = ActionChains(driver)

        driver.get("https://www.facebook.com/")
        time.sleep(3)

        # ✅ Scroll right to make login form visible
        driver.execute_script("window.scrollTo(300, 0)")
        time.sleep(2)

        email = wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )

        email.click()
        email.send_keys("seleniumtest")
        time.sleep(2)

        # CTRL + A
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        time.sleep(1)

        # CTRL + C
        actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        time.sleep(1)

        # TAB → password field
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)

        # CTRL + V
        actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(3)

        driver.quit()