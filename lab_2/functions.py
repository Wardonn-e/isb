import math
from scipy.special import gammaincc
from constants import PI, SEQUENCE_CPP_PATH, SEQUENCE_JAVA_PATH, BLOCK_SIZE

def read_sequence_from_file(filename: str) -> str:
    try:
        with open(filename, 'r') as file:
            sequence = file.read().strip()
        return sequence
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} does not exist.")
    except IOError:
        raise IOError(f"An error occurred while reading the file {filename}.")

def frequency_bit_test(sequence: str) -> float:
    sequence_length = len(sequence)
    sum_bits = sum(1 if bit == '1' else -1 for bit in sequence)
    s_obs = abs(sum_bits) / math.sqrt(sequence_length)
    p_value = math.erfc(s_obs / math.sqrt(2))
    return p_value

def same_consecutive_bits_test(sequence: str) -> float:
    sequence_length = len(sequence)
    proportion_ones = sequence.count('1') / sequence_length
    tau = 2 / math.sqrt(sequence_length)

    if abs(proportion_ones - 0.5) >= tau:
        return 0.0

    number_of_runs = 1
    for i in range(1, sequence_length):
        if sequence[i] != sequence[i - 1]:
            number_of_runs += 1

    expected_runs = 2 * sequence_length * proportion_ones * (1 - proportion_ones)
    variance = 2 * math.sqrt(2 * sequence_length) * proportion_ones * (1 - proportion_ones)
    p_value = math.erfc(abs(number_of_runs - expected_runs) / variance)
    return p_value

def longest_run_of_ones_test(sequence: str) -> float:
    sequence_length = len(sequence)
    pi = PI

    number_of_blocks = sequence_length // BLOCK_SIZE
    max_ones_in_block = [0] * BLOCK_SIZE

    for i in range(number_of_blocks):
        block = sequence[i * BLOCK_SIZE:(i + 1) * BLOCK_SIZE]
        max_run = max(len(run) for run in block.split('0'))
        max_ones_in_block[max_run] += 1

    chi_squared = sum(
        [(max_ones_in_block[i] - number_of_blocks * pi[i]) ** 2 / (number_of_blocks * pi[i]) for i in range(3)]
    )
    p_value = gammaincc(3 / 2, chi_squared / 2)
    return p_value

def perform_tests_on_sequence(sequence: str, source: str):
    print(f"Result for {source}:")

    print("Frequency Bit Test:")
    p_value = frequency_bit_test(sequence)
    print(f"P-value: {p_value}")

    print("\nSame Consecutive Bits Test:")
    p_value = same_consecutive_bits_test(sequence)
    print(f"P-value: {p_value}")

    print("\nLongest Run of Ones in a Block Test:")
    p_value = longest_run_of_ones_test(sequence)
    print(f"P-value: {p_value}")

    print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    sequence_cpp = read_sequence_from_file(SEQUENCE_CPP_PATH)
    sequence_java = read_sequence_from_file(SEQUENCE_JAVA_PATH)

    perform_tests_on_sequence(sequence_cpp, "C++ Sequence")
    perform_tests_on_sequence(sequence_java, "Java Sequence")
