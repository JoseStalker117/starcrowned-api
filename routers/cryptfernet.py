from cryptography.fernet import Fernet
from dotenv import load_dotenv
from typing import Any
import os, json, pickle

load_dotenv('./config.env')


class CryptFernet:    
    def __init__(self):
        self.key = os.getenv("fernetkey")
        self.fernet = Fernet(self.key)
        
    # ===== Encriptar/Desencriptar texto simple =====
    def encrypt(self, message: str) -> str:
        encrypted_message = self.fernet.encrypt(message.encode())
        return encrypted_message.decode()

    def decrypt(self, encrypted_message: str) -> str:
        decrypted_message = self.fernet.decrypt(encrypted_message.encode())
        return decrypted_message.decode()
    
    # ===== Encriptar/Desencriptar usando JSON =====
    def encrypt_dict(self, data: dict) -> str:
        json_str = json.dumps(data)
        return self.encrypt(json_str)

    def decrypt_dict(self, encrypted_data: str) -> dict:
        json_str = self.decrypt(encrypted_data)
        return json.loads(json_str)

    def encrypt_list(self, data: list) -> str:
        json_str = json.dumps(data)
        return self.encrypt(json_str)

    def decrypt_list(self, encrypted_data: str) -> list:
        json_str = self.decrypt(encrypted_data)
        return json.loads(json_str)

    # ===== Encriptar/Desencriptar objetos complejos (pickle) =====
    def encrypt_object(self, obj: Any) -> str:
        pickle_bytes = pickle.dumps(obj)
        encrypted_bytes = self.fernet.encrypt(pickle_bytes)
        return encrypted_bytes.decode()

    def decrypt_object(self, encrypted_data: str) -> Any:
        decrypted_bytes = self.fernet.decrypt(encrypted_data.encode())
        return pickle.loads(decrypted_bytes)



