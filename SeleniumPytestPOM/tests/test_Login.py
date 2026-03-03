# check the title of the web page
import time

import pytest
from pages.Login_page import LoginPage   # ✅ important import


@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_valid_login(self, driver):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        lp = LoginPage(driver)
        lp.login("Admin", "admin123")
        assert "OrangeHRM" in driver.title
