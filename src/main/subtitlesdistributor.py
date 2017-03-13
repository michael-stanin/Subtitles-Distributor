import os
import shutil
import subprocess
import time
import logging
from functools import reduce
from threading import Thread
from watchdog.observers import Observer
from .setqueue import SetQueue
from main.fileextractors.fileextractor import FileExtractor
from main.fileeventhandlers.moviefileeventhandler import MovieEventHandler
from main.fileeventhandlers.subtitlesfileeventhandler import SubtitlesEventHandler


BUF_SIZE = 10
mq = SetQueue(BUF_SIZE)
sq = SetQueue(BUF_SIZE)


def clear_queues():
    with mq.mutex:
        mq.queue.clear()
    with sq.mutex:
        sq.queue.clear()


def copyfile(src, dst, log):
    try:
        log.info("Start copying %s to %s.",src, dst)
        shutil.copyfile(src, dst)
    except shutil.Error as e:  # Directories are the same
        log.exception("File not copied. Error: %s", e)
    except IOError as e:
        log.exception("File not found or location is not writable. Error: %s", e)
    except:
        pass
    finally:
        log.info("Done copying %s to %s.", src, dst)


def is_valid_directory(d):
    return os.path.exists(d) and os.path.isdir(d)


def valid_directories(dirs):
    return all(map(is_valid_directory, dirs))



def extract(sfile, sdir, mdir):
    return FileExtractor(sfile, sdir, mdir).run()


class SubtitlesDistributor:
    def __init__(self, argv):
        self.stop_event = argv[0]
        self.mDir = argv[1]
        self.sDir = argv[2]
        self.log = logging.getLogger(__name__)

    def producing_thread(self, handler, d):
        observer = Observer()
        observer.setDaemon(True)
        observer.schedule(handler, d, recursive=True)
        observer.start()

        try:
            while not self.stop_event.is_set():
                time.sleep(1)
        finally:
            self.log.info("Stop event is set.")
            observer.stop()
            observer.join()

    def _consume(self, results):
        self.log.info("Consuming movies and subtitles.")
        self.log.info("Movies: %s.", mq.to_list())
        self.log.info("Subtitles: %s.", sq.to_list())

        movie_file, movie_dir = mq.get()
        subs_file, subs_dir = sq.get()

        self.log.info("Trying to extract...")
        rc = extract(subs_file, subs_dir, movie_dir)
        if rc:
            self.log.info("Extraction succeeded.")
        else:
            self.log.error("Extraction failed!")
            self.log.info("Starting copy of %s to %s", subs_file, movie_dir)
            copyfile(subs_file, movie_dir, self.log)
        query = 'explorer /select,"{}"'.format(os.path.abspath(movie_file))
        subprocess.Popen(query)
        results.append(rc)
        mq.task_done()
        sq.task_done()

    def consuming_thread(self, results):
        while not self.stop_event.is_set():
            if not mq.empty() and not sq.empty():
                self._consume(results)
        return

    def _start_worker_threads(self, mq, sq, results):
        m_t = Thread(name="Movies Thread",
                     target=self.producing_thread,
                     args=(MovieEventHandler(mq), self.mDir))
        s_t = Thread(name="Subtitles Thread",
                     target=self.producing_thread,
                     args=(SubtitlesEventHandler(sq), self.sDir))
        c_t = Thread(name="Consumer Thread",
                     target=self.consuming_thread,
                     args=(results,))
        for t in [m_t, s_t, c_t]:
            t.daemon = True
        for t in [m_t, s_t, c_t]:
            t.start()
        return m_t, s_t, c_t

    def _start(self, results):
        self.log.info("Movies directory - %s", self.mDir)
        self.log.info("Subtitles directory - %s", self.sDir)
        if valid_directories([self.mDir, self.sDir]):
            while not self.stop_event.is_set():
                m_t, s_t, c_t = self._start_worker_threads(mq, sq, results)
                for t in [m_t, s_t, c_t]:
                    t.join()
                self.log.info("Worker threads finished.")

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
