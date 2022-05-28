import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client("pub")
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)
# print("done")
# send a message to the raspberry/topic every 1 second, 5 times in a row
for i in range(10):
    # the four parameters are topic, sending content, QoS and whether retaining the message respectively
    client.publish('M2MQTT_Unity/test', payload=i, qos=0, retain=False)
    print(f"send {i} to M2MQTT_Unity/test")
    time.sleep(1)

client.loop_forever()

