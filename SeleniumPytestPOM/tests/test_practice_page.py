import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_practice_page():
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    wait = WebDriverWait(driver, 10)

    # --------------------------------------------------
    # Helper function to scroll to element
    # --------------------------------------------------
    def scroll_to(element):
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )
        time.sleep(1)

    # ==================================================
    # 1. Suggestion Class Example
    # ==================================================
    suggestion = driver.find_element(By.ID, "autocomplete")
    scroll_to(suggestion)
    suggestion.send_keys("Ind")
    time.sleep(1)
    suggestion.send_keys(Keys.ARROW_DOWN)
    suggestion.send_keys(Keys.ENTER)

    # ==================================================
    # 2. Open Window → Child → Close → Parent
    # ==================================================
    parent = driver.current_window_handle
    open_window = driver.find_element(By.ID, "openwindow")
    scroll_to(open_window)
    open_window.click()

    for win in driver.window_handles:
        if win != parent:
            driver.switch_to.window(win)
            print("Child Window Title:", driver.title)
            driver.close()

    driver.switch_to.window(parent)

    # ==================================================
    # 3. Open Tab → Switch → Close → Parent
    # ==================================================
    open_tab = driver.find_element(By.ID, "opentab")
    scroll_to(open_tab)
    open_tab.click()

    for win in driver.window_handles:
        if win != parent:
            driver.switch_to.window(win)
            print("Tab Title:", driver.title)
            driver.close()

    driver.switch_to.window(parent)

    # ==================================================
    # 4. Alerts & Confirm
    # ==================================================
    name = driver.find_element(By.ID, "name")
    scroll_to(name)
    name.send_keys("Sujan")

    driver.find_element(By.ID, "alertbtn").click()
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    alert.accept()

    driver.find_element(By.ID, "confirmbtn").click()
    confirm = driver.switch_to.alert
    print("Confirm Text:", confirm.text)
    confirm.dismiss()

    # ==================================================
    # 5. Web Table Fixed Header → Chennai
    # ==================================================
    fixed_table = driver.find_element(By.CLASS_NAME, "tableFixHead")
    scroll_to(fixed_table)

    rows = driver.find_elements(
        By.XPATH, "//div[@class='tableFixHead']//tbody/tr"
    )

    for row in rows:
        if "Chennai" in row.text:
            print("Fixed Table Row:", row.text)

    # ==================================================
    # 6. Web Table Example → Highlighted Course
    # ==================================================
    courses_table = driver.find_element(By.ID, "product")
    scroll_to(courses_table)

    highlighted = driver.find_element(
        By.XPATH,
        "//table[@name='courses']//td[contains(text(),'Advanced Selenium Framework')]"
    )
    print("Highlighted Course:", highlighted.text)

    # ==================================================
    # 7. Mouse Hover → Top
    # ==================================================
    mouse_hover = driver.find_element(By.ID, "mousehover")
    scroll_to(mouse_hover)

    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover).perform()
    time.sleep(1)

    top = driver.find_element(By.LINK_TEXT, "Top")
    top.click()

    # ==================================================
    # 8. iFrame → Get Text
    # ==================================================
    iframe = driver.find_element(By.ID, "courses-iframe")
    scroll_to(iframe)

    driver.switch_to.frame(iframe)
    iframe_text = driver.find_element(
        By.XPATH, "//a[contains(text(),'Mentorship')]"
    )
    print("iFrame Text:", iframe_text.text)

    driver.switch_to.default_content()

    time.sleep(2)
    driver.quit()