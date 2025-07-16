import firebase_admin
from  firebase_admin import credentials, db


cred = credentials.Certificate('starcrowned-key.json')
try:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://starcrowned-4d560-default-rtdb.firebaseio.com/'
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