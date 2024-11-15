from PyQt6.QtWidgets import QProgressBar, QWidget, QVBoxLayout


class UploadProgress(QWidget):
    def __init__(self):
        super().__init__()

        progress_bar = QProgressBar()
        progress_layout = QVBoxLayout()
        progress_layout.addWidget(progress_bar)
        self.setLayout(progress_layout)
