import logging
import time
import uuid

import paho.mqtt.client as mqtt
import paho.mqtt.enums as MQTTErrorCode


def on_connect(*lst):
    print('on_connect', lst)
    rc = lst[3]
    if rc == 0:
        print("Connected to MQTT Broker ok!")
    else:
        print(f"Connected to MQTT Broker Failed! return code {rc}")
    
def on_disconnect(*lst):
    print('on_disconnect', lst)
    rc = lst[-1]
    if rc == 0:
        print("Disconnected to MQTT Broker ok!")
    else:
        print(f"Disconnected to MQTT Broker Failed! return code {rc}")
    
def on_subscribe(*lst):
    print('on_subscribe', lst)
    
def on_unsubscribe(*lst):
    print('on_unsubscribe', lst)

def on_message(*lst):
    # print('on_message', lst)
    
    userdata = lst[1]
    msg : mqtt.MQTTMessage = lst[-1]
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    
    if msg.topic not in userdata:
        userdata[msg.topic] = [msg.payload.decode()]
    else:
        userdata[msg.topic].append(msg.payload.decode())
        
    # breakpoint()
    
def on_publish(*lst):
    print('on_publish', lst)
    count = lst[-1]
    print(f'send msg num: {count}')
    # breakpoint()
    
def on_log(*lst):
    print('on_log', lst)
    # print(lst[-1])
    
    
def get_client(hostname, auth = None, client_id = "") -> mqtt.Client:
    
    client = mqtt.Client(client_id=client_id)
    
    # client.enable_logger()
    
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    # client.on_subscribe = on_subscribe
    # client.on_unsubscribe = on_unsubscribe
    client.on_message = on_message
    # client.on_publish = on_publish
    # client.on_log = on_log
    
    
    # TODO:
    if auth:
        ...
        
    client.connect(hostname)
    
    # time.sleep(5)
    
    return client


def clean_client(client: mqtt.Client):
    print('clean_client!!!!!!!!!!!!!!!!!!!!!')
    client.disconnect()
    client.loop_stop()
    
    
def send_msg(client: mqtt.Client, topics, msg):
    client.loop_start()
    
    for t in topics:
        
        res: mqtt.MQTTMessage = client.publish(t, msg, qos=2, retain=True)
        # MQTTErrorCode
        # breakpoint()
        # status = res[0]
        status = res.rc
        if status == 0:
            print(f"Send `{msg}` to topic `{t}`")
        else:
            print(f"Failed to send message to topic {t}, {status}")
        time.sleep(0.2)  # 很关键!!! TODO: why
    
    
def get_msg(client: mqtt.Client, topics, wait_time: int = 30):
    client.loop_start()
    
    client.user_data_set({})
    for t in topics:
        client.subscribe(t, qos=2)
        
    time.sleep(wait_time)
    
    clean_client(client)
    
    return client.user_data_get()
    