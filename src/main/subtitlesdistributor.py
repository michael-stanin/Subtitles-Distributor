import os
import subprocess
import logging
from functools import reduce
from watchdog.observers import Observer
from .setqueue import SetQueue
from main.fileextractors.fileextractor import FileExtractor
from main.fileeventhandlers.moviefileeventhandler import MovieEventHandler
from main.fileeventhandlers.subtitlesfileeventhandler import SubtitlesEventHandler
from main.utilities.fileutils import valid_directories
from main.utilities.subtitlesadjuster import CopyAdjuster


BUF_SIZE = 10
mq = SetQueue(BUF_SIZE)
sq = SetQueue(BUF_SIZE)


def clear_queues():
    with mq.mutex:
        mq.queue.clear()
    with sq.mutex:
        sq.queue.clear()


def extract(sfile, mfile):
    fe = FileExtractor(sfile, mfile)
    return fe.run()


def copy(s_base_dir, sfile, mfile):
    ca = CopyAdjuster(s_base_dir, sfile, mfile)
    return ca.adjust()


def folder_observer(handler, d):
    observer = Observer()
    observer.setDaemon(True)
    observer.schedule(handler, d, recursive=True)
    return observer


def finish_folder_observer(observer):
    if observer.isAlive():
        observer.stop()
        observer.join()


class SubtitlesDistributor:
    def __init__(self, argv):
        self.stop_event = argv[0]
        self.mDir = argv[1]
        self.sDir = argv[2]
        self.log = logging.getLogger(__name__)

    def watch_and_distribute(self, results):
        movs_observer = folder_observer(MovieEventHandler(mq), self.mDir)
        subs_observer = folder_observer(SubtitlesEventHandler(sq), self.sDir)

        movs_observer.name = "Movie Watcher Thread"
        subs_observer.name = "Subtitles Watcher Thread"

        movs_observer.start()
        subs_observer.start()

        try:
            while not self.stop_event.is_set():
                if not mq.empty() and not sq.empty():
                    self._consume(results)
        finally:
            self.log.info("Stop event is set.")
            self.log.debug("Joining movies watcher")
            finish_folder_observer(movs_observer)
            self.log.debug("Joining Subtitles watcher")
            finish_folder_observer(subs_observer)
            self.log.debug("Joining finished.")

    def _consume(self, results):
        self.log.info("Consuming movies and subtitles.")
        self.log.info("Movies: %s.", mq.to_list())
        self.log.info("Subtitles: %s.", sq.to_list())

        movie_file, movie_dir = mq.get()
        subs_file, subs_dir = sq.get()

        self.log.info("Trying to extract...")
        rc = extract(subs_file, movie_file)
        if rc:
            self.log.info("Extraction succeeded.")
        else:
            self.log.error("Extraction failed!")
            self.log.info("Trying to copy...")
            rc = copy(self.sDir, subs_file, movie_file)
            copy_status_message = "Copy succeeded." if rc else "Copy failed!"
            self.log.info(copy_status_message)

        if rc:
            query = 'explorer /select,"{}"'.format(os.path.abspath(movie_file))
            subprocess.Popen(query)

        results.append(rc)
        mq.task_done()
        sq.task_done()

    def _start(self, results):
        self.log.info("Movies directory - %s", self.mDir)
        self.log.info("Subtitles directory - %s", self.sDir)
        if valid_directories([self.mDir, self.sDir]):
            self.log.info("%s and %s are valid.", self.mDir, self.sDir)
            self.watch_and_distribute(results)

    def start(self):
        self.log.info("Starting Subtitles Distributor.")
        rc = True
        results = []

        self._start(results)

        if results:
            rc = reduce(lambda x, y: x and y, results)
            self.log.debug("Results: %s, equal to: %s", repr(results), rc)

        clear_queues()

        self.log.info("Ending Subtitles Distributor.")
        return rc
