import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://barrelscope.parkzap.com/login"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(2)
create = driver.find_element(By.XPATH, "//a[normalize-space()='Create account']")
create.click()
if create.is_displayed():
    print("Registration form is displayed. ....."
          "PASS......")
else:
    print("Registration form is not displayed. Something went wrong.")
time.sleep(3)
driver.quit()

# **********************************************Using_Excel_Import*********************************************************

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

# *******************************Full code for jetson dashboard*****************************************
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = "https://live23.parkzap.com/parkzap/internal/admin/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(2)

# Find element and send username
driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys("abhishek.sahu@stackfusion.io")
time.sleep(2)

# Find element and send password
driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys("jaj!pr$O8$23AWr@po")
time.sleep(2)

# Click on the login button
driver.find_element(By.XPATH, "//input[@value='Log in']").click()
time.sleep(5)

# Navigate to Jetson devices
driver.find_element(By.XPATH, "//a[normalize-space()='Jetson devices']").click()
time.sleep(3)
Gate_ID_data = [1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943]
Mac_Address = ["48:00:00:00:00", "48:00:00:00:01", "48:00:00:00:02", "48:00:00:00:03", "48:00:00:00:04",
               "48:00:00:00:05",
               "48:00:00:00:06", "48:00:00:00:07", "48:00:00:00:08", "48:00:00:00:09", "48:00:00:00:10"]

Static_IP = ["000.00.00.123", "000.00.00.124", "000.00.00.125", "000.00.00.126", "000.00.00.127", "000.00.00.128",
             "000.00.00.129", "000.00.00.130", "000.00.00.131"]

Static_Subnet = ["255.255.255.0", "255.255.255.0", "255.255.255.0", "255.255.255.0", "255.255.255.0", "255.255.255.0",
                 "255.255.255.0", "255.255.255.0", "255.255.255.0", "255.255.255.0"]
Gateway = ["192.268.1.111", "192.268.1.112", "192.268.1.113", "192.268.1.114", "192.268.1.115", "192.268.1.116"]
DNS1 = ["1.1.1.1"]
DNS2 = ["8.8.8.8"]

# Loop through Gate_ID_data, Mac_Address, Static_IP, Static_Subnet, DNS1, and DNS2
for i in range(len(Gate_ID_data)):
    try:
        # Click on the gate ID
        xpath_gate_id = f"//a[normalize-space()='{Gate_ID_data[i]}']"
        element_gate_id = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_gate_id)))
        element_gate_id.click()
        time.sleep(3)

        # Fill in Mac Address
        xpath_mac_address = "//input[@id='id_mac_address']"
        element_mac_address = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_mac_address)))
        element_mac_address.clear()
        element_mac_address.send_keys(Mac_Address[i])

        # Fill in Static IP
        xpath_static_ip = "//input[@id='id_ethernet_jetson_static_ip_address']"
        element_static_ip = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_static_ip)))
        element_static_ip.clear()
        element_static_ip.send_keys(Static_IP[i])

        # Fill in Static Subnet
        xpath_static_subnet = "//input[@id='id_ethernet_jetson_static_subnet']"
        element_static_subnet = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_static_subnet)))
        element_static_subnet.clear()
        element_static_subnet.send_keys(Static_Subnet[i])

        xpath_Gateway = "//input[@id='id_ethernet_jetson_static_gateway']"
        element_gateway = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_Gateway)))
        element_gateway.clear()
        element_gateway.send_keys(Gateway[i])

        # Fill in DNS1
        xpath_dns1 = "//input[@id='id_ethernet_jetson_static_DNS1']"
        element_dns1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_dns1)))
        element_dns1.clear()
        element_dns1.send_keys(DNS1[0])

        # Fill in DNS2
        xpath_dns2 = "//input[@id='id_ethernet_jetson_static_DNS2']"
        element_dns2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_dns2)))
        element_dns2.clear()
        element_dns2.send_keys(DNS2[0])

        # Save the information
        xpath_save_button = "//input[@name='_save']"  # replace 'save_button_id' with the actual ID or other locator
        element_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_save_button)))
        element_save_button.click()

    except Exception as e:
        print(f"Error processing data at index {i}: {e}")

