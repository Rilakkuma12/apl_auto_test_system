#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2019/9/27 9:43
from common.base import Base
from tools.handle_log import my_logger
import time
import uuid
us = Base()
# 0queue清理所有，1task清理当前，2plate忽略当前
clear_type = ['queue', 'task', 'plate']


def transfer_resp(task_id, req_id, clear_type_num, barcode, idx):
    comm_id = uuid.uuid1()
    comm = '''{
        "message_id": "UUID",
        "message_type": "transfer_response",
        "message_group": "%s",
        "message_content": {
            "task_id": "%s",
            "command_id": "%s",
            "request_id": "%s",
            "request": "plate_transfer",
            "response": "success|failure",
            "attributes": {
              "clear_type": "%s",
              "plate_barcode": "%s",
              "idx": "%s"
            }
        }
    } ''' % (us.topic_task_lims, task_id, comm_id, req_id, clear_type[clear_type_num], barcode, idx)
    return comm


def handle_task_err():
    while True:
        task_id, req_id, barcode, idx = us.get_robot_request_exception_info()
        if task_id is not None:
            break
    num = int(input('get a task err info, choose clear type?[0 clear queue，1 clear current，2 ignore current]: '))
    my_logger.debug('task exception handle: {}'.format(clear_type[num]))
    msg = transfer_resp(task_id, req_id, num, barcode, idx)
    # msg = transfer_resp('6187', 'dc83297030014e768edfe7f0b675040b', 2, 'MGPH010001000001', 16)
    time.sleep(1)
    us.send(us.topic_task_lims, msg)


def handle_task_err_temp():
    # while True:
    #     task_id, req_id, barcode, idx = us.get_robot_request_exception_info()
    #     if task_id is not None:
    #         break
    task_id, req_id, barcode, idx = ('1905', 'Node-0-0', 'BGMX040000000002', '1')
    num = int(input('get a task err info, choose clear type?[0 clear queue，1 clear current，2 ignore current]: '))
    my_logger.debug('task exception handle: {}'.format(clear_type[num]))
    msg = transfer_resp(task_id, req_id, num, barcode, idx)
    # msg = transfer_resp('6187', 'dc83297030014e768edfe7f0b675040b', 2, 'MGPH010001000001', 16)
    time.sleep(1)
    us.send(us.topic_task_lims, msg)


if __name__ == '__main__':
    while True:
        handle_task_err()
    # handle_task_err_temp()
