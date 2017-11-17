import psycopg2
import os

def hello(event, context):
    print os.environ.get('port')
    try:
        conn = psycopg2.connect("dbname = os.environ.get('dbname') user = os.environ.get('user') host= os.envrion.get('host') password = os.environ.get('pass')")
        return "Connection established"
    except psycopg2.DatabaseError, err:
        return str(err)

    cur = conn.cursor()
