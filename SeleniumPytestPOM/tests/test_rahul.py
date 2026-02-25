import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_SeleniumPractise_E2E:

    def test_end_to_end(self):

        # ---------- VARIABLES ----------
        BASE_URL = "https://rahulshettyacademy.com/seleniumPractise/#/"
        SEARCH_ITEM = "Tomato"
        COUNTRY = "India"

        try:
            print("Launching browser...")
            driver = webdriver.Firefox(
                service=Service(GeckoDriverManager().install())
            )
            driver.maximize_window()

            # ---------- OPEN BASE URL ----------
            print("Opening site:", BASE_URL)
            driver.get(BASE_URL)
            time.sleep(3)

            # ---------- SEARCH FOR PRODUCT ----------
            print("Searching for product:", SEARCH_ITEM)
            search_box = driver.find_element(By.CSS_SELECTOR, "input.search-keyword")
            search_box.send_keys(SEARCH_ITEM)
            time.sleep(3)

            # ---------- ADD PRODUCT TO CART ----------
            print("Adding product to cart")
            add_buttons = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
            if len(add_buttons) > 0:
                add_buttons[0].click()
                time.sleep(2)
            else:
                print("No add button found!")

            # ---------- VIEW CART ----------
            print("Opening cart")
            driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()
            time.sleep(2)

            print("Proceed to checkout")
            driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
            time.sleep(3)

            # ---------- APPLY PROMO (optional display) ----------
            print("On checkout page")
            time.sleep(3)

            # ---------- PLACE ORDER ----------
            print("Placing order")
            driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
            time.sleep(3)

            # ---------- SELECT COUNTRY ----------
            print("Selecting country:", COUNTRY)
            dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
            dropdown.select_by_visible_text(COUNTRY)
            time.sleep(2)

            # ---------- ACCEPT TERMS ----------
            print("Accepting terms and conditions")
            driver.find_element(By.CLASS_NAME, "chkAgree").click()
            time.sleep(2)

            # ---------- PROCEED ----------
            print("Proceeding")
            driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
            time.sleep(4)

            print("End to End Automation Completed Successfully ✔️")

        except Exception as e:
            print("Test Failed ❌ Error:")
            print(e)

        finally:
            print("Closing browser")
            driver.quit()