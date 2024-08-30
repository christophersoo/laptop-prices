import psycopg2
from dbinfo import DB_NAME, DB_USER, DB_PW, DB_HOST, DB_PORT

conn = {
        'dbname': DB_NAME,
        'username': DB_USER,
        'password': DB_PW,
        'host': DB_HOST,
        'port': DB_PORT
        }

if not conn:
    raise OperationalError("Database is not found.")
else:
    print("Database Connected Successfully.")
