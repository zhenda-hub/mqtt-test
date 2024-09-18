from .my_mqtt import get_client, send_msg, clean_client


if __name__ == '__main__':
    broker = 'broker.hivemq.com'
    # broker = 'iot.mqtt.cn'  # bug
    port = 1883
    topics = ["test/topic", "test/topic1", "test/topic2"]
    auth = {'username': "hahaha", 'password': '666666'}
    
    cl = get_client(broker, auth=auth)
    for i in range(6, 0, -1):
        send_msg(cl, topics, f'msgggg  {i}')
    
    clean_client(cl)
    