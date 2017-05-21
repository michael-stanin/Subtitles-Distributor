from .config import Config
from os import path, getenv


PATHS_SECTION = "WATCH FOLDER PATHS"
DEFAULT_MOVIES_FOLDER = "DEFAULT MOVIES FOLDER"
DEFAULT_SUBTITLES_FOLDER = "DEFAULT SUBTITLES FOLDER"
MOVIES_FOLDERS = "MOVIES FOLDERS"
SUBTITLES_FOLDERS = "SUBTITLES FOLDERS"
DISTRIBUTING_SECTION = "DISTRIBUTING SETTINGS"
AUTO_START_DISTRIBUTING = "AUTO START DISTRIBUTING"
APP_DATA = getenv("APPDATA")
USER_PROFILE = getenv("USERPROFILE")
USER_DOWNLOADS = path.join(USER_PROFILE, "Downloads")
CONFIG_FILE = path.join(APP_DATA, "Subtitles Distributor/folders_config.cfg")


class FoldersConfig(Config):
    def __init__(self):
        super(FoldersConfig, self).__init__()
        self._init_config_file()

    def _init_config_file(self):
        self.config_file = CONFIG_FILE
        super(FoldersConfig, self)._init_config_file()

    def _set_defaults(self):
        self._set_default_path_section()
        self._set_default_distributing_section()
        super(FoldersConfig, self)._update()

    def _set_default_path_section(self):
        if not self.config.has_section(PATHS_SECTION):
            self.config[PATHS_SECTION] = {}
        pathsection = self.config[PATHS_SECTION]

        if not self.config.has_option(PATHS_SECTION, DEFAULT_MOVIES_FOLDER):
            pathsection[DEFAULT_MOVIES_FOLDER] = ""

        if not self.config.has_option(PATHS_SECTION, DEFAULT_SUBTITLES_FOLDER):
            pathsection[DEFAULT_SUBTITLES_FOLDER] = ""

        if not self.config.has_option(PATHS_SECTION, MOVIES_FOLDERS) or \
                (self.config.has_option(PATHS_SECTION, MOVIES_FOLDERS) and not self.config.get(PATHS_SECTION, MOVIES_FOLDERS)):
            pathsection[MOVIES_FOLDERS] = USER_DOWNLOADS if path.exists(USER_DOWNLOADS) else ""

        if not self.config.has_option(PATHS_SECTION, SUBTITLES_FOLDERS) or \
                (self.config.has_option(PATHS_SECTION, SUBTITLES_FOLDERS) and not self.config.get(PATHS_SECTION, SUBTITLES_FOLDERS)):
            pathsection[SUBTITLES_FOLDERS] = USER_DOWNLOADS if path.exists(USER_DOWNLOADS) else ""

    def _set_default_distributing_section(self):
        if not self.config.has_section(DISTRIBUTING_SECTION):
            self.config[DISTRIBUTING_SECTION] = {}
        distributing_section = self.config[DISTRIBUTING_SECTION]

        if not self.config.has_option(DISTRIBUTING_SECTION, AUTO_START_DISTRIBUTING):
            distributing_section[AUTO_START_DISTRIBUTING] = ""

    def reset_default_folders(self):
        [self._set(PATHS_SECTION, key, "") for key in [DEFAULT_MOVIES_FOLDER, DEFAULT_SUBTITLES_FOLDER]]

    @property
    def default_movies_folder(self):
        return self._get(PATHS_SECTION, DEFAULT_MOVIES_FOLDER)

    @default_movies_folder.setter
    def default_movies_folder(self, val):
        self._set(PATHS_SECTION, DEFAULT_MOVIES_FOLDER, val)

    @property
    def default_subtitles_folder(self):
        return self._get(PATHS_SECTION, DEFAULT_SUBTITLES_FOLDER)

    @default_subtitles_folder.setter
    def default_subtitles_folder(self, val):
        self._set(PATHS_SECTION, DEFAULT_SUBTITLES_FOLDER, val)

    @property
    def movies_folders(self):
        return self._get(PATHS_SECTION, MOVIES_FOLDERS)

    @movies_folders.setter
    def movies_folders(self, val):
        self._set(PATHS_SECTION, MOVIES_FOLDERS, "|".join(val))

    @property
    def subtitles_folders(self):
        return self._get(PATHS_SECTION, SUBTITLES_FOLDERS)

    @subtitles_folders.setter
    def subtitles_folders(self, val):
        self._set(PATHS_SECTION, SUBTITLES_FOLDERS, "|".join(val))

    @property
    def auto_start_distributing(self):
        return self._get(DISTRIBUTING_SECTION, AUTO_START_DISTRIBUTING)

    @auto_start_distributing.setter
    def auto_start_distributing(self, val):
        self._set(DISTRIBUTING_SECTION, AUTO_START_DISTRIBUTING, val)
