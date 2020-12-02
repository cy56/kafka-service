import sqlalchemy as db

def get_engine():
    engine = db.create_engine('mysql+pymysql://root:root@127.0.0.1:3306/yippi_sns')
    return engine