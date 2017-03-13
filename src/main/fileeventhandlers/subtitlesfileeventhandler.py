from main.fileeventhandlers.fileeventhandler import FileEventHandler


class SubtitlesEventHandler(FileEventHandler):
    patterns = ["*.zip", "*.rar", "*.7z", "*.srt", "*.sub"]

    def __init__(self, q, *args, **kwargs):
        super(SubtitlesEventHandler, self).__init__(q, *args, **kwargs)
