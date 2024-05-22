import argparse

from asymmetric_cipher import RSA
from symmetric_cipher import AES
from file_manager import File


def main():
    parser = argparse.ArgumentParser(description="Encrypt/decrypt text using RSA and AES algorithms.")
    parser.add_argument("mode", choices=["key_gen", "encryption", "decryption"], help="Operation mode: key_gen, encryption, decryption.")
    args = parser.parse_args()

    settings = File.read_json("settings.json")

    def key_gen():
        symmetric_key = AES.generate_key(192)
        private_key, public_key = RSA.generate_key_pair()

        RSA.save_private_key(settings["private_key"], private_key)
        RSA.save_public_key(settings["public_key"], public_key)
        File.write_bytes(settings["symmetric_key"], RSA.encrypt(public_key, symmetric_key))

        print("keys were generated")

    def encryption():
        # Text encryption
        initial_text = File.read_bytes(settings["initial_file"])
        symmetric_key_encrypted = File.read_bytes(settings["symmetric_key"])
        private_key = RSA.load_private_key(settings["private_key"])

        symmetric_key = RSA.decrypt(private_key, symmetric_key_encrypted)
        encrypted_text = AES.encrypt(symmetric_key, initial_text)
        File.write_bytes(settings["encrypted_file"], encrypted_text)

        print("text encrypted")

    def decryption():
        encrypted_text = File.read_bytes(settings["encrypted_file"])
        symmetric_key_encrypted = File.read_bytes(settings["symmetric_key"])
        private_key = RSA.load_private_key(settings["private_key"])

        symmetric_key = RSA.decrypt(private_key, symmetric_key_encrypted)
        decrypted_text = AES.decrypt(symmetric_key, encrypted_text)
        File.write_bytes(settings["decrypted_file"], decrypted_text)

        print("text decrypted")

    if args.mode == "key_gen":
        key_gen()
    elif args.mode == "encryption":
        encryption()
    elif args.mode == "decryption":
        decryption()


if __name__ == "__main__":
    main()
