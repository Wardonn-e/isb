from json import dump
from random import shuffle


def generate_monoalphabetic_substitution() -> None:
    """
    Generates monoalphabetic substitution and writes it to a JSON file.

    Returns:
        None
    """
    try:
        alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        shuffle(alphabet)
        mapping: Dict[str, str] = {char: alphabet[i] for i, char in enumerate('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')}
        with open('monoalphabetic_substitution.json', 'w', encoding='utf-8') as f:
            dump(mapping, f, ensure_ascii=False, indent=4)
        print("JSON file successfully created.")
    except Exception as e:
        print(f"An error occurred: {e}")


generate_monoalphabetic_substitution()
