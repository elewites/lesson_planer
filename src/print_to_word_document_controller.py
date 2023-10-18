from PyQt6.QtWidgets import QPushButton

# data handlers
from .data_handlers.user_selection_data_handler import UserSelectionDataHandler


class PrintWordDocumentController:
    def __init__(
        self, button: QPushButton, handler: UserSelectionDataHandler, filepath: str
    ):
        """
        Initialize a controller for printing a Word document with selected data.

        Args:
            button (QPushButton): The button that triggers the document printing.
            handler (UserSelectionDataHandler): The data handler to extract data from.
            filepath (str): The file path where the Word document will be saved.
        """
        self._button = button
        self._handler = handler
        self._path = filepath

        self._add_event_handlers()

    def _add_event_handlers(self):
        """
        Add event handlers to the button's click event.
        """
        self._button.clicked.connect(self._button_handler)

    def _button_handler(self):
        """
        Handle the button click event.

        When the button is clicked, this method prints the selected data to a Word document
        using the data handler and specified file path.
        """
        print("handled")
        self._handler.write_selection_to_docx(self._path)
