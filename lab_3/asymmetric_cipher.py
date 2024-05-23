from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

from file_manager import File


class RSA:
    """
    Class representing RSA encryption and decryption operations.
    """

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
