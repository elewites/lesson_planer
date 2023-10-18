# library imports
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QComboBox,
    QMessageBox,
    QLabel,
)

WINDOW_H = 600
WINDOW_W = 800


class Window(QMainWindow):
    """
    Main window class for Lesson Planner application.

    Attributes:
    - m_central_widget (QWidget): Central widget
    - m_main_layout (QVBoxLayout): Main layout
    - m_upload_sentences_button (QPushButton): Upload button
    - m_upload_sentences_combo (QComboBox): Combo box for selection section to upload sentences
    - m_select_random_sentences_button (QPushButton): Select random sentences button
    - m_select_random_sentences_combo (QComboBox): Combo box for selecting the section for random selection
    - m_select_random_sentences_quantity_combo (QComboBox): Combo box for selecting quantity of random selection
    - m_view_selected_sentences_button (QPushButton): Button to view the sentences user has selected so far
    - m_view_database_sentences_button (QPushButton): View all database sentences button
    - m_print_selection_to_word_document_button (QPushButton): Print selection to Word Document button
    - m_sentences_display (QTextEdit): Text display for sentences
    """

    def __init__(self):
        """Initializes window"""
        super().__init__(parent=None)
        # set window settings
        self.__set_window_settings()
        # create central widget
        self.__add_central_widget()
        # add layout to central widget
        self.__add_main_layout()

        # add instructions
        self._instructions = (
            "<b>Instructions:</b> <br><br>"
            "<b>View Database</b>: displays sentences in database grouped by section.<br>"
            "<b>Click to Upload Sentences</b>: uploads sentences to database.<br>"
            "---> Input sentences in text box below seperated by punctuation, then specify section for upload.<br>"
            "---> You can upload sentences by bulk to a section. e.g. This is sentence. Now add this second sentence<br>"
            "<b>Click to Get Random Sentences</b>: adds specified <i>#</i> of random sentences from specified <i>section</i> to <i>your selection</i><br>"
            "---> Must populate your database first for sentences to become available. <br>"
            "<b>View My Selection</b>: prints <i>your selection</i> to screen<br>"
            "---> You can add multiple times to <i>your selection</i> before printing to word document<br>"
            "<b>Print Selection to Word Document</b>: prints <i>your selection</i> to word document"
        )

        self.__add_instructions()

        # add sentences button panel
        self.__add_button_panel_sentences()
        # add display for sentences
        self.__add_display_sentences()

    # GENERIC RE-USABLE FUNCTIONS FOR CREATING Widgets
    def __create_vertical_layout(self, parent: QWidget | None) -> QVBoxLayout:
        """Returns a vertical layout"""
        return QVBoxLayout(parent)

    def __create_horizontal_layout(self, parent: QWidget | None) -> QHBoxLayout:
        """Returns a horizontal layout"""
        return QHBoxLayout(parent)

    def __create_button(self, parent: QWidget | None, label: str) -> QPushButton:
        """Returns a button"""
        return QPushButton(label, parent)

    def __create_input(self, parent: QWidget | None) -> QTextEdit:
        """Return a text input"""
        return QTextEdit(parent)

    def __create_combo(self, parent: QWidget | None) -> QTextEdit:
        "Return a qcombo box"
        return QComboBox(parent)

    # SETUP FUNCTIONS
    def __set_window_settings(self) -> None:
        """Set window settings"""
        self.setWindowTitle("Lesson Planner")
        self.setFixedSize(WINDOW_W, WINDOW_H)

    def __add_central_widget(self) -> None:
        """Adds a central widget to this"""
        self.m_central_widget = QWidget(self)
        self.setCentralWidget(self.m_central_widget)

    def __add_main_layout(self) -> None:
        """Add vertical box layout to central widget"""
        self.m_main_layout = self.__create_vertical_layout(self.m_central_widget)
        self.m_central_widget.setLayout(self.m_main_layout)

    def __add_instructions(self) -> None:
        self.m_instructions = QLabel(self._instructions, self.m_central_widget)
        self.m_main_layout.addWidget(self.m_instructions)

    def __add_button_panel_sentences(self) -> None:
        """Adds a button panel to handle sentences"""
        # panel one
        panel_one: QHBoxLayout = self.__create_horizontal_layout(self.m_central_widget)
        # panel two
        panel_two: QHBoxLayout = self.__create_horizontal_layout(self.m_central_widget)
        # panel three
        panel_three: QHBoxLayout = self.__create_horizontal_layout(
            self.m_central_widget
        )

        # upload functionality
        self.m_upload_sentences_button = self.__create_button(
            self.m_central_widget, "Click to Upload Sentences:"
        )
        self.m_upload_sentences_combo = self.__create_combo(self.m_central_widget)
        self.m_upload_sentences_combo.addItem("Select Section")

        # random selection functionality
        self.m_select_random_sentences_button = self.__create_button(
            self.m_central_widget, "Click to Get Random Sentences:"
        )
        self.m_select_random_sentences_section_combo = self.__create_combo(
            self.m_central_widget
        )
        self.m_select_random_sentences_section_combo.addItem("Select Section")
        self.m_select_random_sentences_quantity_combo = self.__create_combo(
            self.m_central_widget
        )
        self.m_select_random_sentences_quantity_combo.addItem("Quantity")

        # view selection functionality
        self.m_view_selected_sentences_button = self.__create_button(
            self.m_central_widget, "View My Selection"
        )

        # view database functionality
        self.m_view_database_sentences_button = self.__create_button(
            self.m_central_widget, "View Database"
        )

        # print selection functionality to word document
        self.m_print_selection_to_word_document_button = self.__create_button(
            self.m_central_widget, "Print Selection to Word Document"
        )

        # add widgets and panels to window
        panel_one.addWidget(self.m_upload_sentences_button)
        panel_one.addWidget(self.m_upload_sentences_combo)
        panel_two.addWidget(self.m_select_random_sentences_button)
        panel_two.addWidget(self.m_select_random_sentences_section_combo)
        panel_two.addWidget(self.m_select_random_sentences_quantity_combo)
        panel_three.addWidget(self.m_view_selected_sentences_button)
        panel_three.addWidget(self.m_view_database_sentences_button)
        self.m_main_layout.addLayout(panel_one)
        self.m_main_layout.addLayout(panel_two)
        self.m_main_layout.addLayout(panel_three)
        self.m_main_layout.addWidget(self.m_print_selection_to_word_document_button)

    def __add_display_sentences(self) -> None:
        """Adds a display for sentences"""
        self.m_sentences_display = self.__create_input(self.m_central_widget)
        self.m_main_layout.addWidget(self.m_sentences_display)

    def m_display_message(self, title: str, message: str) -> None:
        """Add a display message to window"""
        message_box = QMessageBox(self)
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.exec()
