# encoding=utf-8
import random
import time
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
# my_hotel = HotelManage()
# my_table = TableManage()
us = Base()
my_command_id = HandleCommandId()


class KafkaControlBuzzer:
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

    __msg = '''{
        "message_id":"UUID",
        "message_type":"buzzer_lamp",
        "message_group":"%s",
        "message_content":{
            "module_id":"7",
            "device_id":"%s",
            "buzzer_switch":"%s",
            "lamp_color":"%s",
            "alert_time":"2020-5-20 11:02:00"
        }
    }'''
    msg = json.loads(__msg)  # 把msg转换为字典
    load_list = msg['message_content']['parameters']['inputs']

    sealing = False
    tear = False
    centrifugal = False
    centrifuge_pn = ''

    def control_buzzer(self, device_id, buzzer, lamp_color, topic=us.topic_device):
        msg = self.__msg % (topic, device_id, buzzer, lamp_color)
        us.send(us.topic_device, msg)


aa = KafkaControlBuzzer()
if __name__ == '__main__':
    # "buzzer_switch": "on|off ",
    # "lamp_color": "green|yellow|red ",
    aa.control_buzzer(us.a_interaction, 'on', 'red')
    time.sleep(5)
    aa.control_buzzer(us.a_interaction, 'off', 'yellow')

