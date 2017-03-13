from .config import Config
from main.findresource import find_data_file


VERSION_SECTION = "VERSION"
VERSION = "VERSION"
SUB_VERSION = "SUB VERSION"
BUILD = "BUILD"
CONFIG_FILE = find_data_file("version.cfg")
VERSION_NUMBER = "1"
SUB_VERSION_NUMBER = "2"
BUILD_NUMBER = "0"
DOT = "."


class VersionConfig(Config):
    def __init__(self):
        super(VersionConfig, self).__init__()
        self._init_config_file()

    def _init_config_file(self):
        self.config_file = CONFIG_FILE
        self._init_version()
        super(VersionConfig, self)._init_config_file()
        self._update_version()

    def _init_version(self):
        self.config[VERSION_SECTION] = {}
        version_section = self.config[VERSION_SECTION]
        version_section[VERSION] = VERSION_NUMBER
        version_section[SUB_VERSION] = SUB_VERSION_NUMBER
        version_section[BUILD] = BUILD_NUMBER

    def _update_version(self):
        version_section = self.config[VERSION_SECTION]
        if version_section[VERSION] != VERSION_NUMBER:
            version_section[VERSION] = VERSION_NUMBER
            version_section[BUILD] = BUILD_NUMBER
        if version_section[SUB_VERSION] != SUB_VERSION_NUMBER:
            version_section[SUB_VERSION] = SUB_VERSION_NUMBER
            version_section[BUILD] = BUILD_NUMBER
        super(VersionConfig, self)._update()

    def incremented_version(self):
        self.build = str(int(self.build) + 1)
        return self.full_version

    @property
    def full_version(self):
        return self.version + DOT + self.sub_version + DOT + self.build

    @property
    def version(self):
        return self._get(VERSION_SECTION, VERSION)

    @property
    def sub_version(self):
        return self._get(VERSION_SECTION, SUB_VERSION)

    @property
    def build(self):
        return self._get(VERSION_SECTION, BUILD)

    @build.setter
    def build(self, val):
        self._set(VERSION_SECTION, BUILD, val)
