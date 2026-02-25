import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_BrowserNav:
    def test_browser_navigation(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()

        # navigate to url
        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(2)

        # browser interactions
        title = driver.title
        print("Title:", title)

        url = driver.current_url
        print("Current URL:", url)

        time.sleep(2)

        # navigation commands
        driver.back()
        time.sleep(2)

        driver.forward()
        time.sleep(2)

        driver.refresh()
        time.sleep(2)

        driver.quit()