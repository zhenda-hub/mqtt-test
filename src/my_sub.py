from src.my_mqtt import get_client, get_msg
import pprint
import uuid


if __name__ == '__main__':
    broker = 'broker.hivemq.com'
    # broker = 'iot.mqtt.cn'  # bug
    port = 1883
    topics = ["test/topic", "test/topic1", "test/topic2"]
    auth = {'username': "hahaha", 'password': '666666'}
    
    cl = get_client(
        broker,
        # auth=auth,
        client_id=str(uuid.getnode()),
    )
    msg = get_msg(cl, topics)
    pprint.pprint(msg)
        