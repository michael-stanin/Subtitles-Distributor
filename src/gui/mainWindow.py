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
from main.subtitlesdistributor import SubtitlesDistributor
from main.utilities.fileutils import is_valid_directory


def browse_dialog(title):
    return QFileDialog.getExistingDirectory(
        None, title, getenv("SYSTEMDRIVE"), options=QFileDialog.ShowDirsOnly)


def generate_folders_list(default_folder, folder_config):
    l = [e for e in folder_config if not e == default_folder]
    l.insert(0, default_folder)
    return l


def handle_folder(container, combo_box, action_default_folder):
    valid_folder = is_valid_directory(combo_box.currentText())
    folder = ""
    if valid_folder:
        folder = combo_box.currentText()
        if folder not in container:
            container.append(folder)
            combo_box.addItem(folder)
        action_default_folder.setEnabled(True)
    else:
        action_default_folder.setEnabled(False)
    return folder


def folder_browse(combo_box, title):
    folder = path.abspath(browse_dialog(title))
    combo_box.setCurrentText(folder)
    return folder


def combo_box_items(combo_box):
    return [combo_box.itemText(i) for i in range(1, combo_box.count())]


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self._config()
        self.connect()

    def _config(self):
        self.stop_event = Event()
        self.moviesDir = ""
        self.subtitlesDir = ""
        self.movies = []
        self.subs = []
        self.sdThread = None
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
        movies_split = self.folder_config.movies_folders.split("|")
        self.movies = generate_folders_list(self.default_movies_folder, movies_split)
        self.moviesCmbBox.addItems(self.movies)
        self.moviesDir = self.default_movies_folder

        self.default_subtitles_folder = self.folder_config.default_subtitles_folder
        subs_split = self.folder_config.subtitles_folders.split("|")
        self.subs = generate_folders_list(self.default_subtitles_folder, subs_split)
        self.subtitlesCmbBox.addItems(self.subs)
        self.subtitlesDir = self.default_subtitles_folder

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

        if not self.moviesDir or not self.subtitlesDir:
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
        self.moviesDir = handle_folder(self.movies, self.moviesCmbBox, self.actionDefault_Movies_Folder)
        self.subtitlesDir = handle_folder(self.subs, self.subtitlesCmbBox, self.actionDefault_Subtitles_Folder)

        if self.moviesDir and self.subtitlesDir:
            if self.sdThread is not None and self.sdThread.isAlive():
                self.stop()
            self.distributeBtn.setEnabled(True)
            state = self.autoDistributeChkBx.checkState()
            if state == Qt.Checked:
                self._auto_distribute()
            self.statusbar.showMessage("Ready to watch and distribute!", 4000)
        else:
            self.distributeBtn.setEnabled(False)

    def execute_sd(self):
        self.sd = SubtitlesDistributor(
            [self.stop_event, self.moviesDir, self.subtitlesDir])
        return self.sd.start()

    def distribute(self):
        self.stopBtn.setEnabled(True)
        self.distributeBtn.setEnabled(False)

        self.statusbar.showMessage("Started watching and distributing!", 4000)

        self.stop_event.clear()
        self.sdThread = Thread(name="Subtitles Distributor Thread", target=self.execute_sd, args=())
        try:
            self.sdThread.start()
            self.log.info("Watchers started.")
        except Exception as e:
            self.log.exception("Staring watchers thread failed - %s", e)

    def stop(self):
        self.statusbar.showMessage("Stopping watching and distributing!", 4000)
        self.log.info("Stopping watching and distributing!")
        self.stopBtn.setEnabled(False)
        self.distributeBtn.setEnabled(True)
        self.stop_event.set()
        if self.sdThread is not None:
            self.sdThread.join()
        if hasattr(self, "sd"):
            del self.sd
            self.log.info("Subtitles Distributor object deleted.")
            self.log.info("Watchers finished.")

    def exit(self):
        self.stop()
        # Skip the first-default folders
        self.folder_config.movies_folders = combo_box_items(self.moviesCmbBox)
        self.folder_config.subtitles_folders = combo_box_items(self.subtitlesCmbBox)
        self.folder_config.auto_start_distributing = repr(self.autoDistributeChkBx.isChecked())

    def subtitles_folder_browse(self):
        self.subtitlesDir = self.folder_browse(self.subtitlesCmbBox, "Select a subtitles folder to watch:")

    def movie_folder_browse(self):
        self.moviesDir = self.folder_browse(self.moviesCmbBox, "Select a movies folder to watch:")
