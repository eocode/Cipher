import os
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from pathlib import Path
import base64


class CipherTools:

    def __init__(self, file=''):
        self.file = file
        self.filename = self.get_path(file)
        self.cipher_folder = 'cipher'
        self.base_folder = 'files'
        self.key = ''

    def generate_key(self):
        self.key = Fernet.generate_key()
        return self.key

    def save_key_file(self):
        with open("./"+self.cipher_folder+"/key.key", "wb") as file:
            file.write(self.key)

    def load_key(self):
        return open("./"+self.base_folder+"/key.key", "rb").read()

    def encrypt(self, key):
        try:
            f = Fernet(key)
            with open("./"+self.base_folder+"/"+self.file+"", "rb") as file:
                file_info = file.read()
            encrypted_data = f.encrypt(file_info)
            self.create_dirname("./"+self.cipher_folder+"/"+self.filename+"")
            with open("./"+self.cipher_folder+"/"+self.filename+"/encrypt.txt", "wb") as file:
                file.write(encrypted_data)
            return True
        except:
            return False

    def decrypt(self, key):
        try:
            f = Fernet(key)
            with open("./"+self.cipher_folder+"/"+self.filename+"/encrypt.txt", "rb") as file:
                encripted_data = file.read()
            decrypted_data = f.decrypt(encripted_data)
            with open("./"+self.cipher_folder+"/"+self.filename+"/decrypt.txt", "wb") as file:
                file.write(decrypted_data)
            return True
        except:
            return False

    def create_dirname(self, dirname):
        try:
            os.stat(dirname)
        except:
            os.mkdir(dirname)

    def get_path(self, file):
        return Path(file).stem.replace(" ", "")

    def init_paths(self):
        self.create_dirname('./files')
        self.create_dirname('./cipher')
