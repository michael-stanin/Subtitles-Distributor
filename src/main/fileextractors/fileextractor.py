import logging
from main.fileextractors.compressedfile import get_compressed_file
from os.path import join


class FileExtractor:
    def __init__(self, subname, subdir, movdir):
        self.sn, self.sd, self.md = subname, subdir, movdir
        self.subzip = None
        self.log = logging.getLogger(__name__)
    
    def run(self):
        sub_full_path = join(self.sd, self.sn)
        self.subzip = get_compressed_file(sub_full_path)
        if self.subzip:
            return self._extractfile()
        return False

    def _extractfile(self):
        self.log.info("Start extracting %s to: %s", self.sn, self.md)
        extracted = self._extract_subtitles_to_movie_dir()
        self.log.info("End extracting %s to: %s - with result %s", self.sn, self.md, repr(extracted))
        return extracted

    def _extract_subtitles_to_movie_dir(self):
        extracted = False
        try:
            self.subzip.accessor.extractall(self.md)
            extracted = True
        except Exception as e:
            self.log.exception("Failed to extract: %s", e)
        return extracted
