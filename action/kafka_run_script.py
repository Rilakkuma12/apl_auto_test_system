#encoding=utf-8
import time
import uuid
from common.base import Base
import os
import io
import base64
from tools.handle_log import my_logger
from tools.constance import DATA_PATH
from tools.handle_task_id import my_task_id
from tools.handle_command_id import HandleCommandId
# __TASK_ID = my_task_id.get_task_id()
us = Base()
my_command_id = HandleCommandId()


class RunScript:
    __fmt_script = u'''{
            "message_id": "UUID",
            "message_type": "command",
            "message_group": "%s",
            "message_content": {
                "task_id": "%s",
                "task_class": "11",
                "module_id": "7",
                "device_type": "MGISP-96XLEX",
                "device_id": "%s",
                "command_id": "%s",
                "command": "run",
                "parameters": {
                    "script_code": "",
                    "script_name": "%s",
                    "script_content": "%s",
                    "final_script": "%s",
                    "arguments": {}
                }
            }
        }'''

    def __init__(self, task_id=my_task_id.get_task_id()):
        self.task_id = task_id

    def b64encode(self, path):
        abs = os.path.abspath(path)
        my_logger.info(abs)
        buff = ''
        with io.open(abs, mode='rt', encoding='utf-8') as f:
            for row in f.readlines():
                buff = buff + row
            # result = base64.b64encode(buff.encode('utf-8'))
            result = base64.b64encode(buff.encode('utf-8'))
            # print("BASE64加密串:\n" + str(result, 'utf-8'))
            return os.path.basename(path), str(result, 'utf-8')

    def start_script(self, device_id, path, if_final=False):
        command_id = my_command_id.get_command_id()
        info = self.b64encode(path)
        # global __fmt_script, __TASK_ID, __DEVICE_TYPE, __DEVICE_ID
        if if_final:
            msg = self.__fmt_script % (us.topic_task_lims, self.task_id, device_id, command_id, info[0], info[1], 'yes')
        else:
            msg = self.__fmt_script % (us.topic_task_lims, self.task_id, device_id, command_id, info[0], info[1], 'no')
        us.send(us.topic_task_lims, msg)
        __DEVICE_ID = device_id
        return command_id

    def run_script(self, device_id, path, if_final=False):
        com_id_run = self.start_script(device_id, DATA_PATH + path, if_final)
        my_logger.info('runScript, command id: {}'.format(com_id_run))
        us.wait_task_complete(us.consumer_task_apl, us.topic_task_apl, com_id_run)

    def run_script_no_wait(self, device_id, path, if_final=False):
        com_id_run = self.start_script(device_id, DATA_PATH + path, if_final)
        my_logger.info('runScript, command id: {}'.format(com_id_run))
        return com_id_run


if __name__ == "__main__":
    try:
        for i in range(1):
            # run_script(us.SP96XL1, 'spx96_pre_clean_cn_local_new.py')
            # run_script(us.a_SP96XL1, 'spx96_loadtips_aspirate.py')
            # run_script_no_wait(us.a_SP96XL1, 'spx96_home.py')
            # time.sleep(3)
            rr = RunScript()
            rr.run_script(us.b_SP96XL4, 'spx96_home.py')
            # run_script(us.a_SP96XL1, '3-2.Nifty_2板ER+LA+纯化+PCRmix_20190121-无富集.py')
    except Exception as e:
        my_logger.error(u'error: %s' % e)
