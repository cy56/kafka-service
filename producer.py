from kafka import KafkaProducer

bootstrap_servers = ['localhost:9092']
topicName = 'my-topic-one'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

producer.send(topicName, b'bye liao !!!! ')
producer.flush()