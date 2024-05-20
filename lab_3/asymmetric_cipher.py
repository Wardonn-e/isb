from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class AsymmetricCryptography:
    def __init__(self, private_key_path: str, public_key_path: str) -> None:
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path

    @staticmethod
    def generate_key_pair() -> tuple:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        return private_key, private_key.public_key()

    def save_private_key(self, private_key: rsa.RSAPrivateKey) -> None:
        with open(self.private_key_path, 'wb') as key_file:
            key_file.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

    def save_public_key(self, public_key: rsa.RSAPublicKey) -> None:
        with open(self.public_key_path, 'wb') as key_file:
            key_file.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

    def load_private_key(self) -> rsa.RSAPrivateKey:
        with open(self.private_key_path, 'rb') as key_file:
            return serialization.load_pem_private_key(key_file.read(), password=None)

    def load_public_key(self) -> rsa.RSAPublicKey:
        with open(self.public_key_path, 'rb') as key_file:
            return serialization.load_pem_public_key(key_file.read())

    @staticmethod
    def encrypt_with_public_key(public_key: rsa.RSAPublicKey, text: bytes) -> bytes:
        return public_key.encrypt(
            text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def decrypt_with_private_key(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:
        return private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
