#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/7/26 13:42
from common import base as us
from tools.handle_log import my_logger
import time

command = ['Ingore', 'ClearCurrent', 'ClearAll']


def device_command(device_id, request_id, res):
    comm = '''{
        "message_type": "transfer_response",
        "message_group": "task_lims",
        "message_content": {
            "device_id": "%s",
            "request_id": "%s",
            "response": "%s"
        },
        "message_id": "2eb1116b01c94a24b6b53dd23a8e2195"
    }''' % (device_id, request_id, command[res])
    return comm


def handle_task_err(device, res):
    req_id = us.get_robot_request_exception_info()
    # req_id = '664cc44baa3343a8bc7c9b956c5b8d44'
    my_logger.debug('task exception handle: {}'.format(command[res]))
    msg = device_command(device, req_id, res)
    time.sleep(1)
    us.send(us.__topic_task_lims, msg)


if __name__ == '__main__':
    # 0 Ingore, 1 ClearCurrent, 2 ClearAll
    while True:
        handle_task_err(us.a_interaction, 0)

