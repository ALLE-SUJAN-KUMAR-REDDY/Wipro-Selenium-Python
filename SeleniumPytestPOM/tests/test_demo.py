import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


class Test_DemoWebShop_Checkout_E2E:

    def test_register_login_checkout(self):

        # ---------- Browser Setup ----------
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )
        wait = WebDriverWait(driver, 20)
        driver.maximize_window()

        driver.get("https://demowebshop.tricentis.com/")

        # ---------- Test Data ----------
        email = f"sujan{random.randint(1000,9999)}@test.com"
        password = "Test@123"

        # ================= REGISTER =================
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()

        wait.until(EC.element_to_be_clickable((By.ID, "gender-male"))).click()
        driver.find_element(By.ID, "FirstName").send_keys("Sujan")
        driver.find_element(By.ID, "LastName").send_keys("Reddy")
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
        driver.find_element(By.ID, "register-button").click()

        result = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "result"))
        )
        assert "completed" in result.text.lower()

        # ================= LOGOUT =================
        driver.find_element(By.LINK_TEXT, "Log out").click()

        # ================= LOGIN =================
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))).click()
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

        account = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "account"))
        )
        assert email in account.text

        # ================= ADD TO CART =================
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Books"))).click()
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Add to cart']"))
        ).click()

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='content']"))
        )

        # ================= SHOPPING CART =================
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shopping cart"))).click()

        # Agree terms
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()

        # ================= BILLING ADDRESS =================
        wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_CountryId"))).send_keys("India")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Hyderabad")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Madhapur")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("500081")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("9999999999")

        driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']").click()

        # ================= SHIPPING =================
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@onclick='Shipping.save()']")
        )).click()

        # ================= SHIPPING METHOD =================
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@onclick='ShippingMethod.save()']")
        )).click()

        # ================= PAYMENT METHOD =================
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@onclick='PaymentMethod.save()']")
        )).click()

        # ================= PAYMENT INFO =================
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@onclick='PaymentInfo.save()']")
        )).click()

        # ================= CONFIRM ORDER =================
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@onclick='ConfirmOrder.save()']")
        )).click()

        # ================= VERIFY ORDER =================
        success_msg = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//strong[contains(text(),'successfully')]")
            )
        )
        assert "successfully" in success_msg.text.lower()

        # ================= LOGOUT =================
        driver.find_element(By.LINK_TEXT, "Log out").click()

        time.sleep(2)
        driver.quit()