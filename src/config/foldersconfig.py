from .config import Config
from os import path, getenv


PATHS_SECTION = "WATCH FOLDER PATHS"
MOVIES_FOLDER = "MOVIES FOLDER"
SUBTITLES_FOLDER = "SUBTITLES FOLDER"
APP_DATA = getenv("APPDATA")
CONFIG_FILE_FOLDER = path.join(APP_DATA, "")
CONFIG_FILE = path.join(APP_DATA, "Subtitles Distributor/folders_config.cfg")


class FoldersConfig(Config):
    def __init__(self):
        super(FoldersConfig, self).__init__()
        self._init_config_file()

    def _init_config_file(self):
        self.config_file = CONFIG_FILE
        self.config[PATHS_SECTION] = {}
        pathsection = self.config[PATHS_SECTION]
        pathsection[MOVIES_FOLDER] = ""
        pathsection[SUBTITLES_FOLDER] = ""
        super(FoldersConfig, self)._init_config_file()

    def reset(self):
        [self._set(PATHS_SECTION, key, "") for key in [MOVIES_FOLDER, SUBTITLES_FOLDER]]

    @property
    def movies(self):
        return self._get(PATHS_SECTION, MOVIES_FOLDER)

    @movies.setter
    def movies(self, folder):
        self._set(PATHS_SECTION, MOVIES_FOLDER, folder)

    @property
    def subtitles(self):
        return self._get(PATHS_SECTION, SUBTITLES_FOLDER)

    @subtitles.setter
    def subtitles(self, folder):
        self._set(PATHS_SECTION, SUBTITLES_FOLDER, folder)
