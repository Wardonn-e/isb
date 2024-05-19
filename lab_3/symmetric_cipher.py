import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


class AES:
    def __init__(self, key: bytes):
        self.key = key

    @staticmethod
    def generate_key(key_length: int) -> bytes:
        if key_length not in [128, 192, 256]:
            raise ValueError("Длина ключа должна быть 128, 192 или 256 бит")
        key_length_bytes = key_length // 8
        key = os.urandom(key_length_bytes)
        return key

    def encrypt(self, text: str) -> bytes:
        iv = os.urandom(16)  # Initialization vector
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()

        padded_data = padder.update(text.encode()) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        return iv + ciphertext

    def decrypt(self, text: bytes) -> str:
        iv = text[:16]
        actual_ciphertext = text[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

        decrypted_padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()
        plaintext = unpadder.update(decrypted_padded_data) + unpadder.finalize()

        return plaintext.decode()


key = AES.generate_key(192)
print(key)
cipher = AES(key)

original_text = "Бубубубубубу"
encrypted = cipher.encrypt(original_text)
print("Зашифрованный текст:", encrypted)

decrypted = cipher.decrypt(encrypted)
print("Расшифрованный текст:", decrypted)
