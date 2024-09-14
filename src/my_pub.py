from .my_mqtt import get_client, send_msg, clean_client


if __name__ == '__main__':
    broker = 'broker.hivemq.com'
    # broker = 'iot.mqtt.cn'  # bug
    port = 1883
    topics = ["test/topic", "test/topic1", "test/topic2"]
    
    cl = get_client(broker)
    for i in range(10):
        send_msg(cl, topics, f'msgggg  {i}')
    
    clean_client(cl)
    