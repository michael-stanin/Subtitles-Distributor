import os
import shutil
import ntpath
import glob
from rarfile import RarFile
from zipfile import ZipFile
from main.fileextractors.compressedfile import ZIPFile, RARFile


def copyfile(src, dst, log):
    try:
        log.info("Start copying '%s' to '%s'.", src, dst)
        shutil.copyfile(src, dst)
    except shutil.Error as e:  # Directories are the same
        log.exception("File not copied. Error: '%s'", e)
    except IOError as e:
        log.exception("File not found or location is not writable. Error: '%s'", e)
    except:
        pass
    finally:
        log.info("Done copying '%s' to '%s'.", src, dst)


def is_valid_directory(d):
    return os.path.exists(d) and os.path.isdir(d)


def is_valid_file(f):
    return os.path.exists(f) and os.path.isfile(f)


def valid_directories(dirs):
    return all(map(is_valid_directory, dirs))


def extract_archive_file_paths(zip, z_path):
    parent_dir = dir_path(z_path)
    if isinstance(zip, ZIPFile):
        with ZipFile(z_path) as z:
            fps = [os.path.join(parent_dir, p) for p in z.namelist() if not p.endswith("/")]
    elif isinstance(zip, RARFile):
        with RarFile(z_path) as r:
            fps = [os.path.join(parent_dir, p.filename) for p in r.infolist() if not p.isdir()]
    else:
        fps = []
    return fps


def file_name(f):
    return ntpath.basename(ntpath.splitext(f)[0])


def file_extension(f):
    return ntpath.splitext(f)[1]


def extract_file_paths(path):
    t = []
    fps = glob.glob(path + "**/**", recursive=True)
    for f in fps:
        if is_valid_file(f):
            t.append(f)
    return t


def extract_file_name(fp):
    return os.path.basename(os.path.splitext(fp)[0])


def get_file_name(fp):
    return path_leaf(fp)


def dir_path(fp):
    head, tail = ntpath.split(fp)
    return head


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
