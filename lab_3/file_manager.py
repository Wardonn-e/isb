import json

class File:
    @staticmethod
    def read_bytes(file_path: str) -> bytes:
        """
        Reads bytes from a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            bytes: The bytes read from the file.
        """
        try:
            with open(file_path, "rb") as file:
                data = file.read()
            return data
        except Exception as error:
            print(error)

    @staticmethod
    def read(file_path: str) -> str:
        """
        Reads text from a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The text read from the file.
        """
        try:
            with open(file_path, "r") as file:
                data = file.read()
            return data
        except Exception as error:
            print(error)

    @staticmethod
    def write(file_path: str, data: str) -> None:
        """
        Writes text to a file.

        Args:
            file_path (str): The path to the file.
            data (str): The text to write to the file.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(data)
        except Exception as error:
            print(error)

    @staticmethod
    def write_bytes(file_path: str, data: bytes) -> None:
        """
        Writes bytes to a file.

        Args:
            file_path (str): The path to the file.
            data (bytes): The bytes to write to the file.
        """
        try:
            with open(file_path, "wb") as file:
                file.write(data)
        except Exception as error:
            print(error)

    @staticmethod
    def read_json(path: str) -> dict:
        """
        Read JSON file.

        Args:
            path (str): Path to the JSON file.

        Returns:
            dict: Сontents JSON file.
        """
        with open(path, "r", encoding="UTF-8") as file:
            return json.load(file)
