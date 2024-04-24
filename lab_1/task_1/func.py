from typing import Dict
from json import dump, load, JSONDecodeError
from random import shuffle
from constants import ALPHABET


def write_to_file(filename: str, text: str) -> None:
    """
    Write text to a file.

    Args:
        filename (str): Path to the output text file.
        text (str): The text to write to the file.

    Raises:
        IOError: If there is an error writing to the file.

    Returns:
        None
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Error writing to file: {e}")


def read_from_file(filename: str) -> str:
    """
    Read text from a file.

    Args:
        filename (str): Path to the input text file.

    Returns:
        str: The text read from the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except Exception as e:
        print(f"Error reading from file: {e}")
        return ""


def write_to_json(data: dict, filename: str) -> None:
    """
    Write data to a JSON file.

    Args:
        data (dict): The dict data to be written.
        filename (str): The name of JSON file.

    Returns:
        None
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")


def read_json_from_file(mapping_file: str) -> dict:
    """
    Read JSON from a file.

    Args:
        mapping_file (str): The name of the JSON file to read from.

    Returns:
        dict: The JSON content read from the file.
    """
    try:
        with open(mapping_file, 'r', encoding='utf-8') as f:
            mapping = load(f)
            return mapping
    except IOError as e:
        print(f"Error reading from file: {e}")
        return {}
    except JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}


def generate_substitution() -> dict[str, str]:
    """
    Generates substitution and writes it to a JSON file.

    Returns:
        Dict[str, str]: Mapping to substituted characters.
    """
    alphabet = list(ALPHABET)
    shuffle(alphabet)
    mapping: Dict[str, str] = {char: alphabet[i] for i, char in enumerate(ALPHABET)}
    return mapping


def encrypt_text(input_text: str, mapping: dict) -> str:
    """
    Encrypts text.

    Args:
        input_text (str): The text to encrypt.
        mapping (dict): The mapping for substitution.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ''.join(mapping.get(char, char) for char in input_text.upper())
    return encrypted_text
