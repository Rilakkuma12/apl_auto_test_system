# -*- coding: UTF-8
from common import base as us
import time
from action import kafka_run_script
from action import kafka_load_consumables
from action import kafka_push_consumables
from action import kafka_run_script
from action import kafka_device_command
from action import kafka_transfer
import json
from datetime import datetime
from tools.handle_log import my_logger
import time
from tools.handle_excel import HandleExcel
from tools.constance import TIME_RECORD_PATH
from action import kafka_interaction

record_file = HandleExcel(TIME_RECORD_PATH)


if __name__ == '__main__':
    """
        堆栈、工位、冰箱、交互区、传递窗                    
    """
    try:
        for i in range(100000000000):
            my_logger.info('cyc {} begin...'.format(i + 1))
            # 开锁
            kafka_device_command.unlock_hotel(us.b_HotelA)
            kafka_device_command.unlock_hotel(us.b_HotelB)
            time.sleep(10)

            # 上锁
            kafka_device_command.lock_hotel(us.b_HotelA)
            kafka_device_command.lock_hotel(us.b_HotelB)
            time.sleep(10)

            # 扫码
            kafka_device_command.scan_hotel_no_wait(us.a_HotelA)
            kafka_device_command.scan_hotel(us.a_HotelB)
            time.sleep(5)

            # 释放
            kafka_device_command.release_hotel(us.b_HotelA)
            kafka_device_command.release_hotel(us.b_HotelB)
            time.sleep(10)

            my_logger.info('cyc {} end...'.format(i + 1))

    except Exception as e:
        my_logger.error(u'error: %s' % e)
