from func import *

if __name__ == "__main__":
    generate_monoalphabetic_substitution()
    encrypt_text("input.txt", "output.txt", "monoalphabetic_substitution.json")