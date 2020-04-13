#encoding=utf-8
import uuid
from base import common as us
from datetime import datetime
from tools.handle_log import my_logger
from kafka_device_command import scan_hotel

__TASK_ID = (datetime.now().isoformat()).replace(':', '-')


def device_command_roll(hotel, rack):
    # 0 解锁 1 上锁 2 扫码 3 释放
    # command = ['roll', 'scan']
    command_id = uuid.uuid1()
    # rst = int(random()*3)
    comm = '''{
        "message_type": "device_command",
        "message_group": "storage_lims",
        "message_content": {
            "module_id": "1",
            "device_type": "Hotel",
            "device_id": "%s",
            "command_id": "%s",
            "command": "roll",
            "parameters": {
            "rack_idx": "%s"
            }
        },
        "message_id": "ce286c57670b4f1891e6df0758da630c"
        }
    ''' % (hotel, command_id, rack)
    return comm, command_id


def device_command_scan(hotel, rack):
    # 0 解锁 1 上锁 2 扫码 3 释放
    # command = ['roll', 'scan']
    command_id = uuid.uuid1()
    # rst = int(random()*3)
    comm = '''{
        "message_type": "device_command",
        "message_group": "storage_lims",
        "message_content": {
            "module_id": "1",
            "device_type": "Hotel",
            "device_id": "%s",
            "command_id": "%s",
            "command": "scan",
            "parameters": {
            "rack_idxs": [{
            "rack_idx": "%s"
            }]
            }
        },
        "message_id": "ce286c57670b4f1891e6df0758da630c"
        }
    ''' % (hotel, command_id, rack)
    return comm, command_id


def roll_single_rack(hotel, rack):
    msg_1, com_id = device_command_roll(hotel, rack)
    my_logger.info('roll one rack, command id: {}'.format(com_id))
    us.send(us.__topic_storage_lims, msg_1)
    us.wait_command_complete(us.consumer_storage_apl, us.__topic_storage_apl, com_id)
    my_logger.info('roll one rack completed!')


def scan_single_rack(hotel, rack):
    msg_1, com_id = device_command_scan(hotel, rack)
    my_logger.info('scan one rack, command id: {}'.format(com_id))
    us.send(us.__topic_storage_lims, msg_1)
    us.wait_command_complete(us.consumer_storage_apl, us.__topic_storage_apl, com_id)
    my_logger.info('scan one rack completed!')


if __name__ == "__main__":
    try:
        for i in range(1):
            # 扫单列
            # roll_single_rack(us.HotelA, '1')
            # scan_single_rack(us.HotelA, '1')
            scan_hotel(us.HotelB)

    except Exception as e:
        my_logger.error(u'error: %s' % e)
