import logging
from main.fileextractors.compressedfile import get_compressed_file
from main.utilities.fileutils import dir_path
from main.utilities.subtitlesadjuster import ArchiveAdjuster


class FileExtractor:
    def __init__(self, subname, movfile):
        self.sn, self.mn = subname, movfile
        self.subzip = get_compressed_file(self.sn)
        self.log = logging.getLogger(__name__)
    
    def run(self):
        if self.subzip:
            return self._extractfile() and self._adjust_subs()
        return False

    def _adjust_subs(self):
        return ArchiveAdjuster(self.subzip, self.sn, self.mn).adjust()

    def _extractfile(self):
        self.log.info("Start extracting %s to: %s", self.sn, dir_path(self.mn))
        extracted = self._extract_subtitles_to_movie_dir()
        self.log.info("End extracting %s to: %s - with result %s", self.sn, dir_path(self.mn), repr(extracted))
        return extracted

    def _extract_subtitles_to_movie_dir(self):
        extracted = False
        try:
            self.subzip.accessor.extractall(dir_path(self.mn))
            extracted = True
        except Exception as e:
            self.log.exception("Failed to extract: %s", e)
        return extracted
