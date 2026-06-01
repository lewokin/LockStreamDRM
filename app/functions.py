from cryptography.fernet import Fernet
import random
import string

fernet = Fernet(b'e9xCFeEkwAylXTr7XydO-OX19Kh_HS0oJarZxVGkXY8=')

def encrypt_dictoniary(dictionary: dict) -> dict:
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    for i in range(len(keys)):
        keys[i] = fernet.encrypt(str.encode(keys[i])).decode("utf-8")
    
    for i in range(len(values)):
        values[i] = fernet.encrypt(str.encode(values[i])).decode("utf-8")

    return dict(zip(keys,values))

def decrypt_dictoniary(dictionary: dict) -> dict:
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    for i in range(len(keys)):
        keys[i] = fernet.decrypt(str.encode(keys[i])).decode("utf-8")
    
    for i in range(len(values)):
        values[i] = fernet.decrypt(str.encode(values[i])).decode("utf-8")

    return dict(zip(keys,values))
