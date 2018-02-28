import os
import logging
from logging.handlers import TimedRotatingFileHandler

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
# 更保险的做法 https://stackoverflow.com/questions/2860153/how-do-i-get-the-parent-directory-in-python
ROOT_PATH = os.path.abspath(os.path.join(CURRENT_PATH, os.pardir))
LOG_PATH = os.path.join(ROOT_PATH, 'Log')


class LogHandler(logging.Logger):
    """
    日志类
    """
    def __init__(self, name, level=DEBUG, stream=True, file=True):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, self.level)
        if stream:
            self._set_stream_handler_()
        if file:
            self._set_file_handler_()

    def _set_stream_handler_(self):
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(self.level)
        self.addHandler(stream_handler)

    def _set_file_handler_(self):
        file_name = os.path.join(LOG_PATH, '{}.log'.format(self.name))
        file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=10)
        file_handler.suffix = '%Y%m%d.log'
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(self.level)
        self.file_handler = file_handler
        self.addHandler(file_handler)

