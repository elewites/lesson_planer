from typing import Optional, Dict, Any
import json
import os


class Serializer:
    """
    Serializer manages reading from and writing to JSON files.

    Methods:
        read_from_json_file: Reads JSON data from a file and returns it as a dictionary.
        write_to_json_file: Writes data to a file in JSON format.

    Attributes:
        None
    """

    @staticmethod
    def read_from_json_file(filepath: str) -> Optional[Dict[str, Any]]:
        """
        Read JSON data from a file.

        Args:
            filepath (str): The path to the JSON file.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the JSON data, or None if an error occurs.

        Raises:
            FileNotFoundError: If the specified file is not found.
            json.JSONDecodeError: If there is an error decoding the JSON data.
        """
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File '{filepath}' not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None

    @staticmethod
    def write_to_json_file(filepath: str, data: Dict[str, Any]) -> None:
        """
        Write data to a JSON file.

        Args:
            filepath (str): The path to the JSON file.
            data (Dict[str, Any]): The data to be written to the file.

        Returns:
            None

        Raises:
            FileNotFoundError: If the specified file is not found.
            json.JSONDecodeError: If there is an error decoding the JSON data.
        """
        try:
            with open(filepath, "w") as file:
                json.dump(data, file, indent=2)
            print(f"Data written to '{filepath}'")
        except FileNotFoundError:
            print(f"File '{filepath}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

    @staticmethod
    def get_full_path(relative_path):
        """
        Get the full path by combining the current directory with a given relative path.

        Args:
            relative_path (str): The relative path to be combined with the current directory.

        Returns:
            str: The full path obtained by combining the current directory and the relative path.
        """

        # Get the directory where the script or executable is located
        current_directory = (
            os.path.dirname(__file__) if hasattr(__file__, "__file__") else os.getcwd()
        )
        # Combine the current directory and the relative path to get the full path
        full_path = os.path.join(current_directory, relative_path)
        return full_path
