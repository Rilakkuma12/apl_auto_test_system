#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/6/3 19:53
import uuid
from common import base as us
from datetime import datetime
from tools.handle_log import my_logger
__TASK_ID = (datetime.now().isoformat()).replace(':', '-')


def command_scan_single_rack(hotel=us.a_HotelA):
    command_id = uuid.uuid1()
    comm = '''{
        "message_type": "device_command",
        "message_group": "storage_lims",
        "message_content": {
            "module_id": "Module1",
            "device_type": "Hotel",
            "device_id": "%s",
            "command_id": "%s",
            "command": "scan",
            "parameters": {
                "rack_idxs": [{
                    "rack_idx": "3"
                }, 
                {
                    "rack_idx": "4"
                }]
            }
        },
        "message_id": "776ae021b5a647238c7f2c06a90686e3"
    }''' % (hotel, command_id)
    return comm, command_id


def scan_hotel_single_rack(hotel=us.a_HotelA):
    msg_1, com_id = command_scan_single_rack(hotel)
    my_logger.info('scan one rack, command id: {}'.format(com_id))
    us.send(us.__topic_storage_lims, msg_1)
    us.wait_command_complete(us.consumer_storage_apl, us.__topic_storage_apl, com_id)
    my_logger.info('scan one rack completed!')


if __name__ == "__main__":
    try:
        scan_hotel_single_rack()
        # command_scan_single_rack()
        # command_scan_single_rack(us.a_HotelB)
        # time.sleep(20)
    except Exception as e:
        my_logger.error(u'error: %s\n' % e)

