import os
from cryptography.fernet import Fernet

def make_key(key_path: str) -> str:
    key = Fernet.generate_key()
    with open(key_path, "wb") as f:
        f.write(key)
    return key_path

def encrypt(text: str, key_path: str) -> str:
    with open(key_path, "rb") as f:
        key = f.read()
    fernet = Fernet(key)
    return fernet.encrypt(text.encode()).decode()

def decrypt(token: str, key_path: str) -> str:
    with open(key_path, "rb") as f:
        key = f.read()
    fernet = Fernet(key)
    return fernet.decrypt(token.encode()).decode()