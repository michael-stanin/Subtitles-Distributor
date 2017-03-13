from .helpDialog import HelpDialog
from .ui.developerWindowUi import Ui_DeveloperWindow


class DeveloperWindow(HelpDialog, Ui_DeveloperWindow):

    def __init__(self, *args, **kwargs):
        super(DeveloperWindow, self).__init__(*args, **kwargs)
