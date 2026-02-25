import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


# Your Downloads folder
DOWNLOAD_DIR = r"C:\Users\Sujan Kumar Reddy\Downloads"


class Test_Download:
    def test_dw(self):

        # Firefox preferences for auto download
        options = Options()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", DOWNLOAD_DIR)
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "image/jpeg,application/octet-stream"
        )
        options.set_preference("pdfjs.disabled", True)

        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options
        )

        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(2)

        # Click file to download
        file_link = driver.find_element(
            By.XPATH, "//a[normalize-space()='alert.jpeg']"
        )
        file_link.click()

        time.sleep(5)  # wait for download

        # Verify file downloaded
        file_path = os.path.join(DOWNLOAD_DIR, "alert.jpeg")
        assert os.path.exists(file_path)

        driver.quit()