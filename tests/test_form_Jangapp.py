from browser.browser_helper import new_chrome_window
from selenium.webdriver.common.by import By

import time

def test_form():
    # Open the page
    driver = new_chrome_window()
    driver.get("https://hangers-crisbusa.web.app/")

    #scroll to search the form
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.55);")
    time.sleep(3)

    #enter information in the inputs
    driver.find_element(By.NAME, "firstname").send_keys("Diana")
    driver.find_element(By.NAME, "lastname").send_keys("Servin")
    driver.find_element(By.NAME, "email").send_keys("servinaguileradiana@gmail.com")
    driver.find_element(By.NAME, "message").send_keys("This is a test")
    driver.find_element(By.CLASS_NAME, "bd-btn-link").click()
    time.sleep(2)


    driver.quit()
