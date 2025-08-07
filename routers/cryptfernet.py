from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv('./config.env')


class CryptFernet:    
    def __init__(self):
        self.key = os.getenv("fernetkey")
        self.fernet = Fernet(self.key)
        
    def encrypt(self, message: str) -> str:
        fernet = Fernet(self.key)
        encrypted_message = fernet.encrypt(message.encode())
        return encrypted_message.decode()

    def decrypt(self, encrypted_message: str) -> str:
        fernet = Fernet(self.key)
        decrypted_message = fernet.decrypt(encrypted_message.encode())
        return decrypted_message.decode()


