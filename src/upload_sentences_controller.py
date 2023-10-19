import re
from PyQt6.QtWidgets import (
    QPushButton,
    QTextEdit,
    QComboBox,
)
from typing import Dict, List, Callable

# my modules imports
from .window import Window
from .data_handlers.json_data_handler import JsonDataHandler
from .controller_observer import Observer


class UploadSentencesController:
    """
    Controller class for uploading sentences.

    Args:
        handler (JsonDataHandler): An instance of the JsonDataHandler class.
        button (QPushButton): The button used to trigger sentence upload.
        section (QComboBox): The combo box for selecting a section.
        text (QTextEdit): The text editor for entering sentences.
        display_message (Callable[['Window', str, str], None]): A function for displaying messages.

    Attributes:
        _handler (JsonDataHandler): The JSON data handler instance.
        _button (QPushButton): The upload button.
        _combo (QComboBox): The section selection combo box.
        _text (QTextEdit): The text editor for entering sentences.
        _alert (Callable[['Window', str, str], None]): A function for displaying messages.
        _sentences_to_upload (list): Temporary data holder for sentences to upload.
        _section (str): Temporary data holder for the selected section.
    """

    def __init__(
        self,
        handler: JsonDataHandler,
        button: QPushButton,
        section: QComboBox,
        text: QTextEdit,
        display_message: Callable[["Window", str, str], None],
    ):
        self._handler = handler
        self._button = button
        self._combo = section
        self._text = text
        self._alert = display_message

        # temporary data holders
        self._sentences_to_upload = []
        self._section = ""

        # add even handlers
        self.__add_event_handlers()

        # refresh combo upon initialization
        self.__refesh_combo()

        # list of observers
        # self._observers = []

    def __add_event_handlers(self) -> None:
        """Add event handlers to button, combo and text"""
        self._button.clicked.connect(self.__button_handler)
        self._combo.activated.connect(self.__combo_handler)
        self._text.textChanged.connect(self.__text_handler)

    def __button_handler(self) -> None:
        """Uploads the sentences that user has inputted into json file"""
        if self._section == "":
            self._alert("Alert", "Selection Section First!")
            return None
        if self._sentences_to_upload == []:
            self._alert("Alert", "Input Sentences to Upload First")
            return None

        # add sentences
        self._handler.add_bulk_sentences(self._section, self._sentences_to_upload)

        # refresh the combo in case a new section was added
        self.__refesh_combo()

        # clear the text input.
        self._text.clear()

        # clear section
        self._section = ""
        return None

    def __refesh_combo(self) -> None:
        """Adds sections that are available to the combo"""
        # Clear existing items in combo
        self._combo.clear()

        # add placeholder at top of combo
        self._combo.addItem("Select Section")

        # get number of sections available
        sentences: Dict[str, List[str]] = self._handler.get_sentences()
        N = len(sentences)
        for i in range(N):
            self._combo.addItem(str(i + 1))
        self._combo.addItem("Add Section: " + str(N + 1))

    def __combo_handler(self, index) -> None:
        """Event handler for combo"""
        # get the user selected section and parse
        section = self._combo.itemText(index)
        if section == "Select Section":
            print("no selection")
            section = ""
            return None
        if "Add" in section:
            section = "section" + section[-1]
        else:
            section = "section" + section
        self._section = section
        # print(section)
        return None

    def __text_handler(self) -> None:
        """Save list of sentences from user input."""
        text = self._text.toPlainText()

        # Use regular expressions to split the text into sentences
        sentences: str = re.split(r"[.!?]", text)  # Split at '.', '!', or '?'

        # Remove any leading/trailing whitespace from each sentence
        sentences: List[str] = [
            sentence.strip() for sentence in sentences if sentence.strip()
        ]

        # print(sentences)
        self._sentences_to_upload = sentences
