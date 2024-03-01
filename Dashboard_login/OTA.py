import paho.mqtt.client as mqtt
import json
import time

# Topic
PARKBOX_TOPIC = '_parkbox'
gate_id_for_topic = 69
# Topic
topic = str(gate_id_for_topic) + PARKBOX_TOPIC


# Callback function for on_connect event
def on_connect(client, userdata, flags, rc):
    # Define the message to be sent
    ota_message = {
        "sender_mac_add": "11:11:11:11:11:11",
        "receiver_mac": "00:00:00:00:00:00",
        "message_type_code": 8014,
        "message_body": {
            "hw_version": '1',
            "firmware_path": "https://live23.parkzap.com/media/pb_generic/183_4f35648_Parkbox-v1.bin"
        }
    }
    # Convert the message to a JSON string
    ota_message_json = json.dumps(ota_message)
    if rc == 0:  # 0 means mqqt is successfully connected
        print(f"Connected to MQTT broker with result code {rc}")
        # Subscribe to the dynamic topic for OTA updates
        client.subscribe(topic)
        # Publish the OTA message
        client.publish(topic, payload=ota_message_json, qos=1)  # qos can be 0, 1, or 2
    else:
        print(f"Connection failed with result code {rc}")


# Callback function for on_publish event
def on_publish(client, userdata, mid):
    print(f"Message published with mid: {mid}")


# global response
def on_message(client, userdata, msg):
    # received_message = msg.payload.decode()
    # message = json.loads(received_message)
    # print(message)
    try:
        response = json.loads(msg.payload)
        print()
        print()
        print(response)
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error processing message: {e}")
    # print(f"Received response from {device_id} with status: {status}")


# Usage of the MQTT client
def setup_and_run_mqtt_client(mqtt_broker, mqtt_port, timeout=200):
    # list for unreachable jetsons
    unreachable_device = []
    # Usage of the MQTT client
    client = mqtt.Client()
    # Set the on_connect, on_publish, and on_message callback functions
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_message = on_message
    try:
        # Connect to the MQTT broker
        client.connect(mqtt_broker, mqtt_port, 60)
    except OSError as e:
        print(f"Error connecting to MQTT broker: {e}")
        # print("host is unreachable or anything else")
        return
    # Start the MQTT loop
    try:
        client.loop_start()
        # Keep the script running for a while to allow the client to publish the message
        client.loop(timeout=timeout)
        print()
        # Delay for additional time (e.g., 59 seconds)
        time.sleep(59)
        print()
    except AttributeError as e:
        print(f"AttributeError during MQTT loop: {e}")
    except Exception as e:
        print(f"Unhandled exception during MQTT loop: {e}")
    finally:
        # Stop the MQTT loop when done
        client.loop_stop()


# Replace 'mqtt_broker' and 'mqtt_port' with your MQTT broker details
mqtt_broker = "172.27.0.107"
mqtt_port = 8883
# Call the function with the specified MQTT broker details
setup_and_run_mqtt_client(mqtt_broker, mqtt_port)
