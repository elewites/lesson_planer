from typing import Dict, List
from ..controller_observer import ControllerObserver


# BASE CLASS FOR data handler classess
class BaseDataHandler:
    def __init__(self):
        """
        Initialize the BaseDataHandler with empty dictionaries for sentences and words.
        """
        self.sentences: Dict[str, List[str]] = {}
        self.words: Dict[str, List[str]] = {}

        # observers
        self._observers = []

    # OBSERVER FUNCTIONS
    def add_observer(self, observer: ControllerObserver) -> None:
        """
        Add an observer to the list of observers.

        Parameters:
        observer (ControllerObserver): An instance of a controller that observes changes in this controller.
        """
        self._observers.append(observer)

    def _notify_observers(self) -> None:
        """
        Notify all registered observers of a change in this controller.

        This method iterates through the list of registered observers and calls the
        `update` method on each observer, passing a reference to this controller as
        the `source_controller` to inform observers about the source of the change.
        """
        for observer in self._observers:
            observer.update(self)

    def add_sentence(self, section: str, sentence: str):
        """
        Add a sentence to the specified section.

        :param section: The section name.
        :param sentence: The sentence to add.
        """
        if section in self.sentences:
            self.sentences[section].append(sentence)
            # notify observers of data change
            self._notify_observers()
        else:
            self.sentences[section] = [sentence]
            # notify observers of data change
            self._notify_observers()

    def add_bulk_sentences(self, section: str, sentences_to_add: List[str]) -> None:
        """
        Add a list of sentences to a specific section.

        Args:
            section (str): The section to which the sentences will be added.
            sentences_to_add (List[str]): A list of sentences to add to the section.

        If the specified section already exists, the new sentences are appended to the existing list of sentences.
        If the section does not exist, a new section is created with the provided sentences.
        After adding or appending the sentences, this method notifies observers of the data change.
        """

        if section in self.sentences:
            self.sentences[section].extend(sentences_to_add)
            # Notify observers of data change
            self._notify_observers()
        else:
            self.sentences[section] = sentences_to_add
            # Notify observers of data change
            self._notify_observers()

    def add_word(self, section: str, word: str):
        """
        Add a word to the specified section.

        :param section: The section name.
        :param word: The word to add.
        """
        if section in self.words:
            self.words[section].append(word)
            # notify observers of data change
            self._notify_observers()
        else:
            self.words[section] = [word]
            # notify observers of data change
            self._notify_observers()

    def remove_sentence(self, section: str, sentence: str):
        """
        Remove a sentence from the specified section.

        :param section: The section name.
        :param sentence: The sentence to remove.
        """
        if section in self.sentences and sentence in self.sentences[section]:
            self.sentences[section].remove(sentence)
            # notify observers of data change
            self._notify_observers()

    def remove_word(self, section: str, word: str):
        """
        Remove a word from the specified section.

        :param section: The section name.
        :param word: The word to remove.
        """
        if section in self.words and word in self.words[section]:
            self.words[section].remove(word)
            # notify observers of data change
            self._notify_observers()

    def get_sentence_section(self, section: str) -> List[str]:
        """
        Get a list of sentences for the specified section.

        :param section: The section name.
        :return: A list of sentences in the section.
        """
        return self.sentences.get(section, [])

    def get_word_section(self, section: str) -> List[str]:
        """
        Get a list of words for the specified section.

        :param section: The section name.
        :return: A list of words in the section.
        """
        return self.words.get(section, [])

    def get_sentences(self) -> Dict[str, List[str]]:
        """
        Get sentences

        :return: A list of sentences.
        """
        return self.sentences

    def get_words(self) -> Dict[str, List[str]]:
        """
        Get words

        :return: a list of words.
        """
        return self.words

    def get_formatted_sentences_by_section(self, section: str) -> str:
        """
        Get formatted sentences for a specific section, including a bold section header.

        Args:
            section (str): The section for which sentences will be retrieved and formatted.

        Returns:
            str: A formatted string with HTML tags to make the section bold and separate sentences with line breaks.

        This method retrieves sentences from the specified section, formats them as an HTML string
        with the section name in bold and each sentence on a new line, and returns the formatted text.
        """
        sentences = self.get_sentence_section(section)
        formatted_list = "<br>".join(
            sentences
        )  # Use <br> to separate sentences for line breaks

        # Use HTML formatting to make the section string bold
        formatted_section = f"<b>{section}</b>"

        # Combine the section and the formatted list using <br> for line breaks
        formatted_text = f"{formatted_section}<br>{formatted_list}"

        return formatted_text + "<br><br>"

    def format_all_sentences(self) -> str:
        """
        Format all sentences in the 'sentences' attribute with section names in bold.

        Returns:
            str: A formatted string with HTML tags that include section names in bold
                 and list sentences under each section.
        """

        formatted_text = ""

        # Iterate through the sections and their associated sentences
        for section, sentences in self.sentences.items():
            # Use HTML formatting to make the section string bold
            formatted_section = f"<b>{section}</b>"

            # Join the sentences with line breaks
            formatted_sentences = "<br>".join(sentences)

            # Combine the section and the formatted sentences
            section_text = f"{formatted_section}<br>{formatted_sentences}"

            # Append the formatted section and sentences to the result
            formatted_text += section_text + "<br><br>"

        if len(self.sentences) == 0:
            return formatted_text + "No selections so far... \n"

        return formatted_text
