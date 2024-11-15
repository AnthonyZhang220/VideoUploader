from PyQt6.QtWidgets import QFormLayout, QLineEdit, QWidget


class DouyinUploadForm(QWidget):
    def __init__(self):
        super().__init__()

        form_layout = QFormLayout()
        form_layout.addRow("Enter video title:", QLineEdit(self))
        form_layout.addRow("Enter video subtitle:", QLineEdit(self))
        form_layout.addRow("Enter video description:", QLineEdit(self))
        form_layout.addRow("Upload Thumbnail:", QLineEdit(self))
        self.setLayout(form_layout)
