from PyQt6.QtWidgets import QMessageBox
from typing import Dict, List
import os

# serializer
from .serializer import Serializer

# data handlers
from .data_handlers.json_data_handler import JsonDataHandler
from .data_handlers.user_selection_data_handler import UserSelectionDataHandler

# window
from .window import Window

# controllers
from .upload_sentences_controller import UploadSentencesController
from .random_selection_controller import RandomSelectionController
from .view_user_selection_controller import ViewUserSelectionController
from .view_all_stored_data_controller import ViewAllStoredDataController
from .print_to_word_document_controller import PrintWordDocumentController


JSON_FILE_PATH = "./data/data.json"
WORD_DOCUMENT_PATH = "./output/lesson.docx"


class MainController:
    """
    A controller class for managing the application logic.

    Parameters:
        app_window (QWidget): The main window of the application.
    """

    def __init__(self, app_window: Window):
        #  reference to window
        self.window = app_window
        # json handler
        self._json_handler = JsonDataHandler(Serializer.get_full_path(JSON_FILE_PATH))
        # user selection handler
        self._user_selection_handler = UserSelectionDataHandler()

        # controller for uploading sentences functionality
        self._upload_sentences_controller = UploadSentencesController(
            self._json_handler,
            self.window.m_upload_sentences_button,
            self.window.m_upload_sentences_combo,
            self.window.m_sentences_display,
            self.window.m_display_message,
        )

        # controller for random selection functionality
        self._random_selection_controller = RandomSelectionController(
            self._json_handler,
            self._user_selection_handler,
            self.window.m_select_random_sentences_button,
            self.window.m_select_random_sentences_section_combo,
            self.window.m_select_random_sentences_quantity_combo,
            self.window.m_sentences_display,
            self.window.m_display_message,
        )

        # controller for viewing user selection
        self._view_user_selection_controller = ViewUserSelectionController(
            self.window.m_view_selected_sentences_button,
            self.window.m_sentences_display,
            self._user_selection_handler,
        )

        # controller for viewing all stored data
        self._view_all_stored_data_controller = ViewAllStoredDataController(
            self.window.m_view_database_sentences_button,
            self.window.m_sentences_display,
            self._json_handler,
        )

        # controller for printing to word document
        self._print_to_word_document_controller = PrintWordDocumentController(
            self.window.m_print_selection_to_word_document_button,
            self._user_selection_handler,
            Serializer.get_full_path(WORD_DOCUMENT_PATH)
        )

        # REGISTER OBSERVERS for json_handler
        self._json_handler.add_observer(self._random_selection_controller)
