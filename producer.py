from kafka import KafkaProducer

bootstrap_servers = ['localhost:9092']
topicName = 'my-topic-test'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

producer.send(topicName, b'finally gaodim you liao !!!! ')
producer.flush()