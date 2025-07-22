import firebase_admin, os
from  firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv('./config.env')

cred = credentials.Certificate('./routers/starcrowned-key.json')
try:
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.getenv("fbdb_url")
    })
    print("[Firebase] Conexión inicializada correctamente")
except ValueError:
    print("[Firebase] Firebase ya está inicializado")
except Exception as e:
    print(f"[Firebase] Error al inicializar: {e}")



# Funciones de ejemplo para mandar a llamar desde las rutas
def Login():
    return

def Register():
    return

def Database():
    return