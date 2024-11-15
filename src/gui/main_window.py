import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from src.gui.toolbar import MainToolbar
from src.gui.layout import CentralLayout
from src.gui.menu import MainMenu
from qt_material import apply_stylesheet


def apply_qss(self):
    try:
        apply_stylesheet(self, theme="dark_teal.xml")
    except FileNotFoundError:
        print("Error applying stylesheet!")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Video Uploader')
        self.resize(400, 300)

        # set up central layout
        self.setCentralWidget(CentralLayout())

        # set up toolbar
        toolbar = MainToolbar(self)
        self.addToolBar(toolbar)

        # set up menu
        menubar = MainMenu(self)
        self.setMenuBar(menubar)

        # apply style sheet
        apply_qss(self)

    def close_app(self):
        print("Closing...")
        sys.exit()

    def close_event(self, event):
        self.close_app()
        event.accept()
