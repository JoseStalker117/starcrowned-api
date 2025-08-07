import firebase_admin, os
from  firebase_admin import credentials, firestore
from dotenv import load_dotenv
from . import cryptfernet as crypt

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


class fbCrowned:
    def __init__(self):
        self.fs = firestore.client()
    
    def insert(self):
        try:
            doc_ref = self.fs.collection('crowned').document('data')
            doc_ref.set({
                'name': 'StarCrowned',
                'description': 'A project to crown the stars.',
                'status': 'active'
            })
            return "Documento insertado correctamente"
        except Exception as e:
            return f"Error getting document: {e}"
        
        