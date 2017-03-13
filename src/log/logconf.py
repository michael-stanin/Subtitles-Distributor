import sys
import logging
from os import path, getenv


APP_DATA = getenv("APPDATA")
LOG_FILE = path.join(APP_DATA, "Subtitles Distributor/subtitles_distributor.log")


def logging_level():
    if getattr(sys, 'frozen', False):
        return logging.INFO
    return  logging.DEBUG


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standardformat': {
            'format': '[{asctime}] [{levelname:8}] [{name}] [{funcName}():{lineno}]: [{message}]',
            'style': '{'
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'mode': 'w',
            'formatter': 'standardformat',
        },
        'stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'standardformat',
        },
    },
    'loggers': {
        'gui.mainWindow': {
            'handlers': ['file', 'stream'],
            'level': logging_level(),
            'propagate': True
        },
        'main.subtitlesdistributor': {
            'handlers': ['file', 'stream'],
            'level': logging_level(),
            'propagate': False
        },
        'main.fileextractors.fileextractor': {
            'handlers': ['file', 'stream'],
            'level': logging_level(),
            'propagate': False
        },
        'main.fileeventhandlers.fileeventhandler': {
            'handlers': ['file', 'stream'],
            'level': logging_level(),
            'propagate': False
        },
        'config.config': {
            'handlers': ['file', 'stream'],
            'level': logging_level(),
            'propagate': False
        },
    }
}
