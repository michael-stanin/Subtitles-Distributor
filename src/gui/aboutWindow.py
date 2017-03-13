from time import strftime
from .helpDialog import HelpDialog
from .ui.aboutWindowUi import Ui_AboutWindow
from config.versionconfig import VersionConfig


class AboutWindow(HelpDialog, Ui_AboutWindow):

    def __init__(self, *args, **kwargs):
        super(AboutWindow, self).__init__(*args, **kwargs)

        cfg = VersionConfig()
        self.version_info_lbl.setText("Subtitles Distributor {}.{}.".format(
            cfg.version, cfg.sub_version
        ))
        self.build_info_lbl.setText("Build #{}, built on {}.".format(
            cfg.build, strftime("%d %B %Y")
        ))
