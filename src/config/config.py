import configparser
import logging
from os import makedirs, path


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_file = None
        self.log = logging.getLogger(__name__)

    def _get(self, section, key):
        val = ""
        try:
            val = self.config[section][key]
        except KeyError as e:
            self.log.exception("%s not found in configuration file - %s", key, e)
        return val

    def _update(self):
        if self.config_file is not None:
            try:
                with open(self.config_file, "w") as configfile:
                    self.config.write(configfile)
            except OSError as e:
                self.log.exception("Failed to update %s - %s", self.config_file, e)

    def _set(self, section, key, value):
        self.config[section][key] = value
        self._update()

    def _set_defaults(self):
        pass

    def _init_config_file(self):
        if self.config_file is not None:
            dir_name = path.dirname(self.config_file)
            if not path.exists(dir_name):
                makedirs(dir_name)
            if path.exists(self.config_file):
                self.config.read_file(open(self.config_file))
            self._set_defaults()
