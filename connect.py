'''
Test a connection to the PostgreSQL database using psycopg.
'''


import psycopg
import os

conn = psycopg.connect(
    host="localhost",
    port=5432,
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD"),
    dbname=os.environ.get("POSTGRES_DB")
)

print(conn.execute("SELECT version();").fetchone())
