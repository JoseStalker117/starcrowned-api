from dotenv import load_dotenv
import os, psycopg2

load_dotenv('./config.env')
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")


class sbPostgre:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT,
                dbname=DBNAME
            )
            print("[Postgres] Connection successful!")
        except Exception as e:
            print(f"[Postgres] Failed to connect: {e}")

    
    def test(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM school.escuela;")
        result = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return result

        