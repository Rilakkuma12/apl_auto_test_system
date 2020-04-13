#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/6/27 20:41
import unittest
from libs.ddt import ddt, data
from tools.handle_excel import HandleExcel
from tools.handle_config import config
from tools.handle_log import my_logger
from tools.constance import CASES_PATH
from action import kafka_device_command
import time
import pytest
from common.kafka_msg import km


@pytest.mark.storage
@pytest.mark.usefixtures('init_app_hotel')
class TestCytomat:
    def test_scan_all(self):
        """
        1.发送扫码指令
        2.断言返回running
        3.断言上报库存信息
        4.断言返回done
        """
        comm_id = kafka_device_command.scan_hotel_no_wait()
        time.sleep(3)
        try:
            assert km.is_conform_to_storage_command_msg(comm_id=comm_id, target_value='running') is True
            assert km.is_conform_to_storage_stock_msg() is True
            assert km.is_conform_to_storage_command_msg(comm_id=comm_id, target_value='done') is True
        except AssertionError as e:
            my_logger.error(e)
            raise e

    def test_scan_one(self):
        """
        1.发送扫码指令
        2.断言返回running
        3.断言上报库存信息
        4.断言返回done
        """
        comm_id = kafka_device_command.scan_hotel_no_wait()
        time.sleep(3)
        try:
            assert km.is_conform_to_storage_command_msg(comm_id=comm_id, target_value='running') is True
            assert km.is_conform_to_storage_stock_msg() is True
            assert km.is_conform_to_storage_command_msg(comm_id=comm_id, target_value='done') is True
        except AssertionError as e:
            my_logger.error(e)
            raise e


if __name__ == '__main__':
    pytest.main([
        '-s',
        '-m storage',
        '--resultlog=reports/auto_test_report.txt',
        '--junitxml=reports/auto_test_report.xml',
        '--html=reports/auto_test_report.html',
        '--alluredir=alluredir/'
                 ])
