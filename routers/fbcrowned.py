import firebase_admin, os
from  firebase_admin import credentials, firestore
from . import cryptfernet as crypt
from pydantic import BaseModel
from datetime import datetime
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


class fbCrowned:
    def __init__(self):
        self.fs = firestore.client()
        self.crypt = crypt.CryptFernet()
    
    def roles(self, uid: str):
        try:
            doc_ref = self.fs.collection('usuarios').document(uid)
            doc = doc_ref.get()
            
            if doc.exists:
                data = doc.to_dict()
                return data.get('rol', 'No role found')
            else:   
                return "No such document!"
        except Exception as e:
            return f"Error getting document: {e}"
    
    def fkey(self, uid: str):
        try:
            doc_ref = self.fs.collection('usuarios').document(uid)
            doc = doc_ref.get()
            
            if doc.exists:
                data = doc.to_dict()
                return data.get('fkey', 'No fkey found')
            else:   
                return "No such document!"
        except Exception as e:
            return f"Error getting document: {e}"
        
        
    def registrar(self, user: BaseModel):
        try:            
            doc_ref = self.fs.collection('users').document(user.uid)
            doc_ref.set({
                'uid': user.uid,
                'nombre': user.nombre,
                'email': user.email,
                'telefono': user.telefono,
                'rol': user.rol,
                'activo': user.activo,
                'fecha_creacion': user.fecha_creacion.isoformat(),
                'ultimo_login': user.ultimo_login.isoformat(),
                'fkey': user.fkey
                })
            
            return "Usuario registrado correctamente"
        except Exception as e:
            return f"Error al registrar usuario: {e}"
        
    def actualizar(self, uid: str, updates: dict):
        try:
            doc_ref = self.fs.collection('users').document(uid)
            doc_ref.update(updates)
            return "Usuario actualizado correctamente"
        except Exception as e:
            return f"Error al actualizar usuario: {e}"
        
    def obtener_usuario(self, uid: str):
        try:
            doc_ref = self.fs.collection('usuarios').document(uid)
            doc = doc_ref.get()
            if doc.exists:
                return doc.to_dict()
            else:
                return "No such document!"
        except Exception as e:
            return f"Error getting document: {e}"
        
