from kafka import KafkaProducer
import json

def produce(topic, data):
    bootstrap_servers = ['localhost:9092']

    producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

    value = json.dumps(data).encode('utf-8')

    producer.send(topic, value)
    producer.flush()