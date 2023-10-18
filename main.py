import sys
from PyQt6.QtWidgets import QApplication
from src.window import Window
from src.main_controller import MainController

if __name__ == "__main__":
    app = QApplication([])
    app_window = Window()
    app_controller = MainController(app_window)
    app_window.show()
    sys.exit(app.exec())
