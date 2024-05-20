import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64


class AES:
    def __init__(self, key: bytes) -> None:
        self.key = key

    @staticmethod
    def generate_key(key_length: int) -> bytes:
        if key_length not in [128, 192, 256]:
            raise ValueError("Длина ключа должна быть 128, 192 или 256 бит")
        key_length_bytes = key_length // 8
        key = os.urandom(key_length_bytes)
        return key

    @staticmethod
    def save_key(key: bytes, file_path: str) -> None:
        with open(file_path, 'wb') as key_file:
            key_file.write(base64.b64encode(key))

    @staticmethod
    def load_key(file_path: str) -> bytes:
        with open(file_path, 'rb') as key_file:
            key = base64.b64decode(key_file.read())
        return key

    def encrypt(self, data: bytes) -> bytes:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()

        padded_data = padder.update(data) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        return iv + ciphertext

    def decrypt(self, data: bytes) -> bytes:
        iv = data[:16]
        actual_ciphertext = data[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

        decrypted_padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()
        plaintext = unpadder.update(decrypted_padded_data) + unpadder.finalize()

        return plaintext
