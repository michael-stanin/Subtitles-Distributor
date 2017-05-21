from os import path, getenv
from threading import Thread, Event
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import Qt
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
        None, title, getenv("SYSTEMDRIVE"), options=QFileDialog.ShowDirsOnly)


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.connect()
        self.show()
        self._config()

    def _config(self):
        self.stop_event = Event()
        self.moviesDir = ""
        self.subtitlesDir = ""
        self.sdThread = None
        #self.sd = None
        self._configure_log()
        self.folder_config = FoldersConfig()
        self._configure_combo_boxes()
        self._configure_auto_distribute()

    def _configure_auto_distribute(self):
        auto_start = self.folder_config.auto_start_distributing
        if auto_start.lower() == "true":
            self.autoDistributeChkBx.setChecked(True)
            self._auto_distribute()

    def _auto_distribute(self):
        valid_movies = is_valid_directory(self.moviesCmbBox.currentText())
        valid_subtitles = is_valid_directory(self.subtitlesCmbBox.currentText())
        if valid_movies and valid_subtitles:
            self.distribute()

    def _configure_combo_boxes(self):
        self.default_movies_folder = self.folder_config.default_movies_folder
        self.moviesCmbBox.addItem(self.default_movies_folder)
        self.movies = []
        for e in self.folder_config.movies_folders.split("|"):
            self.movies.append(e)
        self.moviesCmbBox.addItems(self.movies)
        self.moviesCmbBox.setCurrentText(self.default_movies_folder)

        self.default_subtitles_folder = self.folder_config.default_subtitles_folder
        self.subtitlesCmbBox.addItem(self.default_subtitles_folder)
        self.subs = []
        for e in self.folder_config.subtitles_folders.split("|"):
            self.subs.append(e)
        self.subtitlesCmbBox.addItems(self.subs)
        self.subtitlesCmbBox.setCurrentText(self.default_subtitles_folder)

    def _configure_log(self):
        config.dictConfig(LOGGING)
        self.log = logging.getLogger(__name__)

    def connect(self):
        self.moviesBrowseBtn.clicked.connect(self.movie_folder_browse)
        self.subtitlesBrowseBtn.clicked.connect(self.subtitles_folder_browse)
        self.distributeBtn.clicked.connect(self.distribute)
        self.stopBtn.clicked.connect(self.stop)
        
        self.moviesCmbBox.editTextChanged.connect(self.on_text_changed)
        self.subtitlesCmbBox.editTextChanged.connect(self.on_text_changed)
        self.autoDistributeChkBx.toggled.connect(self.on_auto_distribute_changed)

        self.actionDefault_Movies_Folder.triggered.connect(self.set_default_movies_folder)
        self.actionDefault_Subtitles_Folder.triggered.connect(self.set_default_subtitles_folder)
        self.actionReset_Defaults.triggered.connect(self.reset_defaults_folder)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionLimitations_2.triggered.connect(self.show_limitations)
        self.actionDeveloper_2.triggered.connect(self.show_developer)

        self.statusbar.showMessage("Fill folders to watch.", 4000)

    def on_auto_distribute_changed(self):
        state = self.autoDistributeChkBx.checkState()
        if state == Qt.Checked:
            self._auto_distribute()
        elif state == Qt.Unchecked:
            self.stop()

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
        self.folder_config.default_movies_folder = self.moviesCmbBox.currentText()

    def reset_defaults_folder(self):
        self.folder_config.reset_default_folders()

    def set_default_subtitles_folder(self):
        self.folder_config.default_subtitles_folder = self.subtitlesCmbBox.currentText()

    def on_text_changed(self):
        valid_movies = is_valid_directory(self.moviesCmbBox.currentText())
        valid_subtitles = is_valid_directory(self.subtitlesCmbBox.currentText())
        if valid_movies and valid_subtitles:
            self.moviesDir = self.moviesCmbBox.currentText()
            self.subtitlesDir = self.subtitlesCmbBox.currentText()
            self.distributeBtn.setEnabled(True)
            self.statusbar.showMessage("Ready to watch and distribute!", 4000)
        else:
            self.distributeBtn.setEnabled(False)

        if valid_movies:
            if hasattr(self, "movies") and self.moviesCmbBox.currentText() not in self.movies:
                self.movies.append(self.moviesCmbBox.currentText())
            self.actionDefault_Movies_Folder.setEnabled(True)
        else:
            self.actionDefault_Movies_Folder.setEnabled(False)
        if valid_subtitles:
            if hasattr(self, "subs") and self.subtitlesCmbBox.currentText() not in self.subs:
                self.subs.append(self.subtitlesCmbBox.currentText())
            self.actionDefault_Subtitles_Folder.setEnabled(True)
        else:
            self.actionDefault_Subtitles_Folder.setEnabled(False)

        self._auto_distribute()

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
        # Skip the first-default folders
        self.folder_config.movies_folders = [self.moviesCmbBox.itemText(i) for i in range(1, self.moviesCmbBox.count())]
        self.folder_config.subtitles_folders = [self.subtitlesCmbBox.itemText(i) for i in range(1, self.subtitlesCmbBox.count())]
        self.folder_config.auto_start_distributing = repr(self.autoDistributeChkBx.isChecked())

    def subtitles_folder_browse(self):
        self.subtitlesDir = path.abspath(browse_dialog("Select a subtitles folder to watch:"))
        self.subtitlesCmbBox.setCurrentText(self.subtitlesDir)
        if self.subtitlesDir not in self.movies and not self.subtitlesDir == self.default_subtitles_folder:
            self.subs.append(self.subtitlesDir)
            self.subtitlesCmbBox.addItem(self.subtitlesDir)

    def movie_folder_browse(self):
        self.moviesDir = path.abspath(browse_dialog("Select a movies folder to watch:"))
        self.moviesCmbBox.setCurrentText(self.moviesDir)
        if self.moviesDir not in self.movies and not self.moviesDir == self.default_movies_folder:
            self.movies.append(self.moviesDir)
            self.moviesCmbBox.addItem(self.moviesDir)
