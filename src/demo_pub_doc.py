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
client.loop_start()


def on_publish(*lst):
    # breakpoint()
    print('on_publish', lst)
    # print("mid: " + str(mid))
    
client.on_publish = on_publish


    
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
        
print('dis!!!!!!!!!!!!!!!!!!!')
client.disconnect() # 断开和broker的连接
client.loop_stop()
