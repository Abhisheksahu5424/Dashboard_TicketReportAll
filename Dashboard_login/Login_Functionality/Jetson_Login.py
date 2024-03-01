import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def login_jetson(driver, username, password):
    try:
        url = "https://live23.parkzap.com/parkzap/internal/admin/"
        driver.get(url)
        driver.maximize_window()

        # Find element and send username
        driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys(username)

        # Find element and send password
        driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys(password)

        # Click on the login button on Dashboard
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        return True
    except Exception as error:
        print("Code run successful")
        return False



