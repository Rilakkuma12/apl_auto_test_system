#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/7/15 9:46
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_PATH = os.path.join(BASE_DIR, 'configs')
SETTING_CONF_PATH = os.path.join(CONF_PATH, 'setting.conf')
LOG_PATH = os.path.join(BASE_DIR, 'logs')
DATA_PATH = os.path.join(BASE_DIR, 'datas\\')
CASE_PATH = os.path.join(BASE_DIR, 'cases')
CASES_PATH = os.path.join(DATA_PATH, 'cases.xlsx')
REPORT_PATH = os.path.join(BASE_DIR, 'reports')
TIME_RECORD_PATH = os.path.join(DATA_PATH, 'time_records.xlsx')
TASK_ID_FILE_PATH = os.path.join(DATA_PATH, 'task_id.txt')


if __name__ == '__main__':
    print(BASE_DIR)
    print(CONF_PATH)
    print(SETTING_CONF_PATH)
    print(DATA_PATH)
