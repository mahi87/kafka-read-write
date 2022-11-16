from kafka import KafkaConsumer
import threading
import app

def _read_messages():
    topic = app.app.config['KAFKA_TOPIC']
    group_id = app.app.config['KAFKA_GROUP']
    bootstrap_servers = app.app.config['KAFKA_BOOTSTRAP_SERVER']
    consumer = KafkaConsumer(topic, group_id = group_id, bootstrap_servers=bootstrap_servers)
    for message in consumer:
        print(message.value.decode('utf-8'))
        
def read_messages():    
    t = threading.Thread(target=_read_messages, args=())
    t.start()
    print('reading messages now')
    