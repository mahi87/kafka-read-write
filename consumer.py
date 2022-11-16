from kafka import KafkaConsumer
import threading

def _read_messages():
    consumer = KafkaConsumer('test-topic', group_id = 'test-group', bootstrap_servers=['localhost:9092'])
    for message in consumer:
        print(message.value.decode('utf-8'))
        
def read_messages():    
    t = threading.Thread(target=_read_messages, args=())
    t.start()
    print('reading messages now')
    