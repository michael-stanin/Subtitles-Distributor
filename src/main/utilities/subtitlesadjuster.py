import logging
from os import path
from random import randrange
from shutil import move
from main.utilities.fileutils import extract_archive_file_paths,\
    extract_file_paths, file_name, copyfile, dir_path, file_extension


def is_subtitles_file(name):
    ext = file_extension(name)
    return ext == ".srt" or ext == ".sub"


def _needs_subs_file_name_adjustment(m_name, s_names):
    return not any(map(lambda x: x == m_name, s_names))


def _lucky_subs(distributed_paths):
    random_index = randrange(0, len(distributed_paths))
    lucky_subs = distributed_paths[random_index]
    return lucky_subs, random_index


def _select_and_rename_subs(distributed_paths, movie_file_name):
    lucky_subs, random_index = _lucky_subs(distributed_paths)
    ext = file_extension(lucky_subs)
    new_file_name = path.join(dir_path(lucky_subs), movie_file_name + ext)
    move(distributed_paths[random_index], new_file_name)


class SubtitlesAdjuster:

    def __init__(self, subs_name, movie_name):
        self.sn, self.mn = subs_name, movie_name
        self.log = logging.getLogger(__name__)

    def adjust(self):
        distributed_paths = self._distributed_paths()
        distributed_paths = list(filter(is_subtitles_file, distributed_paths))
        self._put_files_under_movie_dir(distributed_paths)
        self._adjust_one_subs_file_name(distributed_paths)
        return True

    def _put_files_under_movie_dir(self, distributed_paths):
        for i, f in enumerate(distributed_paths):
            name, ext = file_name(f), file_extension(f)
            file_destination = path.join(dir_path(self.mn), name + ext)
            if f != file_destination:
                copyfile(f, file_destination, self.log)
            distributed_paths[i] = file_destination

    def _adjust_one_subs_file_name(self, distributed_paths):
        m_name = file_name(self.mn)
        s_names = [file_name(p) for p in distributed_paths]
        if distributed_paths and _needs_subs_file_name_adjustment(m_name, s_names):
            _select_and_rename_subs(distributed_paths, m_name)

    def _distributed_paths(self):
        return []


class ArchiveAdjuster(SubtitlesAdjuster):

    def __init__(self, z, subs_name, movie_name):
        super(ArchiveAdjuster, self).__init__(subs_name, movie_name)
        self.zip = z

    def _subs_file_paths(self):
        return extract_archive_file_paths(self.zip, self.sn)

    def _distributed_paths(self):
        return [path.join(dir_path(self.mn), path.relpath(f, start=dir_path(self.sn)))
                for f in self._subs_file_paths()]


class CopyAdjuster(SubtitlesAdjuster):

    def __init__(self, s_base_dir, subs_name, movie_name):
        super(CopyAdjuster, self).__init__(subs_name, movie_name)
        self.sDir = s_base_dir

    def _distributed_paths(self):
        if dir_path(self.sn) == self.sDir:
            self.log.info("Additional adjusting of file locations for {} is not required.".format(self.sn))
            return [self.sn]
        t = path.relpath(self.sn, start=self.sDir)
        basedir = t.split(path.sep)[0]
        tt = path.join(self.sDir, basedir)
        return extract_file_paths(tt)
