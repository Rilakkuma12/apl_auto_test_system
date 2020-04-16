#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/8/9 13:15
import uuid
from tools.handle_log import my_logger
from common.base import Base
import time
command_inter = ['success', 'failure']
us = Base()


def device_command_inter_response_fail(request_id, dest, pos, src, rack, level):
    command_id = uuid.uuid1()
    comm = '''{
            "message_type":"load_response",
            "message_group":"%s",
            "message_content":{
                "task_id":"100",
                "command_id":"%s",
                "request_id":"%s",
                "response":"failure",
                "response_time":"2019-08-08 10:20:15",
                "msg":"",
                "attributes":{
                    "target_device_id":"%s",
                    "position":"%s",
                    "source_device_id":"%s",
                    "rack_idx":"%s",
                    "level_idx":"%s"
                }
            },
            "message_id":"fb7c8125c9ba463a8654da90cf9e867c"
        }''' % (us.topic_task_lims, command_id, request_id, dest, pos, src, rack, level)
    return comm


def device_command_inter_response_success(request_id, is_throw_away):
    command_id = uuid.uuid1()
    comm = '''{
            "message_type":"load_response",
            "message_group":"%s",
            "message_content":{
                "task_id":"100",
                "command_id":"%s",
                "request_id":"%s",
                "response":"success",
                "response_time":"2019-08-08 10:20:15",
                "msg":"",
                "attributes":{
                    "throw_away": "%s"
                }
            },
            "message_id":"fb7c8125c9ba463a8654da90cf9e867c"
        }''' % (us.topic_task_lims, command_id, request_id, is_throw_away)
    return comm


def handle_load_from_inter_request(is_continue, is_throw_away):
    request_id, dest, pos, barcode, src, rack, level = us.get_inter_request_info()
    # level = str(int(level) - 1)
    if is_continue:
        my_logger.debug('load_from_inter_request handle: {}'.format('continue'))
        msg = device_command_inter_response_success(request_id, is_throw_away)
    else:
        my_logger.debug('load_from_inter_request handle: {}'.format('back'))
        msg = device_command_inter_response_fail(request_id, dest, pos, src, rack, level)
    time.sleep(1)
    us.send(us.topic_task_lims, msg)


if __name__ == '__main__':
    while True:
        handle_load_from_inter_request(is_continue=True, is_throw_away='true')
