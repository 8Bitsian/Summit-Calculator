# Standard Library Imports
import sys

# Third-party Imports
from PyQt6.QtWidgets import QApplication

# Locacl Library Imports
from gui.app_theme import load_fonts, load_stylesheet
from gui.windows.main_window import main_window

def main():
    """A calculator combining basic/advanced arithmetic, equation solving, statistics, and unit conversions."""
    app = QApplication(sys.argv)

    load_fonts()
    load_stylesheet(app)

    window = main_window()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    print(f"Running {__name__}\n")
    main()
    print("Closing program...")