#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/7/1 9:17
import logging
from logging import handlers
import traceback
import os
import time
from handle_config import config
from constance import LOG_PATH


class HandleLogger:
    def __init__(self, log_name='apl', name='case'):
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)
        self.log = logging.getLogger(name)
        self.log.setLevel('DEBUG')
        if not log_name:
            log_name = config.get_value('log', 'log_name')
        current_date = time.strftime("%Y-%m-%d", time.localtime())
        abs_path = os.path.join(LOG_PATH, '{}.{}.log'.format(log_name, current_date))
        # file_handle = logging.FileHandler(abs_path, encoding='utf-8')
        file_handle = handlers.RotatingFileHandler(abs_path, encoding='utf-8')

        if not self.log.handlers:
            console_handle = logging.StreamHandler()

            simple_format = logging.Formatter('%(asctime)s | %(levelname)s | msg: %(message)s')
            verbose_format = logging.Formatter('%(asctime)s | %(levelname)-5s | %(process)d | %(processName)s | msg: %(message)s - %(filename)s - %(lineno)d')

            file_handle.setFormatter(verbose_format)
            console_handle.setFormatter(simple_format)

            file_handle.setLevel('DEBUG')
            console_handle.setLevel('INFO')

            self.log.addHandler(file_handle)
            self.log.addHandler(console_handle)

    def info(self, msg):
        return self.log.info(msg)

    def debug(self, msg):
        return self.log.debug(msg)

    def error(self, msg):
        return self.log.error(msg)

    def warning(self, msg):
        return self.log.warning(msg)

    def critical(self, msg):
        s = traceback.format_exc()
        return self.log.critical(msg)


my_logger = HandleLogger()
if __name__ == '__main__':
    my_logger.critical('haha')

