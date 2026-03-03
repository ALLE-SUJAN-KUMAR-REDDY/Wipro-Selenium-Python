'''
locators = Page actions

reusability
easy maintenance
readability

login page
1. verify login with valid credentials
2. verify login with invalid credentials
3. verify password masking
4. verify with blank credentials
5. verify input text field validation
6. verify password field allowance
7. verify logo of the login page
'''

from selenium.webdriver.common.by import By
class LoginPage:

    # locators
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")
    dashboard_text = (By.XPATH, "//h6[normalize-space()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver

    # enter username
    def enter_username(self, username):
        self.driver.find_element(self.username_input).send_keys(username)

    # enter password
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # click on login button
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    # combined login method
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()