from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QToolBar


class MainToolbar(QToolBar):
    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)
        self.setIconSize(QSize(16, 16))

        # Add actions to the toolbar
        self.init_actions()

    def init_actions(self):
        button_action = QAction(QIcon("bug.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.setCheckable(True)
        button_action.setShortcut("Ctrl+p")  # Keyboard shortcut
        self.addAction(button_action)

        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your second button")
        button_action2.setCheckable(True)
        self.addAction(button_action2)

        # Add a separator and other widgets to the toolbar if needed
        self.addSeparator()
