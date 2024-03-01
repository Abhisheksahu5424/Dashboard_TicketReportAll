from Dashboard_login.Login_Functionality.Jetson_Login import login_jetson
from Dashboard_login.constants import *


def configure_gate_data(driver, gate_ID_data, mac_addresses, static_ips, gateways, dns1, dns2):
    try:
        # Loop through Gate_ID_data, Mac_Address, Static_IP, Static_Subnet, DNS1, and DNS2
        for i, gate_id in enumerate(gate_ID_data):
            # Click on the gate ID
            xpath_gate_id = f"//a[normalize-space()='{gate_id}']"
            element_gate_id = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_gate_id)))
            element_gate_id.click()

            # Fill the related details
            fields = ['id_mac_address', 'id_ethernet_jetson_static_ip_address', 'id_ethernet_jetson_static_subnet',
                      'id_ethernet_jetson_static_gateway', 'id_ethernet_jetson_static_DNS1',
                      'id_ethernet_jetson_static_DNS2']
            values = [mac_addresses[i], static_ips[i], "255.255.255.0", gateways[i], dns1[0], dns2[0]]

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

    finally:
        # Close the browser
        driver.quit()


# Example usage:
driver = webdriver.Chrome()  # or any other browser of your choice

Gate_ID_data = [1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943]
Mac_Address = ["48:00:00:00:00", "48:00:00:00:01", "48:00:00:00:02", "48:00:00:00:03", "48:00:00:00:04",
               "48:00:00:00:05", "48:00:00:00:06", "48:00:00:00:07", "48:00:00:00:08", "48:00:00:00:09",
               "48:00:00:00:10"]
Static_IP = ["000.00.00.123", "000.00.00.124", "000.00.00.125", "000.00.00.126", "000.00.00.127", "000.00.00.128",
             "000.00.00.129", "000.00.00.130", "000.00.00.131"]
Gateway = ["192.268.1.111", "192.268.1.112", "192.268.1.113", "192.268.1.114", "192.268.1.115", "192.268.1.116"]
DNS1 = ["1.1.1.1"]
DNS2 = ["8.8.8.8"]

configure_gate_data(driver, Gate_ID_data, Mac_Address, Static_IP, Gateway, DNS1, DNS2)
