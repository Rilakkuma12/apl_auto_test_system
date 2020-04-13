#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/7/1 10:13
from configparser import ConfigParser
import os
from constance import SETTING_CONF_PATH


class HandleConfig:
    def __init__(self, conf_file):
        self.config = ConfigParser()
        self.file_name = conf_file
        self.config.read(self.file_name, encoding='utf-8')

    def get_value(self, section, key):
        value = self.config.get(section, key)
        return value

    def get_int(self, section, key):
        value = self.config.getint(section, key)
        return value

    def get_boolean(self, section, key):
        value = self.config.getboolean(section, key)
        return value


config = HandleConfig(SETTING_CONF_PATH)
if __name__ == '__main__':
    a = config.get_value('device id', 'HotelA')
    print(a)
