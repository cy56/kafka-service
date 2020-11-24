from kafka import KafkaConsumer
consumer = KafkaConsumer('my-topic-test', bootstrap_servers=['localhost:9092'])
for message in consumer:
    print (message)