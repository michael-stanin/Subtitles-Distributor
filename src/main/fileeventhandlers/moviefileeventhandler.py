from os.path import dirname
from main.fileeventhandlers.fileeventhandler import FileEventHandler
from main.utilities.fileutils import file_name, path_leaf, dir_path


class MovieEventHandler(FileEventHandler):
    patterns = ["*.mkv", "*.mpg", "*.mp2", "*.mpeg", "*.mpe", "*.mpv", "*.m2v",
                "*.mp4", "*.m4p", "*.m4v", "*.flv", "*.f4v", "*.f4p", "*.f4a",
                "*.f4b", "*.wmv", "*.avi"]

    def __init__(self, q, *args, **kwargs):
        super(MovieEventHandler, self).__init__(q, *args, **kwargs)

    def process(self, event):
        self.log.debug(self.q.to_list())
        valid = not any(self._filter(e) for e in self.q.to_list())
        if valid:
            self.log.info("Handling valid movie file %s", self.path)
            super(MovieEventHandler, self).process(event)

    def _filter(self, e):
        self.log.info(e)
        self.log.debug(file_name(self.path).lower())
        self.log.debug(dirname(self.path).lower())
        b1 = self._is_sample()
        b2 = dir_path(self.path) in e[1]
        self.log.debug("Folder %s is  handled: %s. %s is in %s: %s", path_leaf(dir_path(self.path)), b2, dir_path(self.path), e[1], b2)
        return b1 or b2

    def _is_sample(self):
        sample = "sample"
        b1 = file_name(self.path).lower() == sample
        b2 = path_leaf(dir_path(self.path)).lower() == sample
        self.log.debug("File is  sample: %s", b1)
        self.log.debug("Folder is sample: %s", b2)
        return b1 or b2
