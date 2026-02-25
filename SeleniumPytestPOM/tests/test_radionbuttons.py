import time
from selenium.webdriver.common.by import By


class TestRadioButtons:

    def test_radio_buttons(self, driver):
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        time.sleep(2)

        radio1 = driver.find_element(By.XPATH, "//input[@value='radio1']")
        radio1.click()
        assert radio1.is_selected()

        time.sleep(1)

        radio2 = driver.find_element(By.XPATH, "//input[@value='radio2']")
        radio2.click()
        assert radio2.is_selected()