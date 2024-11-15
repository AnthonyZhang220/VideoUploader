from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QComboBox, QApplication, QFormLayout
from PyQt6.QtCore import Qt
from src.gui.forms.bilibili import BilibiliUploadForm
from src.gui.forms.douyin import DouyinUploadForm
from src.gui.forms.youtube import YoutubeUploadForm
from src.gui.progress import UploadProgress

platform_list = ["youtube", "douyin", "bilibili"]


class PlatformSelection(QWidget):
    def __init__(self):
        super().__init__()

        # Create layout and add widgets
        layout = QVBoxLayout()
        label = QLabel("Hello from Central Layout!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)


def platform_labels():
    # Return a list of platform names
    result = []
    for label in platform_list:
        result.append(label)
    return result


class CentralLayout(QWidget):
    def __init__(self):
        super().__init__()

        # Create layout and add widgets
        layout = QVBoxLayout()
        label = QLabel("Hello from Central Layout!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Create Dropdown menu for platform Selection
        dropdown = QComboBox()
        dropdown.addItems(platform_labels())
        dropdown_label = QLabel("Upload Platform")
        dropdown_label.setBuddy(dropdown)
        layout.addWidget(dropdown)

        # Create Upload Forms
        douyin_form = DouyinUploadForm()
        youtube_form = YoutubeUploadForm()
        bilibili_form = BilibiliUploadForm()
        layout.addWidget(douyin_form)
        layout.addWidget(youtube_form)
        layout.addWidget(bilibili_form)

        # Create widgets
        button = QPushButton("Click Me")
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)

        # Create progress bar
        progress = UploadProgress()
        layout.addWidget(progress)
        self.setLayout(layout)
        # self.change_form("douyin")

    # def change_form(self, name):
    #     # Clear existing layout
    #     for i in reversed(range(platform_list.count())):
    #         self.layout().itemAt(i).widget().setParent(None)
    #
    #     if name == "douyin":
    #         label = QLabel("Douyin Upload")
    #         layout.addWidget(douyin_form)

    def on_button_clicked(self):
        print("Button clicked!")
