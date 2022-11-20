import os
import connection
import sqlparse
import pandas as pd

if __name__ == '__main__':
    print('[INFO] Service ETL is Starting...')
    conf = connection.config('postgres')
    conn, engine = connection.psql_conn(conf)
    cursor = conn.cursor()

    conf_dwh = connection.config('dwh')
    conn_dwh, engine_dwh = connection.psql_conn(conf)
    cursor_dwh = conn_dwh.cursor()

    path_query = os.getcwd()+'/query/'
    query = sqlparse.format(
        open(
            path_query+'query.sql','r'
        ).read(), strip_comments=True
    ).strip()
    print(query)

    try:
        # get data
        print('[INFO] Service ETL is Starting...')
        df = pd.read_sql(query, engine)
        print(df)

    except Exception as e:
        print('[INFO] Service ETL is failed')

