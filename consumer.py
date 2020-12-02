import sys
import json
from kafka import KafkaConsumer
from detectors import check_currency_orders

detector_lists = {
    # 'currency_orders_balance': check_currency_orders
    'my-app-test': check_currency_orders
}

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], value_deserializer=lambda m: json.loads(m.decode('ascii')), key_deserializer=lambda m: json.loads(m.decode('ascii')))
consumer.subscribe(['currency_orders_balance', 'my-app-test'])

def default_handle(data=None):
    print('nothing to do...')
    return False

if __name__ == "__main__":
    try:
        for message in consumer:
            handler = detector_lists.get(message.topic, default_handle)
            if handler is not False:
                handler.handle(message.value)

    except KeyboardInterrupt:
        sys.exit()