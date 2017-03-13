from os.path import dirname
from main.fileeventhandlers.fileeventhandler import FileEventHandler


class MovieEventHandler(FileEventHandler):
    patterns = ["*.mkv", "*.mpg", "*.mp2", "*.mpeg", "*.mpe", "*.mpv", "*.m2v",
                "*.mp4", "*.m4p", "*.m4v", "*.flv", "*.f4v", "*.f4p", "*.f4a",
                "*.f4b", "*.wmv", "*.avi"]

    def __init__(self, q, *args, **kwargs):
        super(MovieEventHandler, self).__init__(q, *args, **kwargs)

    def process(self, event):
        if not any(dirname(self.path) in e[1] for e in self.q.to_list()):
            super(MovieEventHandler, self).process(event)