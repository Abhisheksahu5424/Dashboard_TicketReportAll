import time

from selenium.webdriver.chrome import webdriver

from Dashboard_login.Login_Functionality.Jetson_Login import login_jetson
from Dashboard_login.constants import *
from constants import *
from Dashboard_login.utils import configure_gate_data

if __name__ == "__main__":
    driver = webdriver.Chrome()
    result = login_jetson(driver, USERNAME, PASSWORD)
    time.sleep(5)

    if result:
        print("Login Successful!")
    else:
        print("Login Fail!")

    driver = webdriver.Chrome()
    result = configure_gate_data(driver, Gate_ID_data, Mac_Address, Static_IP, Static_Subnet, Gateway, DNS1, DNS2)
    time.sleep(2)
    if result:
        print("Data Filled Successfully")
    else:
        print("Data Filling Failed")




