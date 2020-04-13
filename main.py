#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/6/26 19:16
import pytest

from tools.handle_config import config
import unittest
from libs import HTMLTestRunnerNew
from tools.constance import REPORT_PATH
from tools.constance import CASE_PATH
import time


if __name__ == '__main__':
    pytest.main([
        '-s',
        '--resultlog=reports/auto_test_report.txt',
        '--junitxml=reports/auto_test_report.xml',
        '--html=reports/auto_test_report.html',
        '--alluredir=alluredir/'
                 ])


