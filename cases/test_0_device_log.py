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


@pytest.mark.device
@pytest.mark.usefixtures('init_app_device_log')
class TestDevice:
    def test_device_log(self):
        """
        1.前置条件-已扫码
        2.发送上料指令，撕膜为true
        3.DX会弹重试框
        4.断言返回重试框错误码
        5.备注：测试结束后需要人工介入恢复
        """
        comm_id = kafka_load_consumables.load_consumable_all_board_no_wait(us.a_SP96XL1,
                                                                           tearing='true',
                                                                           load={'MGRK01': ('POS2',)})
        time.sleep(80)
        try:
            assert km.is_conform_to_device_log(msg_tp='device_log',
                                               comm_id=comm_id,
                                               target_key='log_code',
                                               target_value='1118558') is True
        except AssertionError as e:
            my_logger.error(e)
            raise e


if __name__ == '__main__':
    pytest.main([
        '-s',
        '-m device',
        '--resultlog=reports/auto_test_report.txt',
        '--junitxml=reports/auto_test_report.xml',
        '--html=reports/auto_test_report.html',
        '--alluredir=alluredir/'
                 ])


