from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


def test_window_handling():
    # Launch Firefox browser
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )

    # Open URL
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Click on "Click Here" link
    clickhere = driver.find_element(
        By.XPATH, "//a[normalize-space()='Click Here']"
    )
    clickhere.click()

    # Fetch window handles of both tabs
    windows = driver.window_handles
    print("Window Handles:", windows)

    # Switch to child window
    driver.switch_to.window(windows[1])

    # Get text from child window
    text = driver.find_element(
        By.XPATH, "//h3[contains(text(),'New Window')]"
    )
    print("Child Window Text:", text.text)

    # Close child window
    driver.close()

    # Switch back to parent window
    driver.switch_to.window(windows[0])

    # Verify element is displayed in parent window
    assert clickhere.is_displayed()

    # Close parent window
    driver.close()