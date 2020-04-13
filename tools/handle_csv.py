#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/8/7 13:26
import csv
import pandas as pd
import os
from tools.constance import TIME_RECORD_PATH
from tools.handle_log import my_logger


class HandleCsv:
    head = ['CycleNo', 'LoadCosumablesTime', 'TransferTime', 'PushCosumablesTime']

    def __init__(self):
        if os.path.exists(TIME_RECORD_PATH):
            pass
        else:
            with open(TIME_RECORD_PATH, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(self.head)

    @staticmethod
    def record_to_csv(data):
        with open(TIME_RECORD_PATH, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
        # data = pd.DataFrame(list(data))
        # try:
        #     data.to_csv(TIME_RECORD_PATH, mode='a', header=False, index=False, doublequote=False)
        # except UnicodeEncodeError:
        #     my_logger.error('编码错误，无法写入文件')


if __name__ == '__main__':
    my_file = HandleCsv()
    my_file.record_to_csv(['0:00:20', '0:00:20', '0:00:20'])










