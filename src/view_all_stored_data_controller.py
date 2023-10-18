from PyQt6.QtWidgets import QPushButton, QTextEdit
from .data_handlers.json_data_handler import JsonDataHandler


class ViewAllStoredDataController:
    def __init__(self, button: QPushButton, text: QTextEdit, handler: JsonDataHandler):
        self._button = button
        self._text = text
        self._handler = handler

        # add event handlers
        self.__add_event_handlers()

    def __add_event_handlers(self) -> None:
        self._button.clicked.connect(self.__button_handler)

    def __button_handler(self) -> None:
        print(self._handler.sentences)
        self._text.setText(self._handler.format_all_sentences())
