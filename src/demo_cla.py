import paho.mqtt.client as mqtt
import time
import threading

# MQTT代理的地址和端口
broker_address = "test.mosquitto.org"  # 这是一个公共的MQTT代理
broker_port = 1883

# 主题
topic = "python/mqtt"

# 回调函数 - 当客户端收到CONNACK响应时调用
def on_connect(*lst):
    print('on_connect', lst)
    
    client=lst[0]
    # 订阅主题
    client.subscribe(topic)

# 回调函数 - 当收到消息时调用
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

# 创建发布者函数
def publisher():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(broker_address, broker_port, 60)
    
    for i in range(5):
        message = f"Hello from Python! Message {i}"
        client.publish(topic, message)
        print(f"Published: {message}")
        time.sleep(1)
    
    client.disconnect()

# 创建订阅者函数
def subscriber():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(broker_address, broker_port, 60)
    
    # 保持连接打开并处理消息
    client.loop_forever()

# 创建并启动线程
sub_thread = threading.Thread(target=subscriber)
sub_thread.start()

# 等待一段时间，确保订阅者已经连接
time.sleep(2)

# 运行发布者
publisher()

# 等待订阅者接收所有消息
time.sleep(2)