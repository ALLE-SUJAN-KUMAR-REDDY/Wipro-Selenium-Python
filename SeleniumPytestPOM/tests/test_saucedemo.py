import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_SauceDemo_E2E:

    def test_saucedemo_end_to_end(self):

        # ---------- VARIABLES ----------
        URL = "https://www.saucedemo.com/"
        USERNAME = "standard_user"
        PASSWORD = "secret_sauce"

        try:
            print("Launching browser...")
            driver = webdriver.Firefox(
                service=Service(GeckoDriverManager().install())
            )
            driver.maximize_window()

            # ---------- OPEN URL ----------
            print("Opening SauceDemo website")
            driver.get(URL)
            time.sleep(3)

            # ---------- LOGIN ----------
            print("Entering username")
            driver.find_element(By.ID, "user-name").send_keys(USERNAME)
            time.sleep(1)

            print("Entering password")
            driver.find_element(By.ID, "password").send_keys(PASSWORD)
            time.sleep(1)

            print("Clicking Login button")
            driver.find_element(By.ID, "login-button").click()
            time.sleep(3)

            # ---------- ADD PRODUCT TO CART ----------
            print("Adding product to cart")
            driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            time.sleep(2)

            # ---------- GO TO CART ----------
            print("Opening cart")
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            time.sleep(2)

            # ---------- CHECKOUT ----------
            print("Clicking checkout")
            driver.find_element(By.ID, "checkout").click()
            time.sleep(2)

            # ---------- ENTER CHECKOUT DETAILS ----------
            print("Entering checkout details")
            driver.find_element(By.ID, "first-name").send_keys("Sujan")
            driver.find_element(By.ID, "last-name").send_keys("Reddy")
            driver.find_element(By.ID, "postal-code").send_keys("500001")
            time.sleep(2)

            print("Continuing checkout")
            driver.find_element(By.ID, "continue").click()
            time.sleep(2)

            # ---------- FINISH ORDER ----------
            print("Finishing order")
            driver.find_element(By.ID, "finish").click()
            time.sleep(3)

            print("Order placed successfully!")

        except Exception as e:
            print("Test failed due to error:")
            print(e)

        finally:
            print("Closing browser")
            driver.quit()