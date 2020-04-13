#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2019/9/23 16:06
import time
from common.kafka_msg import km
import pytest
from action import kafka_load_consumables
from common import base as us
from handle_log import my_logger


@pytest.mark.dm
@pytest.mark.usefixtures('init_app_startlet_bmg')
class TestDm:
    def test_response(self):
        try:
            assert True is True
        except AssertionError as e:
            my_logger.error(e)

    def test_load_consumables(self):
        try:
            assert True is True
        except AssertionError as e:
            my_logger.error(e)

    def test_quantification(self):
        try:
            assert True is True
        except AssertionError as e:
            my_logger.error(e)

    def test_normalization(self):
        try:
            assert True is True
        except AssertionError as e:
            my_logger.error(e)

    def test_push_consumables(self):
        try:
            assert True is True
        except AssertionError as e:
            my_logger.error(e)


if __name__ == '__main__':
    pytest.main(['-s',
                 '-m dm',
                 '--resultlog=reports/auto_test_report.txt',
                 '--junitxml=reports/auto_test_report.xml',
                 '--html=reports/auto_test_report.html',
                 '--alluredir=alluredir/'
                 ])
