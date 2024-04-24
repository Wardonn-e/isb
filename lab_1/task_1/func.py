from typing import Dict
from json import dump, load
from random import shuffle


def generate_monoalphabetic_substitution() -> None:
    """
    Generates monoalphabetic substitution and writes it to a JSON file.

    Returns:
        None
    """
    try:
        alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
        shuffle(alphabet)
        mapping: Dict[str, str] = {char: alphabet[i] for i, char in enumerate('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')}
        with open('monoalphabetic_substitution.json', 'w', encoding='utf-8') as f:
            dump(mapping, f, ensure_ascii=False, indent=4)
        print("JSON file successfully created.")
    except Exception as e:
        print(f"An error occurred: {e}")


def encrypt_text(input_file: str, output_file: str, mapping_file: str) -> None:
    """
    Encrypts text from the input file using a monoalphabetic substitution
    and writes the result to the output file.

    Args:
        input_file (str): Path to the input txt file.
        output_file (str): Path to the output txt file.
        mapping_file (str): Path to the JSON file.

    Returns:
        None
    """
    try:
        with open(mapping_file, 'r', encoding='utf-8') as f:
            mapping = load(f)
        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                text = file.read().upper()
        except FileNotFoundError:
            print(f"File '{input_file}' not found.")
        encrypted_text = ''.join(mapping.get(char, char) for char in text)
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(encrypted_text)
        print("Text successfully encrypted and written to", output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
