import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calendar_picker():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    driver.get("https://rsuitejs.com/components/date-picker/#basic")

    driver.execute_script("window.scrollBy(0, 400)")

    date_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@placeholder='MM/dd/yyyy']")
    ))
    date_input.click()

    date_24 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='24' and not(contains(@class,'disabled'))]")
    ))
    date_24.click()

    ok_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='OK']")
    ))
    ok_button.click()

    time.sleep(2)
    driver.quit()