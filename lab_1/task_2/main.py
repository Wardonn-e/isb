from func import read_json_from_file, read_from_file, analyze_text, decode_text, write_to_file

from constants import PATH_INPUT, PATH_OUTPUT, PATH_SUBSTITUTION


if __name__ == "__main__":
    input_text = read_from_file(PATH_INPUT)
    analyze_text(input_text)
    substitution = read_json_from_file(PATH_SUBSTITUTION)
    output_text = decode_text(input_text, substitution)
    write_to_file(PATH_OUTPUT, output_text)
