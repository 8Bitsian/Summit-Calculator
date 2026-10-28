# Standard Library Imports
import sys

# Third-party Imports
from PyQt6.QtWidgets import QApplication

# Locacl Library Imports
from gui.app_theme import load_fonts, load_stylesheet
from gui.windows.main_window import main_window

def run():
    """app.py starts the Summit calcualtor application setup."""
    app = QApplication(sys.argv)

    load_fonts()
    load_stylesheet(app)

    window = main_window()
    window.show()

    return app.exec()