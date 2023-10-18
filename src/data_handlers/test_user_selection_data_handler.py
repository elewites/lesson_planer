import os
from docx import Document
from typing import Dict, List
from .user_selection_data_handler import UserSelectionDataHandler


class TestUserSelectionDataHandler:
    def setup_class(cls):
        cls.test_file_path = "test_document.docx"

    def teardown_class(cls):
        if os.path.exists(cls.test_file_path):
            os.remove(cls.test_file_path)

    def test_get_selection(self):
        data_handler = UserSelectionDataHandler()
        section_name = "section1"
        sentence = "This is a test sentence."
        word = "apple"

        # Add sentences and words
        data_handler.add_sentence(section_name, sentence)
        data_handler.add_word(section_name, word)

        # Call the get_selection method
        selection = data_handler.get_selection()

        # Check if the selection contains the added data
        selection["sentences"] == data_handler.get_sentences()
        selection["words"] == data_handler.get_words()

    def test_write_selection_to_docx(self):
        # Create a UserSelectionDataHandler instance
        data_handler = UserSelectionDataHandler()

        # Add test data
        data_handler.add_sentence("Section1", "Sentence 1")
        data_handler.add_sentence("Section1", "Sentence 2")
        data_handler.add_sentence("Section2", "Sentence 3")

        data_handler.add_word("Section1", "Word 10")
        data_handler.add_sentence("Section2", "Word 20")
        data_handler.add_word("Section3", "Word 1")
        data_handler.add_word("Section3", "Word 2")

        # Write the selection to a .docx file
        data_handler.write_selection_to_docx(self.test_file_path)

        # Check if the .docx file was created
        assert os.path.exists(self.test_file_path)

        # Load the document and check its content
        doc = Document(self.test_file_path)

        # Extract the content for further validation
        #content = [(element.text) for element in doc.element.body]

        # # Define expected content
        # expected_content = [
        #     ("Section1", "Heading1"),
        #     ("Sentence 1", "Normal"),
        #     ("Sentence 2", "Normal"),
        #     ("Section2", "Heading1"),
        #     ("Sentence 3", "Normal"),
        #     ("Word 10", "Normal"),
        #     ("Section3", "Heading1"),
        #     ("Word 20", "Normal"),
        #     ("Word 1", "Normal"),
        #     ("Word 2", "Normal"),
        # ]

        # # Check if the content matches the expected content
        # assert content == expected_content
