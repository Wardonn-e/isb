import base64
import json

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class File:
    """
    A utility class for file operations.
    """

    @staticmethod
    def read_bytes(file_path: str) -> bytes:
        """
        Reads bytes from a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            bytes: The bytes read from the file.
        """
        try:
            with open(file_path, "rb") as file:
                data = file.read()
            return data
        except Exception as error:
            print(error)

    @staticmethod
    def read(file_path: str) -> str:
        """
        Reads text from a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The text read from the file.
        """
        try:
            with open(file_path, "r") as file:
                data = file.read()
            return data
        except Exception as error:
            print(error)

    @staticmethod
    def write(file_path: str, data: str) -> None:
        """
        Writes text to a file.

        Args:
            file_path (str): The path to the file.
            data (str): The text to write to the file.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(data)
        except Exception as error:
            print(error)

    @staticmethod
    def write_bytes(file_path: str, data: bytes) -> None:
        """
        Writes bytes to a file.

        Args:
            file_path (str): The path to the file.
            data (bytes): The bytes to write to the file.
        """
        try:
            with open(file_path, "wb") as file:
                file.write(data)
        except Exception as error:
            print(error)

    @staticmethod
    def read_json(path: str) -> dict:
        """
        Read JSON file.

        Args:
            path (str): Path to the JSON file.

        Returns:
            dict: Сontents JSON file.
        """
        try:
            with open(path, "r", encoding="UTF-8") as file:
                return json.load(file)
        except Exception as error:
            print(error)

    @staticmethod
    def save_private_key(private_key_path: str, private_key: rsa.RSAPrivateKey) -> None:
        """
        Save RSA private key to a file.

        Args:
            private_key_path (str): Path to save the private key.
            private_key (rsa.RSAPrivateKey): RSA private key.
        """
        File.write_bytes(private_key_path,
                         private_key.private_bytes(
                             encoding=serialization.Encoding.PEM,
                             format=serialization.PrivateFormat.TraditionalOpenSSL,
                             encryption_algorithm=serialization.NoEncryption()
                         ))

    @staticmethod
    def save_public_key(public_key_path: str, public_key: rsa.RSAPublicKey) -> None:
        """
        Save RSA public key to a file.

        Args:
            public_key_path (str): Path to save the public key.
            public_key (rsa.RSAPublicKey): RSA public key.
        """
        File.write_bytes(public_key_path,
                         public_key.public_bytes(
                             encoding=serialization.Encoding.PEM,
                             format=serialization.PublicFormat.SubjectPublicKeyInfo
                         ))

    @staticmethod
    def load_private_key(private_key_path: str) -> rsa.RSAPrivateKey:
        """
        Load RSA private key from a file.

        Args:
            private_key_path (str): Path to load the private key from.
        Returns:
            rsa.RSAPrivateKey: Loaded RSA private key.
        """
        return serialization.load_pem_private_key(File.read_bytes(private_key_path), password=None)

    @staticmethod
    def load_public_key(public_key_path: str) -> rsa.RSAPublicKey:
        """
        Load RSA public key from a file.

        Args:
            public_key_path (str): Path to load the public key from.
        Returns:
            rsa.RSAPublicKey: Loaded RSA public key.
        """
        return serialization.load_pem_public_key(File.read_bytes(public_key_path))

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