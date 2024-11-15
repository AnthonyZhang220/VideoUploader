import sys
from PyQt6.QtWidgets import QMenuBar, QMessageBox, QApplication
from PyQt6.QtGui import QAction


class MainMenu(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Add menus
        self.file_menu = self.addMenu("File")
        self.help_menu = self.addMenu("Help")

        # Add actions to menus
        self.init_actions()

    def init_actions(self):
        # File Menus action
        # Add submenu if necessary
        import_submenu = self.file_menu.addMenu("Import")
        import_submenu_action = QAction("Import from your computer", self)
        import_submenu.addAction(import_submenu_action)

        exit_action = QAction("Close", self)
        exit_action.setStatusTip("Close Window")
        exit_action.triggered.connect(self.close_app)
        self.file_menu.addAction(exit_action)

        # Help Menu action
        version_action = QAction("Current Version", self)
        version_action.setStatusTip("Current Version is 1")
        version_action.triggered.connect(self.show_version)
        self.help_menu.addAction(version_action)

    def close_app(self):
        """
        This method handles the Close action.
        It is called when the user selects 'Close' from the File menu.
        You can add any cleanup logic here (e.g., saving data, logging out, etc.).
        """
        print("Performing cleanup before exiting...")

        # Example: Show a confirmation dialog before quitting
        reply = QMessageBox.question(self, "Confirm Exit", "Are you sure you want to exit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()  # Exit the application
        else:
            print("Exit canceled.")

    def show_version(self):
        """
        Display the current version of the application in a message box.
        This is called when the user selects 'Current Version' from the Help menu.
        """
        version = "1.0"
        QMessageBox.information(self, "Version", f"Current Version: {version}")
