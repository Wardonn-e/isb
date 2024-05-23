import math

from scipy.special import gammainc

from constants import PI, SEQUENCE_CPP_PATH, SEQUENCE_JAVA_PATH, BLOCK_SIZE


def read_sequence_from_file(filename: str) -> str:
    """
    Reads a binary data from a file.

    Args:
        filename (str): The name of file.

    Returns:
        str: The binary sequence.
    """
    try:
        with open(filename, 'r') as file:
            sequence = file.read().strip()
        return sequence
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")


def frequency_bit_test(sequence: str) -> float:
    """
    Frequency test on a binary sequence.

    Args:
        sequence (str): The binary sequence.

    Returns:
        float: The p-value of the test.
    """
    sequence_length = len(sequence)
    sum_bits = sum(1 if bit == '1' else -1 for bit in sequence)
    s_obs = abs(sum_bits) / math.sqrt(sequence_length)
    p_value = math.erfc(s_obs / math.sqrt(2))
    return p_value


def same_consecutive_bits_test(sequence: str) -> float:
    """
    Performs the Runs Test on a binary sequence.

    Args:
        sequence (str): The binary sequence as a string.

    Returns:
        float: The p-value of the test.
    """
    sequence_length = len(sequence)
    proportion_ones = sequence.count('1') / sequence_length
    tau = 2 / math.sqrt(len(str(proportion_ones)))

    if abs(proportion_ones-0.5) < tau:
        count = 0
        for i in range(len(sequence) - 1):
            if not (sequence[i] == sequence[i+1]):
                count += 1

        return math.erfc(abs(count - 2 * len(sequence) * proportion_ones * (1 - proportion_ones))
                         / (2 * math.sqrt(2 * len(sequence)) * proportion_ones * (1 - proportion_ones)))
    return 0



def longest_run_of_ones_test(sequence: str) -> float:
    """
    Longest Run of Ones in Block Test on a binary sequence.

    Args:
        sequence (str): The binary sequence.

    Returns:
        float: The p-value of the test.
    """
    num_blocks = len(sequence) // BLOCK_SIZE
    binary_blocks = [sequence[i * 8:(i + 1) * 8] for i in range(num_blocks)]

    max_ones_per_block = []
    for block in binary_blocks:
        max_ones = 0
        current_ones = 0
        for bit in block:
            if bit == "1":
                current_ones += 1
            else:
                max_ones = max(current_ones, max_ones)
                current_ones = 0
        max_ones_per_block.append(max(current_ones, max_ones))

    frequency = [0, 0, 0, 0]
    frequency[0] = max_ones_per_block.count(0) + max_ones_per_block.count(1)
    frequency[1] = max_ones_per_block.count(2)
    frequency[2] = max_ones_per_block.count(3)
    frequency[3] = len(max_ones_per_block) - frequency[0] - frequency[1] - frequency[2]

    chi_square_stat = sum((frequency[i] - 16 * PI[i]) ** 2 / (16 * PI[i]) for i in range(len(frequency)))

    return gammainc(3 / 2, chi_square_stat / 2)


def perform_tests_on_sequence(sequence: str, source: str):
    """
    Runs all three NIST tests on a binary sequence and prints results.

    Args:
        sequence (str): Binary sequence as a string.
        source (str): Source of the sequence.
    """
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