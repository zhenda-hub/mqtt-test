import logging
from pydoc_data import topics
import time
import uuid
import threading
import concurrent.futures

import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
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
    # print('on_publish', lst)
    mid = lst[-1]
    print(f'send msg id: {mid} ok!' )
    # breakpoint()
    
def on_log(*lst):
    print('on_log', lst)
    # print(lst[-1])
    
    
def get_client(hostname, auth = None, client_id = "") -> mqtt.Client:
    
    if client_id:
        client = mqtt.Client(client_id=client_id, clean_session=False)
    else:
        client = mqtt.Client(client_id=client_id)
    
    client.enable_logger()
    
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    # client.on_subscribe = on_subscribe
    # client.on_unsubscribe = on_unsubscribe
    client.on_message = on_message
    client.on_publish = on_publish
    # client.on_log = on_log
    
    if not auth:
        auth = {}
    if auth:
        username = auth.get('username')
        if username:
            password = auth.get('password')
            client.username_pw_set(username, password)
        else:
            raise KeyError("The 'username' key was not found, this is "
                           "required for auth")

        
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
        
        # 异步publish
        # res: mqtt.MQTTMessage = client.publish(t, msg, qos=2, retain=True)
        res: mqtt.MQTTMessage = client.publish(t, msg, qos=2)
        # MQTTErrorCode
        # breakpoint()
        # status = res[0]
        rc = res.rc
        if rc == 0:
            print(f"Send `{msg}` to topic `{t}`, id `{res.mid}`")
        else:
            print(f"Failed to send message to topic {t}, {rc}")
            
        # qos=2 需要等待, 确认broker消息. 很关键!!!
        # 同步等待
        if not res.is_published():
            res.wait_for_publish()
    
def get_msg(client: mqtt.Client, topics, wait_time: int = 30):
    client.loop_start()
    
    client.user_data_set({})
    for t in topics:
        client.subscribe(t, qos=2)
        
    time.sleep(wait_time)
    
    clean_client(client)
    
    return client.user_data_get()
    
    
def get_msg2(hostname, topics, msg_count, timeout=30):
    
    errors = []
    result = []
    # 创建一个线程池执行器
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 启动后台任务
        future = executor.submit(subscribe.simple, topics=topics, hostname=hostname, msg_count=msg_count, qos=2)
        print('end')
        try:
            # 等待最多30秒
            result = future.result(timeout=timeout)
            print(f"任务结果: {result}")
        except concurrent.futures.TimeoutError as e:
            errors.append(e)
        except Exception as e:
            errors.append(e)
    return result, errors

    # res = subscribe.simple(topics=topics, hostname=hostname, msg_count=msg_count, qos=2)
    # return [(i.topic, i.payload) for i in res]
