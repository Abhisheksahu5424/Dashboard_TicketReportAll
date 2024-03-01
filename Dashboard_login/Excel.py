import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import openpyxl

# Load Excel data
excel_file_path = '/home/abhishek/Desktop/Masterdata_Jetson.xlsx'
df = pd.read_excel(excel_file_path)

url = "https://live23.parkzap.com/parkzap/internal/admin/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# Find and send username
driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys("abhishek.sahu@stackfusion.io")

# Find and send password
driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys("jaj!pr$O8$23AWr@po")
# Click on the login button
driver.find_element(By.XPATH, "//input[@value='Log in']").click()

# Navigate to Jetson devices
driver.find_element(By.XPATH, "//a[normalize-space()='Jetson devices']").click()

# Iterate through the rows in the DataFrame
for i, row in df.iterrows():
    try:
        # Click on the gate ID

        xpath_gate_id = f"//a[normalize-space()='{row['Gate_ID_data']}']"
        element_gate_id = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_gate_id)))
        element_gate_id.click()

        # Fill in details from the current row
        fields = ['Mac_Address', 'Static_IP', 'Static_Subnet', 'Gateway', 'DNS1', 'DNS2']
        for field in fields:
            xpath_field = f"//input[@id='id_{field.lower()}']"
            element_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_field)))
            element_field.clear()
            element_field.send_keys(row[field])

        # Save the information
        xpath_save_button = "//input[@name='_save']"
        element_save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_save_button)))
        element_save_button.click()

        # Wait for some time to ensure the data is saved
        time.sleep(3)

    except Exception as e:
        print(f"Error processing data at index {i}: {e}")

# Close the browser
driver.quit()
