from dotenv import load_dotenv
from . import cryptfernet as crypt
import os, psycopg2, json

load_dotenv('./config.env')

def load_sql(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    
    
class sbPostgre:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=       os.getenv("user"),
                password=   os.getenv("password"),
                host=       os.getenv("host"),
                port=       os.getenv("port"),
                dbname=     os.getenv("dbname")
            )
        except Exception as e:
            print(f"[Postgres] Failed to connect: {e}")
    
    def disconnect(self):
        if self.connection:
            self.connection.close()

    
    def escuelas(self):
        self.connect()
        querry = load_sql('./querrys/get_escuela.sql')
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(querry)
                result = cursor.fetchall()
                
        except Exception as e:
            print(f"[Postgres] Error executing query: {e}")
            result = []
        finally:
            self.disconnect()
        return result
        