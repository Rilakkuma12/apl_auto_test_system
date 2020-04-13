#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2019/9/23 16:06
import time
from common.kafka_msg import km
import pytest
from action import kafka_run_script
from common import base as us
from handle_log import my_logger


@pytest.mark.run
class TestRunScript:
    def test_run_script_task(self):
        """
        1.前置条件
        2.发送脚本运行
        3.断言返回task running
        4.断言返回task complete success
        """
        comm_id = kafka_run_script.run_script_no_wait(us.a_SP96XL1, 'spx96_home.py')
        time.sleep(3)

        assert km.is_conform_to_task_msg(msg_tp='response',
                                         comm_id=comm_id,
                                         target_key='response',
                                         target_value='running') is True

        assert km.is_conform_to_task_msg(msg_tp='complete',
                                         comm_id=comm_id,
                                         target_key='complete_status',
                                         target_value='success') is True

    def test_run_script_output(self):
        """
        1.前置条件
        2.发送脚本运行
        3.断言返回脚本中report信息
        """
        comm_id = kafka_run_script.run_script_no_wait(us.a_SP96XL1, 'spx96_home.py')
        time.sleep(3)
        assert km.is_conform_to_script_output(msg_tp='output',
                                              comm_id=comm_id,
                                              target_key='desc',
                                              target_value='脚本开始') is True
        assert km.is_conform_to_script_output(msg_tp='output',
                                              comm_id=comm_id,
                                              target_key='desc',
                                              target_value='脚本结束') is True

    def test_pcr_mix_request(self):
        pass

    def test_transfer_request(self):
        pass


if __name__ == '__main__':
    pytest.main([
        '-s',
        '-m run',
        '--resultlog=reports/auto_test_report.txt',
        '--junitxml=reports/auto_test_report.xml',
        '--html=reports/auto_test_report.html',
        '--alluredir=alluredir/'
                 ])


