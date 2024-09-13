import paho.mqtt.client as mqtt
import time

# MQTT Broker信息
# broker = 'test.mosquitto.org'
# broker = 'mqtt.eclipseprojects.io'
broker = 'broker.hivemq.com'
# broker = 'iot.mqtt.cn'  # bug
port = 1883
topic = "test/topic"

# 连接MQTT Broker
# client = mqtt.Client()
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker, port, 60)

# client.loop_start()


# 发布消息
def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        print('result', result)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

# publish(client)

for msg_count in range(10):
    time.sleep(0.2)
    msg = f"messages: {msg_count}"
    result = client.publish(topic, msg, qos=2, retain=True)
    print('result', result)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
        
# client.disconnect()
# client.loop_stop()
