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


@pytest.mark.load
@pytest.mark.usefixtures('init_app_load_consumables')
class TestLoadConsumable:
    def test_load_task(self):
        """
        1.前置条件扫码
        2.发送上料
        3.断言返回task running
        4.断言返回task complete success
        """
        comm_id = kafka_load_consumables.load_consumable_all_board_no_wait(us.a_SP96XL1, load={'MGRK01': ('POS2',)})
        time.sleep(3)
        try:
            assert km.is_conform_to_task_msg(msg_tp='response',
                                             comm_id=comm_id,
                                             target_key='response',
                                             target_value='running') is True

            assert km.is_conform_to_task_msg(msg_tp='complete',
                                             comm_id=comm_id,
                                             target_key='complete_status',
                                             target_value='success') is True
        except AssertionError as e:
            my_logger.error(e)

    def test_load_put_in_place(self):
        """
        1.前置条件扫码
        2.发送上料
        3.断言返回板位摆放到位
        """
        comm_id = kafka_load_consumables.load_consumable_all_board_no_wait(us.a_SP96XL1, load={'MGRK01': ('POS3',)})
        time.sleep(3)
        try:
            assert km.is_conform_to_task_msg(msg_tp='putinplace',
                                             comm_id=comm_id,
                                             target_key='complete_status',
                                             target_value='success') is True
        except AssertionError as e:
            my_logger.error(e)

    def test_load_assist(self):
        """
        1.前置条件扫码
        2.发送上料
        3.断言返回封撕膜完成
        """
        comm_id = kafka_load_consumables.load_consumable_all_board_no_wait(
            us.a_SP96XL1,
            sealing='true',
            load={'MGRK01': ('POS4',)})
        time.sleep(3)
        try:
            assert km.is_conform_to_task_msg(msg_tp='assist_complete',
                                             comm_id=comm_id,
                                             target_key='complete_status',
                                             target_value='success') is True
        except AssertionError as e:
            my_logger.error(e)


if __name__ == '__main__':
    pytest.main(['-s',
                 '-m load',
                 '--resultlog=reports/auto_test_report.txt',
                 '--junitxml=reports/auto_test_report.xml',
                 '--html=reports/auto_test_report.html',
                 '--alluredir=alluredir/'
                 ])
