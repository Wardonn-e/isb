from func import read_json_from_file, read_from_file, analyze_text, decode_text, write_to_file
from constants import input_path, output_path, substitution_path

if __name__ == "__main__":
    input_text = read_from_file(input_path)
    analyze_text(input_text)
    substitution = read_json_from_file(substitution_path)
    output_text = decode_text(input_text, substitution)
    write_to_file(output_path, output_text)
