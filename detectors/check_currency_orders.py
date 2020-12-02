from services import mysql
from services import producer

import pandas as pd
import json

def handle(raw_data):
    data = json.loads(raw_data.get('body'))
    if data.get('owner_id'):
        owner_id = data.get('owner_id')
        sub = get_sub_orders(owner_id)._get_value(0, 'amount')
        add = get_add_orders(owner_id)._get_value(0, 'amount')
        currency = get_currency(owner_id)._get_value(0, 'amount')
        diff = add - sub
        if (diff != currency):
            print('found not tally issue')
            send_notification(owner_id)
            create_record()

def get_sub_orders(owner_id):
    query = """
        SELECT sum(amount) as amount
        FROM currency_orders
        WHERE owner_id = {} AND type = -1 AND currency = 1;
    """

    query = query.format(owner_id)

    df = pd.read_sql(query, mysql.get_engine())

    df = df.fillna(0)

    return df

def get_add_orders(owner_id):
    query = """
        SELECT sum(amount) as amount
        FROM currency_orders
        WHERE owner_id = {} AND type = 1 AND currency = 1;
    """

    query = query.format(owner_id)

    df = pd.read_sql(query, mysql.get_engine())

    df = df.fillna(0)

    return df

def get_currency(owner_id):
    query = """
        SELECT sum as amount
        FROM currencies 
        WHERE owner_id = {} AND type = 1;
    """

    query = query.format(owner_id)

    df = pd.read_sql(query, mysql.get_engine())

    df = df.fillna(0)

    return df

def create_record(dict={}):
    pass

def send_notification(owner_id):
    # topic = 'currency_order_notifications'
    topic = 'my-app-notification'
    message = {
        'key': owner_id,
        'message': 'user_id: {} not tally !!!'.format(owner_id)
    }

    print('sent notification')
    producer.produce(topic, message)