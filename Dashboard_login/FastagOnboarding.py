

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

Service_Obj = Service()
webdriver.Chrome(service=Service_Obj)
driver = webdriver.Chrome()
URL = "https://swift.fastag.ai/dashboard/login/?next=/dashboard/"

driver.get(URL)

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='id_username']"),