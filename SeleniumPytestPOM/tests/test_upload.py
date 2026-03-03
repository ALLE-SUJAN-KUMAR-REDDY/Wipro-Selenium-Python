import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


class Test_Upload:
    def test_up(self):
        options = Options()
        options.add_argument("--width=1366")
        options.add_argument("--height=768")
        options.add_argument("--disable-gpu")

        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options
        )

        # small wait to ensure browser is ready
        time.sleep(2)

        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(2)

        # -------- Upload file --------
        browse = driver.find_element(By.ID, "file-upload")
        browse.send_keys(
            r"C:\Users\Sujan Kumar Reddy\Downloads\CT20244445822 (1).jpg"
        )
        time.sleep(2)

        # -------- Click upload --------
        upload_btn = driver.find_element(By.ID, "file-submit")
        upload_btn.click()
        time.sleep(2)

        # -------- Assertion --------
        result = driver.find_element(By.TAG_NAME, "h3")
        assert result.text == "File Uploaded!"

        driver.quit()