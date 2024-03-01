import time

import action
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = "https://dashboard.parkzap.com/login"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(2)

Sites = ["Ahmedabad Airport T2", "Ascendas-Singbridge Gurgaon", "IGI Terminal 3 Toll Plaza"]
Gate_Name = ["IN01", "OUT01", "PS7", "PS101", "PS102", "PS4", "EN12", "EN13"]

# Find and send username
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("abhishek.sahu@stackfusion.io")

# Find and send password
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("jaj!pr$O8$23AWr@po")

# Click on the login button
driver.find_element(By.XPATH, "//span[@class='MuiButton-label']").click()
time.sleep(5)
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/span[1]/*[name()='svg'][1]/*[name()='path'][1]").click()
print("Click")

time.sleep(5)
driver.find_element(By.XPATH, "#mui-97217-option-30").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/ul[1]/li[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]").click()
time.sleep(4)
