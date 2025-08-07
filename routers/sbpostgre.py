from dotenv import load_dotenv
from . import cryptfernet as crypt
import os, psycopg2, json

load_dotenv('./config.env')

class sbPostgre:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=       os.getenv("user"),
                password=   os.getenv("password"),
                host=       os.getenv("host"),
                port=       os.getenv("port"),
                dbname=     os.getenv("dbname")
            )
            print("[Postgres] Connection successful!")
        except Exception as e:
            print(f"[Postgres] Failed to connect: {e}")
    
    def disconnect(self):
        if self.connection:
            self.connection.close()

    
    def test(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM school.escuela;")
        result = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return result
        