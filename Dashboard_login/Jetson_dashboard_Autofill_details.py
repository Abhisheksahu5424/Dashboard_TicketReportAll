from constants import *

# def run_test():
#     # Your Selenium test script here
#     driver = webdriver.Chrome()
#     # Add your test steps
#     # Example: driver.get("https://google.com")
#     # Don't forget to close the browser at the end: driver.quit()
#
# # Schedule the test to run every day at a specific time
# schedule.every().day.at("12:00").do(run_test)
#
# while True:1696
#     schedule.run_pending()
#     time.sleep(1)

def login(driver, username, password):
    url = "https://live23.parkzap.com/parkzap/internal/admin/"
    driver.get(url)
    driver.maximize_window()

    # Find element and send username
    driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys(username)

    # Find element and send password
    driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys(password)

    # Click on the login button on Dashboard
    driver.find_element(By.XPATH, "//input[@value='Log in']").click()


# Example usage
driver = webdriver.Chrome()
login(driver, "abhishek.sahu@stackfusion.io", "jaj!pr$O8$23AWr@po")
time.sleep(10)
# Navigate to Jetson device
driver.find_element(By.XPATH, "//a[normalize-space()='Jetson devices']").click()

# Gate ID which need to be selected to enter in correct gate
# Gate_ID_data = [1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943]
#
# # Mac address of that same site
# Mac_Address = ["48:00:00:00:00", "48:00:00:00:01", "48:00:00:00:02", "48:00:00:00:03", "48:00:00:00:04",
#                "48:00:00:00:05", "48:00:00:00:06", "48:00:00:00:07", "48:00:00:00:08", "48:00:00:00:09",
#                "48:00:00:00:10"]
#
# # Static IP which we need to incert in all field
# Static_IP = ["000.00.00.123", "000.00.00.124", "000.00.00.125", "000.00.00.126", "000.00.00.127", "000.00.00.128",
#              "000.00.00.129", "000.00.00.130", "000.00.00.131"]
#
# # Subnet1696
# Static_Subnet = ["255.255.255.0"] * 10
# Gateway = ["192.268.1.111", "192.268.1.112", "192.268.1.113", "192.268.1.114", "192.268.1.115", "192.268.1.116"]
# DNS1 = ["1.1.1.1"]
# DNS2 = ["8.8.8.8"]
#
# Loop through Gate_ID_data, Mac_Address, Static_IP, Static_Subnet, DNS1, and DNS2
for i, gate_id in enumerate(Gate_ID_data):
    try:
        # Click on the gate ID
        xpath_gate_id = f"//a[normalize-space()='{gate_id}']"
        element_gate_id = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_gate_id)))
        element_gate_id.click()

        # Fill the related details
        fields = ['id_mac_address', 'id_ethernet_jetson_static_ip_address', 'id_ethernet_jetson_static_subnet',
                  'id_ethernet_jetson_static_gateway', 'id_ethernet_jetson_static_DNS1',
                  'id_ethernet_jetson_static_DNS2']
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
