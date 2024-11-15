import sys
from PyQt6.QtWidgets import QApplication, QWidget
from src.gui.main_window import MainWindow


def main():
    # Create an application instance
    app = QApplication(sys.argv)
    # window
    window = MainWindow()
    # logic = MainLogic(window)
    window.show()
    # Close app
    app.exec()


if __name__ == "__main__":
    main()
