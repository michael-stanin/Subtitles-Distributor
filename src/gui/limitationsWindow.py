from .helpDialog import HelpDialog
from .ui.limitationsWindowUi import Ui_LimitationsWindow


class LimitationsWindow(HelpDialog, Ui_LimitationsWindow):

    def __init__(self, *args, **kwargs):
        super(LimitationsWindow, self).__init__(*args, **kwargs)