# Close the browser
driver.quit()

# **************************************Parkbox Dashboard full script***************************************
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = "https://live23.parkzap.com/parkzap/internal/admin/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(2)

# Find element and send username
driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys("abhishek.sahu@stackfusion.io")
time.sleep(2)

# Find element and send password
driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys("jaj!pr$O8$23AWr@po")
time.sleep(2)

# Click on the login button
driver.find_element(By.XPATH, "//input[@value='Log in']").click()
time.sleep(5)

# Navigate to Parkbox devices
driver.find_element(By.XPATH, "//a[normalize-space()='Parkboxs']").click()
time.sleep(3)
Gate_ID_data = [1696, 1695, 1694, 1693, 1692, 1691, 1690, 1689, 1688, 1687, 1686]
Mac_Address = ["48:00:00:00:00", "48:00:00:00:01", "48:00:00:00:02", "48:00:00:00:03", "48:00:00:00:04",
               "48:00:00:00:05",
               "48:00:00:00:06", "48:00:00:00:07", "48:00:00:00:08", "48:00:00:00:09", "48:00:00:00:10"]

Static_IP = ["000.00.00.123", "000.00.00.124", "000.00.00.125", "000.00.00.126", "000.00.00.127", "000.00.00.128",
             "000.00.00.129", "000.00.00.130", "000.00.00.131"]

Static_Subnet = ["255.255.255.0", "255.255.255.0", "255.255.255.0", "255.255.255.0", "255.255.255.0", "255.255.255.0",
                 "255.255.255.0", "255.255.255.0", "255.255.255.0", "255.255.255.0"]
Gateway = ["192.268.1.111", "192.268.1.112", "192.268.1.113", "192.268.1.114", "192.268.1.115", "192.268.1.116"]
DNS1 = ["1.1.1.1"]
DNS2 = ["8.8.8.8"]

# Loop through Gate_ID_data, Mac_Address, Static_IP, Static_Subnet, DNS1, and DNS2
for i in range(len(Gate_ID_data)):
    try:
        # Click on the gate ID
        xpath_gate_id = f"//a[normalize-space()='{Gate_ID_data[i]}']"
        element_gate_id = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_gate_id)))
        element_gate_id.click()
        time.sleep(3)

        # Fill in Mac Address Parkbox
        xpath_mac_address = "//input[@id='id_parkbox_mac_address']"
        element_mac_address = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_mac_address)))
        element_mac_address.clear()
        element_mac_address.send_keys(Mac_Address[i])

        # Fill in Static IP parkbox
        xpath_static_ip = "//input[@id='id_ethernet_static_parkbox_ip_address']"
        element_static_ip = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_static_ip)))
        element_static_ip.clear()
        element_static_ip.send_keys(Static_IP[i])

        # Fill in Static Subnet
        xpath_static_subnet = "//input[@id='id_ethernet_static_subnet']"
        element_static_subnet = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_static_subnet)))
        element_static_subnet.clear()
        element_static_subnet.send_keys(Static_Subnet[i])

        xpath_Gateway = "//input[@id='id_ethernet_static_gateway']"
        element_gateway = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_Gateway)))
        element_gateway.clear()
        element_gateway.send_keys(Gateway[i])

        # Fill in DNS1
        xpath_dns1 = "//input[@id='id_ethernet_static_DNS1']"
        element_dns1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_dns1)))
        element_dns1.clear()
        element_dns1.send_keys(DNS1[0])

        # Fill in DNS2
        xpath_dns2 = "//input[@id='id_ethernet_static_DNS2']"
        element_dns2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_dns2)))
        element_dns2.clear()
        element_dns2.send_keys(DNS2[0])

        # Save the information
        xpath_save_button = "//input[@name='_save']"  # replace 'save_button_id' with the actual ID or other locator
        element_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_save_button)))
        element_save_button.click()

    except Exception as e:
        print(f"Error processing data at index {i}: {e}")

# Close the browser
driver.quit()
