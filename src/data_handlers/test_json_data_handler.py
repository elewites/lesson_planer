import os
import json
from .json_data_handler import JsonDataHandler

# Define a test directory and test file path
test_dir = "test_data"
test_file_path = os.path.join(test_dir, "test_data.json")

# Define test data
initial_test_data = {
    "sentences": {"section1": ["sentence1", "sentence2"]},
    "words": {"section2": ["word1", "word2"]},
}


class TestJsonDataHandler:
    def setup_method(self):
        # Create a fresh test directory and initialize a clean test JSON file before each test
        os.makedirs(test_dir, exist_ok=True)
        with open(test_file_path, "w") as file:
            json.dump(initial_test_data, file)

    def teardown_method(self):
        # Remove the test directory and its contents after each test
        if os.path.exists(test_dir):
            for filename in os.listdir(test_dir):
                file_path = os.path.join(test_dir, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            os.rmdir(test_dir)

    def test_deserialize_data(self):
        # Test reading data from file and saving that in JsonDataHandler class
        data_handler = JsonDataHandler(test_file_path)
        assert data_handler.sentences == initial_test_data["sentences"]
        assert data_handler.words == initial_test_data["words"]

    def test_add_sentence(self):
        # Test adding a sentence and check if it's added correctly and triggers serialization
        data_handler = JsonDataHandler(test_file_path)
        data_handler.add_sentence("section3", "new_sentence")

        # Check if the sentence is added correctly
        assert data_handler.sentences["section3"] == ["new_sentence"]

        # Re-open the file and check if the data matches the updated data
        with open(test_file_path, "r") as file:
            data = json.load(file)
        assert data["sentences"] == data_handler.get_sentences()

    def test_add_bulk_sentences(self):
        # initialize data handler
        data_handler = JsonDataHandler(test_file_path)

        # add
        section = "section3"
        sentences_to_add = ["sentence one", "sentences two"]
        data_handler.add_bulk_sentences(section, sentences_to_add)

        # Check if sentences were added
        assert data_handler.get_sentence_section(section) == sentences_to_add

        # Re-open the file and check if the data matches the updated data
        with open(test_file_path, "r") as file:
            data = json.load(file)
        assert data["sentences"][section] == data_handler.get_sentence_section(section)

    def test_add_word(self):
        # Test adding a word and check if it's added correctly and triggers serialization
        data_handler = JsonDataHandler(test_file_path)
        data_handler.add_word("section4", "new_word")

        # Check if the word is added correctly
        assert data_handler.words["section4"] == ["new_word"]

        # Re-open the file and check if the data matches the updated data
        with open(test_file_path, "r") as file:
            data = json.load(file)
        assert data["words"] == data_handler.get_words()

    def test_remove_sentence(self):
        # Test removing a sentence and check if it's removed correctly and triggers serialization
        data_handler = JsonDataHandler(test_file_path)
        data_handler.remove_sentence("section1", "sentence1")

        # Check if the sentence is removed correctly
        assert "sentence1" not in data_handler.sentences["section1"]

        # Re-open the file and check if the data matches the updated data
        with open(test_file_path, "r") as file:
            data = json.load(file)
        assert data["sentences"] == data_handler.get_sentences()

    def test_remove_word(self):
        # Test removing a word and check if it's removed correctly and triggers serialization
        data_handler = JsonDataHandler(test_file_path)
        data_handler.remove_word("section2", "word1")

        # Check if the word is removed correctly
        assert "word1" not in data_handler.words["section2"]

        # Re-open the file and check if the data matches the updated data
        with open(test_file_path, "r") as file:
            data = json.load(file)
        assert data["words"] == data_handler.get_words()

    def test_get_n_random_sentences_from_section(self):
        # Test getting a list of n randomly selected sentences from a section
        data_handler = JsonDataHandler(test_file_path)
        section_name = "section1"
        n = 1  # Number of sentences to retrieve
        random_sentences = data_handler.get_n_random_sentences_from_section(
            section_name, n
        )

        # Check if the result is a list
        assert isinstance(random_sentences, list)

        # Check if the number of retrieved sentences is correct
        assert len(random_sentences) == n

        # Check if the retrieved sentences are within the specified section
        for sentence in random_sentences:
            assert sentence in data_handler.sentences.get(section_name, [])

    def test_get_n_random_words_from_section(self):
        # Test getting a list of n randomly selected words from a section
        data_handler = JsonDataHandler(test_file_path)
        section_name = "section2"
        n = 2  # Number of words to retrieve
        random_words = data_handler.get_n_random_words_from_section(section_name, n)

        # Check if the result is a list
        assert isinstance(random_words, list)

        # Check if the number of retrieved words is correct
        assert len(random_words) == n

        # Check if the retrieved words are within the specified section
        for word in random_words:
            assert word in data_handler.words.get(section_name, [])
