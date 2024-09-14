import paho.mqtt.client as mqtt
import time
import uuid

# MQTT Broker信息
# broker = 'test.mosquitto.org'
# broker = 'mqtt.eclipseprojects.io'
broker = 'broker.hivemq.com'
# broker = 'iot.mqtt.cn'  # bug
port = 1883
topic = "test/topic"

# 连接MQTT Broker
# mqtt.CallbackAPIVersion.VERSION2
# client = mqtt.Client(client_id=str(uuid.getnode()), clean_session=False)
# TODO: uuid
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=str(uuid.getnode()), clean_session=False)
client.connect(broker, port, 60)




# 定义连接回调函数
# def on_connect(client, userdata, flags, rc, properties):
def on_connect(*lst):
    # breakpoint()
    if lst[3] == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic, qos=2)
    else:
        print(f"Failed to connect, return code {lst[3]}")

# 定义消息回调函数
def on_message(client, userdata, msg):
    userdata.append(msg.payload)  # save data
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

client.on_connect = on_connect
client.on_message = on_message

# client.loop_forever()

client.user_data_set([])

client.loop_start()
print('st')
time.sleep(5)
print('se')
client.disconnect()
client.loop_stop()

res_list = client.user_data_get()
print('res_list', res_list)
