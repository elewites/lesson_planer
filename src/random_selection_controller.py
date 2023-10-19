from PyQt6.QtWidgets import (
    QPushButton,
    QTextEdit,
    QComboBox,
)
from typing import Dict, List, Callable

# my modules import
from .controller_observer import Observer
from .data_handlers.json_data_handler import JsonDataHandler
from .data_handlers.user_selection_data_handler import UserSelectionDataHandler
from .window import Window

# CONSTANTS
SELECT_SECTION = "Select Section"
SELECT_QUANTITY = "Select Quantity"
NO_SENTENCES_AVAILABLE = "No Sentences Available"


class RandomSelectionController(Observer):
    def __init__(
        self,
        json_handler: JsonDataHandler,
        user_selection_handler: UserSelectionDataHandler,
        button: QPushButton,
        section_combo: QComboBox,
        quantity_combo: QComboBox,
        text: QTextEdit,
        display_message: Callable[["Window", str, str], None],
    ):
        self._json_handler: JsonDataHandler = json_handler
        self._user_selection_handler = user_selection_handler
        self._button = button
        self._section_combo = section_combo
        self._quantity_combo = quantity_combo
        self._text = text
        self._alert = display_message

        # temporary data holders for section and quantity
        self._section_selected = ""
        self._quantity_selected = 0

        # add event handlers
        self.__add_event_handlers()

        # initialize section combo
        self.__refresh_section_combo()

        # initialize quantity combo with zero since no section has been selected
        self.__refresh_quantity_combo(0)

    # OBSERVER FUNCTIONS
    def update(self, source_controller: JsonDataHandler) -> None:
        """
        Respond to a change initiated by an observed controller.

        This method is called when an observed controller notifies of changes.
        It checks if the source of the change is an instance of the `JsonDataHandler`
        and, if so, refreshes the section combo to react to the change.

        Parameters:
            source_controller (JsonDatHandler): The controller that initiated the change.

        Returns:
            None
        """
        if isinstance(source_controller, JsonDataHandler):
            # refresh combos since data has changed
            print("observer")
            self.__refresh_section_combo()
            self.__refresh_quantity_combo(0)

    # CLASS RELATED FUNCTIONS
    def __add_event_handlers(self) -> None:
        """Add event handlers to button and combos"""
        self._button.clicked.connect(self.__button_handler)
        self._section_combo.activated.connect(self.__section_combo_handler)
        self._quantity_combo.activated.connect(self.__quantity_combo_handler)

    def __button_handler(self) -> None:
        # print("button handler priints: " + str(self._quantity_selected))
        # print("button handler pritns :" + self._section_selected)

        if self._section_selected == "" or self._quantity_selected == 0:
            if self._section_selected == "":
                self._alert("Alert", SELECT_SECTION)
            if self._quantity_selected == 0:
                self._alert("Alert", SELECT_QUANTITY)
            return None

        # if section and quantity have been selected
        random_selection = self._json_handler.get_n_random_sentences_from_section(
            self._section_selected, self._quantity_selected
        )
        # print(random_selection)

        # clear selection if user had added to this section before
        if self._section_selected in self._user_selection_handler.sentences:
            self._user_selection_handler.sentences[self._section_selected].clear()

        # BUG: find bug in commented code below
        # update user_selection_handler
        # self._user_selection_handler.add_bulk_sentences(
        #     self._section_selected, random_selection
        # )
        # TODO: alternative code for the code above so far
        for sentence in random_selection:
            self._user_selection_handler.add_sentence(self._section_selected, sentence)
        # for debugging purposes
        print(self._user_selection_handler.sentences)
        print(self._json_handler.sentences)

        # display selected sentences in text input
        display_selection = (
            "<b>Your Selection</b><br><br>"
            + self._user_selection_handler.format_all_sentences()
        )
        self._text.setText(display_selection)

        # refresh combos
        # self.__refresh_quantity_combo()
        # self.__section_combo_init()

    def __refresh_section_combo(self) -> None:
        """Adds sections that are available to the combo"""

        # clear the selected section
        self._section_selected = ""
        # Clear existing items in combo
        self._section_combo.clear()

        # add placeholder at top of combo
        self._section_combo.addItem(SELECT_SECTION)

        # get number of sections available
        sentences: Dict[str, List[str]] = self._json_handler.get_sentences()
        N = len(sentences)

        # populate the sections available for the section combo
        for i in range(N):
            self._section_combo.addItem(str(i + 1))

    def __section_combo_handler(self, index) -> None:
        """Event handler for section combo"""
        self._quantity_selected = 0
        # get the user selected section and parse
        section = self._section_combo.itemText(index)

        # if no selection has been made return
        if section == SELECT_SECTION:
            # print(SELECT_SECTION)
            self._section_selected = ""
            self.__refresh_quantity_combo(0)
            return None

        # update section name
        self._section_selected = "section" + section

        # refresh quantity combo with length of selected section
        section_length = len(
            self._json_handler.get_sentence_section(self._section_selected)
        )
        self.__refresh_quantity_combo(section_length)
        # # also set selected quantity to zero
        # self._quantity_selected = 0

        return None

    def __refresh_quantity_combo(self, section_length: int) -> None:
        """Adds quantities availabe for selection based on section_length"""
        # Clear existing items in combo
        self._quantity_combo.clear()

        # add placeholder at top of combo
        self._quantity_combo.addItem(SELECT_QUANTITY)

        # add this placeholder if no section has been selected or no sentences available
        if section_length == 0:
            if self._section_selected == "":
                # self._quantity_selected = 0
                return None
            else:
                self._quantity_combo.addItem(NO_SENTENCES_AVAILABLE)
                # self._quantity_selected = 0
                return None

        # populate the sections available for the section combo.
        # user can request the number of random sentences to request.
        for i in range(section_length):
            self._quantity_combo.addItem(str(i + 1) + " random sentences")

    def __quantity_combo_handler(self, index) -> None:
        """Event handler for quantity combo"""
        quantity = self._quantity_combo.itemText(index)
        if quantity == NO_SENTENCES_AVAILABLE:
            self._quantity_selected = 0
            return None
        if quantity == SELECT_QUANTITY:
            self._quantity_selected = 0
            return None
        # parse and save quantity
        digits = ""
        for char in quantity:
            if char.isdigit():
                digits += char
            else:
                break

        self._quantity_selected = int(digits)
