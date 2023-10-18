from PyQt6.QtWidgets import QPushButton, QTextEdit
from .data_handlers.user_selection_data_handler import UserSelectionDataHandler


class ViewUserSelectionController:
    """
    A controller class for viewing user-selected sentences.

    Parameters:
        button (QPushButton): The button used to trigger sentence viewing.
        text (QTextEdit): The QTextEdit widget for displaying sentences.
        user_selection_data_handler (UserSelectionDataHandler):
            The data handler for managing user-selected sentences.

    Methods:
        __init__: Initialize the controller with necessary components.
        __add_event_handlers: Add event handlers for button clicks.
        __button_handler: Handle button clicks to display user-selected sentences.
    """

    def __init__(
        self,
        button: QPushButton,
        text: QTextEdit,
        user_selection_data_handler: UserSelectionDataHandler,
    ):
        """
        Initialize the ViewUserSelectionController.

        Args:
            button (QPushButton): The button used to trigger sentence viewing.
            text (QTextEdit): The QTextEdit widget for displaying sentences.
            user_selection_data_handler (UserSelectionDataHandler):
                The data handler for managing user-selected sentences.

        This constructor sets up the controller with the provided components and adds event handlers.
        """
        self._button = button
        self._text = text
        self._user_selection_data_handler = user_selection_data_handler

        # Add event handlers
        self.__add_event_handlers()

    def __add_event_handlers(self) -> None:
        """
        Add event handlers for button clicks.

        This method connects the button's 'clicked' signal to the 'button_handler' method.
        """
        self._button.clicked.connect(self.__button_handler)

    def __button_handler(self) -> None:
        """
        Handle button clicks to display user-selected sentences.

        When the button is clicked, this method sets the QTextEdit widget's text to
        display user-selected sentences by formatting and retrieving data from the data handler.
        """
        display_selection = (
            "<b>Your Selection</b><br><br>"
            + self._user_selection_data_handler.format_all_sentences()
        )

        self._text.setText(display_selection)
