from threading import Thread, Event
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import logging
from logging import config
from config.foldersconfig import FoldersConfig
from .ui.mainWindowUi import Ui_MainWindow
from .aboutWindow import AboutWindow
from .limitationsWindow import LimitationsWindow
from .developerWindow import DeveloperWindow
from log.logconf import LOGGING
from main.subtitlesdistributor import SubtitlesDistributor, is_valid_directory




def browse_dialog(title):
    return QFileDialog.getExistingDirectory(
        None, title, "C:\\", options=QFileDialog.ShowDirsOnly)


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.connect()
        self.show()
        self.stop_event = Event()
        self.moviesDir = ""
        self.subtitlesDir = ""
        self.sdThread = None
        self.sd = None
        self.folder_config = FoldersConfig()
        self.moviesLine.setText(self.folder_config.movies)
        self.subtitlesLine.setText(self.folder_config.subtitles)
        self._configure_log()

    def _configure_log(self):
        config.dictConfig(LOGGING)
        self.log = logging.getLogger(__name__)

    def connect(self):
        self.moviesBrowseBtn.clicked.connect(self.movie_folder_browse)
        self.subtitlesBrowseBtn.clicked.connect(self.subtitles_folder_browse)
        self.distributeBtn.clicked.connect(self.distribute)
        self.stopBtn.clicked.connect(self.stop)
        
        self.moviesLine.textChanged.connect(self.on_text_changed)
        self.subtitlesLine.textChanged.connect(self.on_text_changed)

        self.actionDefault_Movies_Folder.triggered.connect(self.set_default_movies_folder)
        self.actionDefault_Subtitles_Folder.triggered.connect(self.set_default_subtitles_folder)
        self.actionReset_Defaults.triggered.connect(self.reset_defaults_folder)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionLimitations_2.triggered.connect(self.show_limitations)
        self.actionDeveloper_2.triggered.connect(self.show_developer)

        self.statusbar.showMessage("Fill folders to watch.", 4000)

    def show_developer(self):
        developer_window = DeveloperWindow(self)
        developer_window.show()

    def show_limitations(self):
        limitations_window = LimitationsWindow(self)
        limitations_window.show()

    def show_about(self):
        about_window = AboutWindow(self)
        about_window.show()

    def set_default_movies_folder(self):
        self.folder_config.movies = self.moviesLine.text()

    def reset_defaults_folder(self):
        self.folder_config.reset()

    def set_default_subtitles_folder(self):
        self.folder_config.subtitles = self.subtitlesLine.text()

    def on_text_changed(self):
        valid_movies = is_valid_directory(self.moviesLine.text())
        valid_subtitles = is_valid_directory(self.subtitlesLine.text())
        if valid_movies and valid_subtitles:
            self.moviesDir = self.moviesLine.text()
            self.subtitlesDir = self.subtitlesLine.text()
            self.distributeBtn.setEnabled(True)
            self.statusbar.showMessage("Ready to watch and distribute!", 4000)
        else:
            self.distributeBtn.setEnabled(False)

        if valid_movies:
            self.actionDefault_Movies_Folder.setEnabled(True)
        else:
            self.actionDefault_Movies_Folder.setEnabled(False)
        if valid_subtitles:
            self.actionDefault_Subtitles_Folder.setEnabled(True)
        else:
            self.actionDefault_Subtitles_Folder.setEnabled(False)

    def execute_sd(self):
        self.sd = SubtitlesDistributor(
            [self.stop_event, self.moviesDir, self.subtitlesDir])
        return self.sd.start()

    def distribute(self):
        self.stopBtn.setEnabled(True)
        self.distributeBtn.setEnabled(False)

        self.statusbar.showMessage("Started watching and distributing!", 4000)

        self.stop_event.clear()
        self.sdThread = Thread(target=self.execute_sd, args=())
        try:
            self.sdThread.start()
            self.log.info("Watchers started.")
        except Exception as e:
            self.log.exception("Staring watchers thread failed - %s", e)

    def stop(self):
        self.statusbar.showMessage("Stopping watching and distributing!", 4000)
        self.stopBtn.setEnabled(False)
        self.distributeBtn.setEnabled(True)
        self.stop_event.set()
        if hasattr(self, "sd"):
            del self.sd
            self.log.info("Subtitles Distributor object deleted.")
            self.log.info("Watchers finished.")
        if self.sdThread is not None:
            self.sdThread.join()


    def subtitles_folder_browse(self):
        self.subtitlesDir = browse_dialog("Select a subtitles folder to watch:")
        self.subtitlesLine.setText(self.subtitlesDir)

    def movie_folder_browse(self):
        self.moviesDir = browse_dialog("Select a movies folder to watch:")
        self.moviesLine.setText(self.moviesDir)
