import argparse

from asymmetric_cipher import RSA
from symmetric_cipher import AES
from file_manager import File


def main() -> None:
    """
    Main function to execute the encryption/decryption process.
    """
    parser = argparse.ArgumentParser(description="Encrypt/decrypt text using RSA and AES algorithms.")
    parser.add_argument("mode", choices=["key_gen", "encryption", "decryption"],
                        help="Operation mode: key_gen, encryption, decryption.")
    args = parser.parse_args()

    settings = File.read_json("settings.json")

    def key_gen() -> None:
        """
        Generates RSA key pair and AES symmetric key, and saves them to designated files.
        """
        symmetric_key = AES.generate_key(192)
        private_key, public_key = RSA.generate_key_pair()

        File.save_private_key(settings["private_key"], private_key)
        File.save_public_key(settings["public_key"], public_key)
        File.write_bytes(settings["symmetric_key"], RSA.encrypt(public_key, symmetric_key))

        print("keys were generated")

    def encryption():
        """
        Encrypts text file using RSA and AES algorithms.
        """
        initial_text = File.read_bytes(settings["initial_file"])
        symmetric_key_encrypted = File.read_bytes(settings["symmetric_key"])
        private_key = File.load_private_key(settings["private_key"])

        symmetric_key = RSA.decrypt(private_key, symmetric_key_encrypted)
        encrypted_text = AES.encrypt(symmetric_key, initial_text)
        File.write_bytes(settings["encrypted_file"], encrypted_text)

        print("text encrypted")

    def decryption() -> None:
        """
        Decrypts encrypted text file using RSA and AES algorithms.
        """
        encrypted_text = File.read_bytes(settings["encrypted_file"])
        symmetric_key_encrypted = File.read_bytes(settings["symmetric_key"])
        private_key = File.load_private_key(settings["private_key"])

        symmetric_key = RSA.decrypt(private_key, symmetric_key_encrypted)
        decrypted_text = AES.decrypt(symmetric_key, encrypted_text)
        File.write_bytes(settings["decrypted_file"], decrypted_text)

        print("text decrypted")

    match args.mode:
        case "key_gen":
            key_gen()
        case "encryption":
            encryption()
        case "decryption":
            decryption()
        case _:
            print("Unknown mode")


if __name__ == "__main__":
    main()
