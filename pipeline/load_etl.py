import pandas as pd
import psycopg2
from psycopg2 import sql, extras
from dbinfo import DB_NAME, DB_USER, DB_PW, DB_HOST, DB_PORT

conn = psycopg2.connect(
        dbname = DB_NAME,
        user = DB_USER,
        password = DB_PW,
        host = DB_HOST,
        port = DB_PORT
        )

if not conn:
    raise OperationalError("Database is not found.")
else:
    print("Database Connected Successfully.")

cur = conn.cursor()


def insert_data(df, table_name):
    values = [tuple(row) for row in df.values]

    insert_query = sql.SQL("""
        INSERT INTO {} (name, price) VALUES %s
    """).format(sql.Identifier(table_name))

    extras.execute_values(cur, insert_query, values)
    conn.commit()
    print(f'Inserted {len(df)} rows into table {table_name}')
    conn.close()


def load(df, table_name):

    create_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            name VARCHAR(100),
            price VARCHAR(50)
        )
    """).format(sql.Identifier(table_name))

    cur.execute(create_query)

    conn.commit()

    insert_data(df, table_name)

def retrieve(table):

    select_query = f"SELECT * FROM {table};"
    df = pd.read_sql(select_query, conn)
    conn.close()
    return df
