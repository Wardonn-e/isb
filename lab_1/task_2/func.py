from json import load


def analyze_text(file_path: str) -> None:
    """
    Reads text from a file and frequency analysis.

    Args:
        file_path (str): Path to the input text file.

    Returns:
        None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        frequencies = {}
        total_characters = 0
        for char in text:
            frequencies[char] = frequencies.get(char, 0) + 1
            total_characters += 1
        normalized_frequencies = {char: freq / total_characters for char, freq in frequencies.items()}
        sorted_frequencies = sorted(normalized_frequencies.items(), reverse=True)
        print("Frequency Analysis:")
        for char, frequency in sorted_frequencies:
            print(f"{char}: {frequency:.4}")
    except Exception as e:
        print(f"An error occurred: {e}")


def decode_text(input_file: str, output_file: str, map_file: str) -> None:
    """
    Decodes text from the input file using a monoalphabetic substitution and writes the result to the output file.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output text file.
        map_file (str): Path to the JSON file.

    Returns:
        None
    """
    try:
        with open(map_file, 'r', encoding='utf-8') as f:
            map = load(f)
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        decoded_text = ''.join(map.get(char, char) for char in text)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decoded_text)

        print("Text successfully decoded and written to", output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
