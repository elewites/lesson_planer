import os
import json
from .serializer import Serializer

# Define a test directory and test data
test_dir = "test_data"
test_data = {
    "sentences": {
        "section_1": ["favorite sentece in section 1"],
        "section_2": ["favorite sentence in section 2"],
        "section_3": ["favorite sentence in section 3"],
    },
    "words": {
        "section_1": ["apple", "apple"],
        "section_2": ["roses", "roses"],
        "section_3": ["wood", "fire"],
    },
}


class TestSerializer:
    @classmethod
    def setup_class(cls):
        # Create a test directory if it doesn't exist
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)

    @classmethod
    def teardown_class(cls):
        # Clean up by removing the test directory and its contents
        if os.path.exists(test_dir):
            for filename in os.listdir(test_dir):
                file_path = os.path.join(test_dir, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            os.rmdir(test_dir)

    def test_read_from_json_file(self):
        # Test reading from a JSON file
        file_path = os.path.join(test_dir, "test_file.json")
        with open(file_path, "w") as file:
            json.dump(test_data, file)

        result = Serializer.read_from_json_file(file_path)
        assert result == test_data

    def test_read_from_json_file_not_found(self):
        # Test reading from a non-existent JSON file
        file_path = os.path.join(test_dir, "non_existent.json")

        result = Serializer.read_from_json_file(file_path)
        assert result is None

    def test_write_to_json_file(self):
        # Test writing to a JSON file
        file_path = os.path.join(test_dir, "write_test.json")
        Serializer.write_to_json_file(file_path, test_data)

        with open(file_path, "r") as file:
            result_data = json.load(file)

        assert result_data == test_data
