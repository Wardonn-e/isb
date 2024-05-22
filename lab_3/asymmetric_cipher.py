from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

from file_manager import File


class RSA:

    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_key_pair() -> tuple:
        """
        Generate RSA key pair.

        Returns:
            tuple: RSA private key and public key.
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        return private_key, private_key.public_key()

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
    def encrypt(public_key: rsa.RSAPublicKey, text: bytes) -> bytes:
        """
        Encrypt text using RSA public key.

        Args:
            public_key (rsa.RSAPublicKey): RSA public key.
            text (bytes): Text to be encrypted.
        Returns:
            bytes: Encrypted ciphertext.
        """
        return public_key.encrypt(
            text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def decrypt(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:
        """
        Decrypt ciphertext using RSA private key.

        Args:
            private_key (rsa.RSAPrivateKey): RSA private key.
            ciphertext (bytes): Ciphertext to be decrypted.
        Returns:
            bytes: Decrypted text.
        """
        return private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
