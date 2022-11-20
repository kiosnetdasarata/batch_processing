import json
import os

import psycopg2
from sqlalchemy import create_engine

def config(connection_db):
    path = os.getcwd()
    with open(path + '\\' + 'config.json') as file:
        conf = json.load(file)[connection_db]
    return conf

def psql_conn(conf):
    try:
        conn = psycopg2.connect(
            host=conf['host'],
            database=conf['db'],
            user=conf['user'],
            password=conf['password'],
            port=conf['port']
        )
        print('[INFO] Success connect PostgreSQL')
        engine = create_engine(
            f"postgres+psycopg2://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['db']}")
        return conn, engine
    except Exception as e:
        print("[INFO] Can't connect PostgreSQL")
        print(str(e))

