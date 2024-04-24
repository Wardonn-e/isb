from func import *
from constants import path_to_json_paths

if __name__ == "__main__":
    path = read_json_from_file(path_to_json_paths)
    input_text = read_from_file(path["input"])
    substitution = generate_substitution()
    write_to_json(substitution, path["substitution"])
    encrypted_text = encrypt_text(input_text, substitution)
    write_to_file(path["output"], encrypted_text)
