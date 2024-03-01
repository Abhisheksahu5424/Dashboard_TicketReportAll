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

# Login
driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys("abhishek.sahu@stackfusion.io")
driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys("jaj!pr$O8$23AWr@po")
driver.find_element(By.XPATH, "//input[@value='Log in']").click()
time.sleep(5)

# Navigate to Parkbox devices
driver.find_element(By.XPATH, "//a[normalize-space()='Parkboxs']").click()
time.sleep(3)

Gate_ID_data = [1696, 1695, 1694, 1693, 1692, 1691, 1690, 1689, 1688, 1687, 1686]
Mac_Address = ["48:00:00:00:00", "48:00:00:00:01", "48:00:00:00:02", "48:00:00:00:03", "48:00:00:00:04",
               "48:00:00:00:05", "48:00:00:00:06", "48:00:00:00:07", "48:00:00:00:08", "48:00:00:00:09", "48:00:00:00:10"]
Static_IP = ["000.00.00.123", "000.00.00.124", "000.00.00.125", "000.00.00.126", "000.00.00.127", "000.00.00.128",
             "000.00.00.129", "000.00.00.130", "000.00.00.131"]
Static_Subnet = ["255.255.255.0"] * 10
Gateway = ["192.268.1.111", "192.268.1.112", "192.268.1.113", "192.268.1.114", "192.268.1.115", "192.268.1.116"]
DNS1 = ["1.1.1.1"]
DNS2 = ["8.8.8.8"]

# Loop through Parkbox data


for i, gate_id in enumerate(Gate_ID_data):
    try:
        # Click on the gate ID
        xpath_gate_id = f"//a[normalize-space()='{gate_id}']"
        element_gate_id = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_gate_id)))
        element_gate_id.click()
        time.sleep(3)

        # Fill in Parkbox details
        fields = ['id_parkbox_mac_address', 'id_ethernet_static_parkbox_ip_address', 'id_ethernet_static_subnet',
                  'id_ethernet_static_gateway', 'id_ethernet_static_DNS1', 'id_ethernet_static_DNS2']
        values = [Mac_Address[i], Static_IP[i], Static_Subnet[i], Gateway[i], DNS1[0], DNS2[0]]

        for field, value in zip(fields, values):
            xpath_field = f"//input[@id='{field}']"
            element_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_field)))
            element_field.clear()
            element_field.send_keys(value)

        # Save the information
        xpath_save_button = "//input[@name='_save']"
        element_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_save_button)))
        element_save_button.click()

    except Exception as e:
        print(f"Error processing data at index {i}: {e}")

# Close the browser
driver.quit()
