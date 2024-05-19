from func import read_from_file, generate_substitution, write_to_json, encrypt_text, write_to_file

from constants import PATH_INPUT, PATH_OUTPUT, PATH_SUBSTITUTION


if __name__ == "__main__":
    input_text = read_from_file(PATH_INPUT)
    substitution = generate_substitution()
    write_to_json(substitution, PATH_SUBSTITUTION)
    encrypted_text = encrypt_text(input_text, substitution)
    write_to_file(PATH_OUTPUT, encrypted_text)
