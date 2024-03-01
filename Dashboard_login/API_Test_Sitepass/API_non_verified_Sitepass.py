# import csv
#
# import requests
#
# sitepass_status = ["non_verified", "not_allowed_gate", "active", "not_active", "is_inside", "blacklist",
#                    "is_clone_inside"]
#
# for data in sitepass_status:
#     url = f"https://live23.parkzap.com/device/parkbox/pass/{data}/list/"
#
#     print("Site name is : Escala OUT01")
#     request_payload = {
#         "mac_address": "b0:b2:1c:90:fb:c7",
#         "pass_id_type": [
#             "epcid"
#         ],
#         "type": [
#             "rfid",
#             "vehicle",
#             "uhf",
#             "nfc",
#             "ticket",
#             "day-pass",
#             "fastag"
#         ]
#     }
#
#     try:
#         response = requests.post(url, json=request_payload)
#
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Process the response data as needed
#             response_data = response.json()
#             print(f"Successful response for {data}: {response_data}")
#             csv_file_path = "response_data.csv"
#             with open(csv_file_path, mode='a', newline='') as csv_file:
#                 csv_writer = csv.writer(csv_file)
#                 csv_writer.writerow(response_data)
#
#             print(f"Response data exported to {csv_file_path}")
#
#         else:
#             # Handle unsuccessful response
#             print(f"Unsuccessful response for {data}. Status code: {response.status_code}")
#
#     except requests.exceptions.RequestException as e:
#         # Handle exceptions during the request
#         print(f"An error occurred while making the request for {data}: {e}")


# import csv
# import requests
#
# sitepass_status = ["non_verified", "not_allowed_gate", "active", "not_active", "is_inside", "blacklist",
#                    "is_clone_inside"]
#
# # Set to store unique responses
# unique_responses = []
#
# for data in sitepass_status:
#     url = f"https://live23.parkzap.com/device/parkbox/pass/{data}/list/"
#
#     print("Site name is : Escala OUT01")
#     request_payload = {
#         "mac_address": "b0:b2:1c:90:fb:c7",
#         "pass_id_type": [
#             "epcid"
#         ],
#         "type": [
#             "rfid",
#             "vehicle",
#             "uhf",
#             "nfc",
#             "ticket",
#             "day-pass",
#             "fastag"
#         ]
#     }
#
#     try:
#         response = requests.post(url, json=request_payload)
#
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Process the response data as needed
#             response_data_list = response.json()
#             count = 0
#
#             for response_data in response_data_list:
#                 response_list = list(response_data.items())
#
#                 # Check if the response is unique
#                 if response_list not in unique_responses:
#                     unique_responses.append(response_list)
#
#                     print(f"Successful response for {data}: {response_data}")
#                     csv_file_path = "response_data.csv"
#                     with open(csv_file_path, mode='a', newline='') as csv_file:
#                         csv_writer = csv.writer(csv_file)
#                         csv_writer.writerow(response_data.values())
#
#                     print(f"Response data exported to {csv_file_path}")
#                 else:
#                     count += 1
#                     print(f"Duplicate response for {data}. Skipping. and the count: {count}")
#         else:
#             # Handle unsuccessful response
#             print(f"Unsuccessful response for {data}. Status code: {response.status_code}")
#
#     except requests.exceptions.RequestException as e:
#         # Handle exceptions during the request
#         print(f"An error occurred while making the request for {data}: {e}")

import csv
import requests

sitepass_status = ["non_verified", "not_allowed_gate", "active", "not_active", "is_inside", "blacklist", "is_clone_inside"]

# Set to store unique responses
unique_responses = []

allowed_transitions = {
    "non_verified": ["non_verified"],
    "not_allowed_gate": ["not_allowed_gate"],
    "active": ["active", "is_inside", "is_clone_inside"],
    "not_active": ["not_active", "is_inside", "is_clone_inside"],
    "is_inside": ["is_inside", "is_clone_inside"],
    "blacklist": ["blacklist"],
    "is_clone_inside": ["is_clone_inside", "is_inside"]
}

for data in sitepass_status:
    url = f"https://live23.parkzap.com/device/parkbox/pass/{data}/list/"

    print("Site name is : Escala OUT01")
    request_payload = {
        "mac_address": "b0:b2:1c:90:fb:c7",
        "pass_id_type": [
            "epcid"
        ],
        "type": [
            "rfid",
            "vehicle",
            "uhf",
            "nfc",
            "ticket",
            "day-pass",
            "fastag"
        ]
    }

    try:
        response = requests.post(url, json=request_payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Process the response data as needed
            response_data_list = response.json()
            count = 0

            for response_data in response_data_list:
                response_list = list(response_data.items())

                # Check if the response is unique
                if response_list not in unique_responses:
                    current_status = data
                    if all(new_status in allowed_transitions[current_status] for new_status in response_data.get("status", [])):
                        unique_responses.append(response_list)

                        print(f"Successful response for {data}: {response_data}")
                        csv_file_path = "response_data.csv"
                        with open(csv_file_path, mode='a', newline='') as csv_file:
                            csv_writer = csv.writer(csv_file)
                            csv_writer.writerow(response_data.values())

                        print(f"Response data exported to {csv_file_path}")
                    else:
                        count += 1
                        print(f"Invalid transition in response for {data}. Skipping. Count: {count}")
                else:
                    count += 1
                    print(f"Duplicate response for {data}. Skipping. Count: {count}")
        else:
            # Handle unsuccessful response
            print(f"Unsuccessful response for {data}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle exceptions during the request
        print(f"An error occurred while making the request for {data}: {e}")
