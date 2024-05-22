import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64

from file_manager import File


class AES:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_key(key_length: int) -> bytes:
        """
        Generates AES key.

        Args:
            key_length (int): The length of the key in bits.

        Returns:
            bytes: The generated AES key.
        """
        if key_length not in [128, 192, 256]:
            raise ValueError("The key length must be 128, 192 or 256 bits")
        key_length_bytes = key_length // 8
        key = os.urandom(key_length_bytes)
        return key

    @staticmethod
    def save_key(key: bytes, file_path: str) -> None:
        """
        Saves the AES key to a file.

        Args:
            key (bytes): The AES key to save.
            file_path (str): The file path to save the key.
        """
        File.write_bytes(file_path, key)

    @staticmethod
    def load_key(file_path: str) -> bytes:
        """
        Loads the AES key from a file.

        Args:
            file_path (str): The file path to load the key from.

        Returns:
            bytes: The loaded AES key.
        """
        return base64.b64decode(File.read_bytes(file_path))

    @staticmethod
    def encrypt(key: bytes, data: bytes) -> bytes:
        """
        Encrypts data using AES.

        Args:
            key (bytes): The AES key for encryption.
            data (bytes): The plaintext data to encrypt.

        Returns:
            bytes: The encrypted data.
        """
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()

        padded_data = padder.update(data) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        return iv + ciphertext

    @staticmethod
    def decrypt(key: bytes, data: bytes) -> bytes:
        """
        Decrypts data using AES.

        Args:
            key (bytes): The AES key for decryption.
            data (bytes): The encrypted data to decrypt.

        Returns:
            bytes: The decrypted data.
        """
        iv = data[:16]
        actual_ciphertext = data[16:]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

        decrypted_padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()
        plaintext = unpadder.update(decrypted_padded_data) + unpadder.finalize()

        return plaintext
