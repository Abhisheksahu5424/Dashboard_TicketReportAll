# #
# # import time
# # from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
# # from webdriver_manager.chrome import ChromeDriverManager
# #
# # url = "https://reports.parkzap.com/login"
# # driver = webdriver.Chrome()
# # driver.get(url)
# # driver.maximize_window()
# # time.sleep(2)
# #
# # # Find element and send username
# # driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("abhishek.sahu@stackfusion.io")
# # time.sleep(2)
# #
# # # Find element and send password
# # driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Harrypotter@2023")
# # time.sleep(2)
# #
# # # Click on the login button
# # driver.find_element(By.XPATH, "//button[@name='method']").click()
# # time.sleep(5)
# # # #
# # # # # Navigate to Jetson devices
# # driver.find_element(By.XPATH, "//span[normalize-space()='Day Close Report']").click()
# # # # time.sleep(3)
# # driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/ul[1]/li[1]/div[1]/div[3]/span[1]").click()
# # # # time.sleep(5)
# # driver.find_element(By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']").send_keys("Thiruvananthapuram International Airport T2")
# # driver.find_element(By.XPATH, "//li[@aria-label='Thiruvananthapuram International Airport T2']").click()
# # time.sleep(1)
# # driver.find_element(By.XPATH, "//span[@class='p-button-icon p-c pi pi-calendar']").click()
# # time.sleep(3)
# # driver.find_element(By.XPATH, "//span[@class='p-highlight']").click()
# # time.sleep(1)
# # driver.find_element(By.XPATH, "//span[normalize-space()='Get Report']").click()
# # time.sleep(3)
# #
# # driver.find_element(By.XPATH,"//span[normalize-space()='Export CSV']").click()
# #
# # time.sleep(10)
# # driver.quit()
#
#
# # #
# # # def send_email(receiver_email, subject, body, attachment_path):
# # #     sender_email = "abhishek.sahu@stackfusion.io"  # Replace with your email
# # #     sender_password = "Harrypotter@023"  # Replace with your email password
# # #
# # #     msg = MIMEMultipart()
# # #     msg['From'] = sender_email
# # #     msg['To'] = receiver_email
# # #     msg['Subject'] = subject
# # #     msg.attach(MIMEText(body, 'plain'))
# # #
# # #     # Attach the exported data file
# # #     with open(attachment_path, "rb") as file:
# # #         attach = MIMEApplication(file.read(),_subtype="xlsx")
# # #         attach.add_header('Content-Disposition','attachment',filename=str(file.name))
# # #         msg.attach(attach)
# # #
# # #     # Connect to SMTP server and send email
# # #     with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server details
# # #         server.starttls()
# # #         server.login(sender_email, sender_password)
# # #         server.sendmail(sender_email, receiver_email, msg.as_string())
# # #
# # # # Example usage:
# # # dashboard_username = "abhishek.sahu@stackfusion.io"
# # # dashboard_password = "Harrypotter@2023"
# # # # download_data(dashboard_username, dashboard_password)
# # #
# # # # Example email details:
# # # recipient_email = "ashwin@stackfusion.io"
# # # email_subject = "Data Export"
# # # email_body = "Please find attached the exported data."
# # #
# # # # Provide the path to the exported data file
# # # attachment_file_path = "/home/abhishek/Downloads/Day Close Report.csv"
# # #
# # # # Send the email
# # # send_email(recipient_email, email_subject, email_body, attachment_file_path)
# #
# # import smtplib
# # import time
# # from email.mime.application import MIMEApplication
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# #
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager
# #
# #
# # # Function to download data from the dashboard
# # def download_data(username, password, site_name):
# #     url = "https://skidata.parkzap.com/reports/day-close-report"
# #     driver = webdriver.Chrome(ChromeDriverManager().install())
# #     driver.get(url)
# #     driver.maximize_window()
# #
# #     # Find the username and password fields, and login
# #     driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(username)
# #     time.sleep(2)
# #     driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
# #     time.sleep(2)
# #     driver.find_element(By.XPATH, "//button[@name='method']").click()
# #     time.sleep(5)
# #
# #     # Navigate to Jetson devices and generate the report
# #     driver.find_element(By.XPATH, "//span[normalize-space()='Day Close Report']").click()
# #     time.sleep(3)
# #     driver.find_element(By.XPATH,
# #                         "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/ul[1]/li[1]/div[1]/div[3]/span[1]").click()
# #     time.sleep(5)
# #
# #     # Select the site
# #     driver.find_element(By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']").send_keys(site_name)
# #     time.sleep(1)
# #     driver.find_element(By.XPATH, f"//li[@aria-label='{site_name}']").click()
# #     time.sleep(1)
# #
# #     # Perform other actions to generate the report
# #     # ...
# #
# #     # Export the CSV report
# #     driver.find_element(By.XPATH, "//span[normalize-space()='Export CSV']").click()
# #     time.sleep(10)
# #
# #     driver.quit()
# #
# #
# # def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
# #     msg = MIMEMultipart()
# #     msg['From'] = sender_email
# #     msg['To'] = receiver_email
# #     msg['Subject'] = subject
# #     msg.attach(MIMEText(body, 'plain'))
# #
# #     # Attach the exported data file
# #     with open(attachment_path, "rb") as file:
# #         attach = MIMEApplication(file.read(), _subtype="csv")
# #         attach.add_header('Content-Disposition', 'attachment', filename=str(file.name))
# #         msg.attach(attach)
# #
# #     # Connect to SMTP server and send email
# #     with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server details
# #         server.starttls()
# #         server.login(sender_email, sender_password)
# #         server.sendmail(sender_email, receiver_email, msg.as_string())
# #
# #
# # # Example usage:
# # dashboard_username = "abhishek.sahu@stackfusion.io"
# # dashboard_password = "Harrypotter@2023"
# # site_to_export = "Thiruvananthapuram International Airport T2"
# #
# # # download_data(dashboard_username, dashboard_password, site_to_export)
# #
# # # Email details
# # sender_email = "abhishek.sahu@stackfusion.io"
# # sender_password = "YourEmailPassword"  # Replace with your email password
# # recipient_email = "ashwin@stackfusion.io"
# # email_subject = "Data Export"
# # email_body = "Please find attached the exported data."
# #
# # # Provide the path to the exported data file
# # attachment_file_path = "/home/abhishek/Downloads/Day Close Report.csv"
# #
# # # Send the email
# # send_email(sender_email, sender_password, recipient_email, email_subject, email_body, attachment_file_path)
#
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from webdriver_manager.chrome import ChromeDriverManager
# # import pandas as pd
# #
# # url = "https://skidata.parkzap.com/reports/day-close-report"
# # driver = webdriver.Chrome()
# # driver.get(url)
# # driver.maximize_window()
# # time.sleep(2)
# #
# # # Login
# # driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("abhishek.sahu@stackfusion.io")
# # time.sleep(2)
# # driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Harrypotter@2023")
# # time.sleep(2)
# # driver.find_element(By.XPATH, "//button[@name='method']").click()
# # time.sleep(5)
# #
# # # Navigate to Day Close Report
# # driver.find_element(By.XPATH, "//span[normalize-space()='Day Close Report']").click()
# # driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/ul[1]/li[1]/div[1]/div[3]/span[1]").click()
# # driver.find_element(By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']").send_keys("Thiruvananthapuram International Airport T2")
# # driver.find_element(By.XPATH, "//li[@aria-label='Thiruvananthapuram International Airport T2']").click()
# # time.sleep(1)
# # driver.find_element(By.XPATH, "//span[@class='p-button-icon p-c pi pi-calendar']").click()
# # time.sleep(3)
# # driver.find_element(By.XPATH, "//span[@class='p-highlight']").click()
# # time.sleep(1)
# # driver.find_element(By.XPATH, "//span[normalize-space()='Get Report']").click()
# # time.sleep(3)
# #
# # # Export Day Close Report as CSV
# # driver.find_element(By.XPATH, "//span[normalize-space()='Export CSV']").click()
# # time.sleep(10)
# #
# # # Now you should have the Day Close Report CSV saved on your machine.
# #
# # # Assuming you have the Ticket Report data in an Excel file, you can read it using pandas
# # ticket_report_path = "/home/abhishek/Downloads/Day Close Report.csv"
# # ticket_df = pd.read_excel(ticket_report_path)
# #
# # # Now you can perform the comparison based on your specific logic
# # # For example, you can extract relevant columns from the Day Close Report CSV and compare with the Ticket Report data.
# # # You may need to modify the column names based on your actual data structure.
# # day_close_df = pd.read_csv("/home/abhishek/Downloads/Day Close Report.csv")
# # fastag_amount_day_close = day_close_df['Fastag Amount'].sum()
# # total_amount_day_close = day_close_df['Total Amount'].sum()
# #
# # fastag_amount_ticket_report = ticket_df['Fastag Amount'].sum()
# # total_amount_ticket_report = ticket_df['Total Amount'].sum()
# #
# # # Perform the comparison
# # if fastag_amount_day_close == fastag_amount_ticket_report and total_amount_day_close == total_amount_ticket_report:
# #     print("Day Close Report and Ticket Report match!")
# # else:
# #     print("Day Close Report and Ticket Report do not match!")
# #
# # # Close the browser
# # driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from datetime import datetime, timedelta
# from selenium.webdriver.common.keys import Keys
#
# # Function to get the next day's date in the required format
# def get_next_day_date():
#     today = datetime.now()
#     next_day = today + timedelta(days=1)
#     return next_day.strftime("31-01-2024")  # Modify the format based on your requirement
#
#
# print(get_next_day_date())
#
# url = "https://reports.parkzap.com/"
# driver = webdriver.Chrome()
# driver.get(url)
# driver.maximize_window()
# time.sleep(2)
#
# # Login
# driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("abhishek.sahu@stackfusion.io")
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Harrypotter@2023")
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[@name='method']").click()
# time.sleep(5)
#
# # Navigate to Day Close Report
# driver.find_element(By.XPATH, "//span[normalize-space()='Day Close Report']").click()
# driver.find_element(By.XPATH,
#                     "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/ul[1]/li[1]/div[1]/div[3]/span[1]").click()
#
# # Select Site dynamically (replace "Ahmedabad" with your dynamic site variable)
# site_name = ["Ahmedabad"]
# element_to_hover_over = driver.find_element(By.XPATH, "//span[normalize-space()='Ahmedabad']")
# input_element = driver.find_element(By.XPATH, "//span[normalize-space()='Ahmedabad']")
# input_element.send_keys("Ahmedabad")
# time.sleep(3)
# input_element.send_keys(Keys.ENTER)
# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']").send_keys(site_name)
# time.sleep(3)
# driver.find_element(By.XPATH, f"//li[@aria-label='{site_name}']").click()
#
# # Select Date dynamically
# next_day_date = get_next_day_date()
# driver.find_element(By.XPATH, "//span[@class='p-button-icon p-c pi pi-calendar']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, f"//span[text()='{next_day_date}']").click()
#
# # Get Report
# driver.find_element(By.XPATH, "//span[normalize-space()='Get Report']").click()
# time.sleep(3)
#
# # Export Day Close Report as CSV
# driver.find_element(By.XPATH, "//span[normalize-space()='Export CSV']").click()
# time.sleep(10)
#
# # Close the browser
# driver.quit()
#
