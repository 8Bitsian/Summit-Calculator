# Standard Library Imports
import sys, os
from pathlib import Path

# Third-party Imports
from PyQt6.QtWidgets import QMainWindow, QWidget, QDialog

# Locacl Library Imports
import gui.controllers.main_controller

from gui.dialogs.settings_dialog import setting_window

from gui.widgets.images import load_icon
from gui.widgets.labels import create_app_title
from gui.widgets.lineedits import create_calc_input
from gui.widgets.buttons import (create_mode_switch,
                                 create_settings_button,
                                 create_numpad_button)

from gui.layouts.main_layout import main_layout

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Basic window description
        self.setWindowTitle("Summit")
        self.setMinimumSize(400, 800)
        # Image sourced from https://fonts.google.com/icons
        self.setWindowIcon(loac_icon("summit.svg"))

        # Create a generic widget for the layout manager
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create main window title label object
        self.main_title = create_app_title(central_widget)
        
        # Create theme mode button object
        self.mode_button = create_mode_switch(central_widget)
        self.mode_button.clicked.connect(
            lambda checked=False: on_mode_switch(self)
        )

        # Create settings button object
        self.settings_button = create_settings_button(central_widget)
        self.settings_button.clicked.connect(
            lambda checked=False: open_settings(self)
        )

        # Create numpad button objects
        self.numpad_button = create_settings_button(central_widget)
        self.numpad_button.clicked.connect(
            lambda checked=False: input_numpad(self)
        )

        # Create dictionary of main widgets
        main_widgets = {
            "main_title": self.main_title,
            "mode_button": self.mode_button,
            "setting_button": self.settings_button,
            "numpad_button": self.numpad_button,
        }

        # Apply the main layout manager to main widget dictionary
        create_main_layout(central_widget, main_widgets)