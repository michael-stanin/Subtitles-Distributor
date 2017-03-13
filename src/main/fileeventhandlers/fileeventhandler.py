import logging
from os.path import dirname
from watchdog.events import PatternMatchingEventHandler


class FileEventHandler(PatternMatchingEventHandler):
    ignore_directories = True

    def __init__(self, q, *args, **kwargs):
        super(FileEventHandler, self).__init__(*args, **kwargs)
        self.q = q
        self.path = ""
        self.log = logging.getLogger(__name__)

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        self.log.info("Found new file in producer - %s", self.path)
        self.q.put((self.path, dirname(self.path)))

    def on_created(self, event):
        self.path = event.src_path
        self.process(event)

    def on_moved(self, event):
        self.path = event.dest_path if event.dest_path else event.src_path
        self.process(event)