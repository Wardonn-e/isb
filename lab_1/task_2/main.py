from func import *
from constants import path_to_json_paths


if __name__ == "__main__":
    path = read_json_from_file(path_to_json_paths)
    input_text = read_from_file(path["input"])
    analyze_text(input_text)
    substitution = read_json_from_file(path["substitution"])
    output_text = decode_text(input_text, substitution)
    write_to_file(path["output"], output_text)