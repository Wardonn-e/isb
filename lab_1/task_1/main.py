from func import read_from_file, generate_substitution, write_to_json, encrypt_text, write_to_file
from constants import path_input, path_output, path_substitution

if __name__ == "__main__":
    input_text = read_from_file(path_input)
    substitution = generate_substitution()
    write_to_json(substitution, path_substitution)
    encrypted_text = encrypt_text(input_text, substitution)
    write_to_file(path_output, encrypted_text)
