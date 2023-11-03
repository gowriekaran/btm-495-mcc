from decouple import config
import psycopg2

DATABASE_URL = config('DATABASE_URL')

try:
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE mcc")
    print("Database created!")
except psycopg2.errors.DuplicateDatabase:
    print("Database already exists!")
finally:
    cursor.close()
    conn.close()
