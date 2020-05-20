#encoding=utf-8
import uuid
from datetime import datetime
from tools.handle_log import my_logger
from common.base import Base
from tools.handle_command_id import my_comm_id

us = Base()
__TASK_ID = (datetime.now().isoformat()).replace(':', '-')
# __TASK_ID = ''
# new_logger = handle_logger()


def device_command(hotel, rst):
    # 0 解锁 1 上锁 2 扫码 3 释放
    command = ['unlock', 'locked', 'scan', 'release']
    command_id = my_comm_id.get_command_id()
    # rst = int(random()*3)
    comm = '''{
        "message_id": "UUID",
        "message_type": "device_command",
        "message_group": "%s",
        "message_content": {
            "module_id": "7",
            "device_type": "Hotel",
            "device_id": "%s",
            "command_id": "%s",
            "command": "%s",
            "parameters": {
                "rack_idxs": []
            }
        }
    }
    ''' % (us.topic_storage_lims, hotel, command_id, command[rst])
    return comm, command_id


def device_command_cytomat(hotel, rst):
    # 0 解锁 1 上锁 2 扫码 3 释放
    command = ['scan_refridge']
    command_id = my_comm_id.get_command_id()
    # rst = int(random()*3)
    comm = '''{
        "message_id": "UUID",
        "message_type": "device_command",
        "message_group": "%s",
        "message_content": {
            "module_id": "7",
            "device_type": "Cytomat",
            "device_id": "%s",
            "command_id": "%s",
            "command": "%s",
            "parameters": {
                "rack_idxs": []
            }
        }
    }
    ''' % (us.topic_storage_lims, hotel, command_id, command[rst])
    return comm, command_id


def unlock_hotel(hotel=us.a_HotelA):
    # 开锁
    # await asyncio.sleep(0)
    msg0, com_id0 = device_command(hotel, 0)
    my_logger.info('unlock door, command id: {}'.format(com_id0))
    us.send(us.topic_storage_lims, msg0)
    return us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id0)


def unlock_hotel_no_wait(hotel=us.a_HotelA):
    # 开锁
    # await asyncio.sleep(0)
    msg0, com_id0 = device_command(hotel, 0)
    my_logger.info('unlock door, command id: {}'.format(com_id0))
    us.send(us.topic_storage_lims, msg0)
    return com_id0


def unlock_hotel_a_and_b():
    # 开锁
    msg0, com_id0 = device_command(us.a_HotelA, 0)
    my_logger.info('open_door_a, command id: {}'.format(com_id0))

    msg1, com_id1 = device_command(us.a_HotelB, 0)
    my_logger.info('open_door_b, command id: {}'.format(com_id1))

    us.send(us.topic_storage_lims, msg0)
    us.send(us.topic_storage_lims, msg1)

    us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id0)
    us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id1)


def lock_hotel(hotel=us.a_HotelA):
    # 上锁
    msg1, com_id1 = device_command(hotel, 1)
    my_logger.info('lock door, command id: {}'.format(com_id1))
    us.send(us.topic_storage_lims, msg1)
    return us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id1)


def lock_hotel_no_wait(hotel=us.a_HotelA):
    # 上锁
    msg1, com_id1 = device_command(hotel, 1)
    my_logger.info('lock door, command id: {}'.format(com_id1))
    us.send(us.topic_storage_lims, msg1)
    return com_id1


def lock_hotel_a_and_b():
    # 上锁
    msg0, com_id0 = device_command(us.a_HotelA, 1)
    my_logger.info('lock door, command id: {}'.format(com_id0))

    msg1, com_id1 = device_command(us.a_HotelB, 1)
    my_logger.info('close_door, command id: {}'.format(com_id1))

    us.send(us.topic_storage_lims, msg0)
    us.send(us.topic_storage_lims, msg1)

    us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id0)
    us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id1)


def release_hotel(hotel=us.a_HotelA):
    # 释放
    # await asyncio.sleep(0)
    msg3, com_id3 = device_command(hotel, 3)
    my_logger.info('release, command id: {}'.format(com_id3))
    us.send(us.topic_storage_lims, msg3)
    return us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id3)


def release_hotel_no_wait(hotel=us.a_HotelA):
    # 释放
    msg3, com_id3 = device_command(hotel, 3)
    my_logger.info('release, command id: {}'.format(com_id3))
    us.send(us.topic_storage_lims, msg3)
    return com_id3


def release_hotel_a_and_b():
    # 释放
    msg0, com_id0 = device_command(us.a_HotelA, 3)
    my_logger.info('release, command id: {}'.format(com_id0))

    msg3, com_id3 = device_command(us.a_HotelB, 3)
    my_logger.info('release, command id: {}'.format(com_id3))

    us.send(us.topic_storage_lims, msg0)
    us.send(us.topic_storage_lims, msg3)

    us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id0)
    us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id3)


def scan_hotel(hotel=us.a_HotelA):
    # 扫码
    # await asyncio.sleep(0)
    msg2, com_id2 = device_command(hotel, 2)
    my_logger.info('scan, command id: {}'.format(com_id2))
    us.send(us.topic_storage_lims, msg2)
    return us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id2)


def scan_cytomat(hotel=us.a_CytomatA):
    # 扫码
    # await asyncio.sleep(0)
    msg2, com_id2 = device_command_cytomat(hotel, 0)
    my_logger.info('scan, command id: {}'.format(com_id2))
    us.send(us.topic_storage_lims, msg2)
    return us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id2)


def scan_cytomat_no_wait(hotel=us.a_CytomatA):
    # 扫码
    # await asyncio.sleep(0)
    msg2, com_id2 = device_command_cytomat(hotel, 0)
    my_logger.info('scan, command id: {}'.format(com_id2))
    us.send(us.topic_storage_lims, msg2)


def scan_hotel_no_wait(hotel=us.a_HotelA):
    # 扫码
    msg2, com_id2 = device_command(hotel, 2)
    my_logger.info('scan, command id: {}'.format(com_id2))
    us.send(us.topic_storage_lims, msg2)
    return com_id2


def scan_hotel_a_and_b():
    # 扫码a
    msg1, com_id1 = device_command(us.a_HotelA, 2)
    my_logger.info('scanA, command id: {}'.format(com_id1))

    # 扫码b
    msg2, com_id2 = device_command(us.a_HotelB, 2)
    my_logger.info('scanB, command id: {}'.format(com_id2))

    us.send(us.topic_storage_lims, msg1)
    us.send(us.topic_storage_lims, msg2)

    us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id1)
    us.wait_command_complete(us.consumer_storage_apl, us.topic_storage_apl, com_id2)


if __name__ == "__main__":
    try:
        for i in range(1):
            scan_hotel(us.b_HotelA)
            # scan_hotel_no_wait()
            scan_hotel(us.b_HotelB)
            # scan_hotel_no_wait(us.b_HotelA)
            # scan_hotel(us.b_HotelB)
            # scan_cytomat(us.a_CytomatA)
    except Exception as e:
        my_logger.error(u'error: %s' % e)

