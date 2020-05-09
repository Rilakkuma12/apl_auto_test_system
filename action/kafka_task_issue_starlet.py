# encoding=utf-8
import uuid
from common.base import Base
import json
from tools.handle_log import HandleLogger
from action.kafka_load import KafkaLoad
from common.hotel_manage import HotelManage
from common.table_manage import TableManage
from tools.handle_task_id import my_task_id
from tools.handle_command_id import HandleCommandId
my_logger = HandleLogger()
my_hotel = HotelManage()
my_table = TableManage()
us = Base()
my_command_id = HandleCommandId()


class KafkaTaskIssue:
    topic = us.topic_task_lims
    turn = 0
    device_list = {
        'module1': us.a_SP96XL1,
        'module2': us.a_SP96XL2,
        'module3': us.a_SP96XL1,
        'interaction1': us.a_interaction,
        'interaction2': us.b_interaction
    }
    holder_type_all = ['slider', 'rack']
    # 1代表前区，2代表后区
    area_map = {'1': True, '2': False}

    __msg = '''
    {
        "message_id": "UUID",
        "message_type": "task_issue",
        "message_group": "%s",
        "message_content": {
            "task_id": "%s",
            "task_class": "",
            "module_id": "",
            "device_type": "STARlet",
            "device_id": "%s",
            "parameters": {
                "pcr_start": []
            }
        }
    }
    '''

    def task_issue(self, dest):
        __TASK_ID = my_task_id.get_task_id()
        msg = self.__msg % (us.topic_task_lims, __TASK_ID, dest)
        my_logger.info('task issue，task id：{}'.format(__TASK_ID))
        us.send(self.topic, msg)
        if us.wait_task_accept(us.consumer_task_apl, us.topic_task_apl, __TASK_ID):
            return __TASK_ID
        else:
            raise Exception('任务下发失败')


issue = KafkaTaskIssue()
if __name__ == '__main__':

    issue.task_issue(us.b_startlet)

