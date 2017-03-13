from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog


class HelpDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(HelpDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
