import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


DOWNLOAD_DIR = r"C:\Users\Sujan Kumar Reddy\Downloads"


class Test_Download:
    def test_dw(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        # find all links
        links = driver.find_elements(By.TAG_NAME, "a")

        # count links
        count = len(links)
        print("Total links:", count)

        # print link text
        for link in links:
            print(link.text)

        time.sleep(2)
        driver.close()