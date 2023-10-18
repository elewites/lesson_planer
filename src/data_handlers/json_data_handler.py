import random
from typing import List

from ..serializer import Serializer
from .base_data_handler import BaseDataHandler


class JsonDataHandler(BaseDataHandler):
    """
    A data handler that manages data serialization and deserialization in JSON format.

    Args:
        file_path (str): The path to the JSON data file.

    Attributes:
        file_path (str): The file path for JSON data storage.

    Methods:
        serialize_data: Serialize the data and write it to the JSON file.
        deserialize_data: Read and deserialize data from the JSON file.
        add_sentence: Add a sentence to the data and update the JSON file.
        add_word: Add a word to the data and update the JSON file.
        remove_sentence: Remove a sentence from the data and update the JSON file.
        remove_word: Remove a word from the data and update the JSON file.
    """

    def __init__(self, file_path: str):
        """
        Initialize the JsonDataHandler instance.

        Args:
            file_path (str): The path to the JSON data file.

        This constructor also deserializes data from the JSON file.
        """
        super().__init__()
        self.file_path = file_path

        # Deserialize data from the file
        self.deserialize_data()

    def serialize_data(self):
        """
        Serialize the data and write it to the JSON file.

        This method serializes sentences and words data and writes it to the JSON file.
        """
        data = {"sentences": self.sentences, "words": self.words}
        Serializer.write_to_json_file(self.file_path, data)

    def deserialize_data(self):
        """
        Read and deserialize data from the JSON file.

        This method reads and deserializes data from the JSON file and populates the sentences and words attributes.
        """
        data = Serializer.read_from_json_file(self.file_path)
        self.sentences = data.get("sentences", {})
        self.words = data.get("words", {})

    def add_sentence(self, section: str, sentence: str):
        """
        Add a sentence to the data and update the JSON file.

        Args:
            section (str): The section to which the sentence belongs.
            sentence (str): The sentence to be added.

        This method adds a sentence to the data, calls the parent class method, and then serializes the updated data.
        """
        super().add_sentence(section, sentence)
        self.serialize_data()  # Serialize in-memory data after adding the sentence

    def add_word(self, section: str, word: str):
        """
        Add a word to the data and update the JSON file.

        Args:
            section (str): The section to which the word belongs.
            word (str): The word to be added.

        This method adds a word to the data, calls the parent class method, and then serializes the updated data.
        """
        super().add_word(section, word)
        self.serialize_data()  # Serialize in-memory data after adding the word

    # def add_bulk_sentences(self, section: str, sentences_to_add: List[str]) -> None:
    #     super().add_bulk_sentences(section, sentences_to_add)
    #     self.serialize_data()

    def add_bulk_sentences(self, section: str, sentences_to_add: List[str]) -> None:
        """
        Add a list of sentences to a specific section and serialize the data.

        Args:
            section (str): The section to which the sentences will be added.
            sentences_to_add (List[str]): A list of sentences to add to the section.

        This method extends the list of sentences in the specified section with the provided sentences and then serializes the updated data. If the section does not exist, a new section is created with the provided sentences. After adding or appending the sentences and serializing the data, this method ensures that the changes are saved.
        """
        print("added bulk")
        super().add_bulk_sentences(section, sentences_to_add)
        self.serialize_data()

    def remove_sentence(self, section: str, sentence: str):
        """
        Remove a sentence from the data and update the JSON file.

        Args:
            section (str): The section from which the sentence is to be removed.
            sentence (str): The sentence to be removed.

        This method removes a sentence from the data, calls the parent class method, and then serializes the updated data.
        """
        super().remove_sentence(section, sentence)
        self.serialize_data()  # Serialize in-memory data after removing the sentence

    def remove_word(self, section: str, word: str):
        """
        Remove a word from the data and update the JSON file.

        Args:
            section (str): The section from which the word is to be removed.
            word (str): The word to be removed.

        This method removes a word from the data, calls the parent class method, and then serializes the updated data.
        """
        super().remove_word(section, word)
        self.serialize_data()  # Serialize in-memory data after removing the word

    def get_n_random_sentences_from_section(self, section: str, n: int) -> List[str]:
        """
        Get a list of n randomly selected sentences from a specific section.

        Args:
            section (str): The section from which sentences will be selected.
            n (int): The number of sentences to retrieve.

        Returns:
            List[str]: A list of n randomly selected sentences from the specified section.
        """
        sentences_in_section = self.sentences.get(section, [])
        if n >= len(sentences_in_section):
            return sentences_in_section
        return random.sample(sentences_in_section, n)

    def get_n_random_words_from_section(self, section: str, n: int) -> List[str]:
        """
        Get a list of n randomly selected words from a specific section.

        Args:
            section (str): The section from which words will be selected.
            n (int): The number of words to retrieve.

        Returns:
            List[str]: A list of n randomly selected words from the specified section.
        """
        words_in_section = self.words.get(section, [])
        if n >= len(words_in_section):
            return words_in_section
        return random.sample(words_in_section, n)
