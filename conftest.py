#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2019/9/23 15:57
import time

import pytest
from action import kafka_device_command, kafka_load_consumables
from action import kafka_push_consumables
from common import base as us
from handle_log import my_logger


@pytest.fixture(scope='class')
def init_app_load_consumables():
    my_logger.info('开始执行上料用例')
    kafka_device_command.scan_hotel()
    kafka_device_command.scan_hotel(us.a_HotelB)
    yield
    # 用例执行完后下料
    kafka_push_consumables.push_consumable_all_boards_only_for_simulate(
        us.a_SP96XL1, pos_num=3, push={'MGRK01': ('POS2', 'POS3', 'POS4')})
    my_logger.info('执行上料用例结束')


@pytest.fixture(scope='class')
def init_app_push_consumables():
    my_logger.info('开始执行上料用例')
    kafka_device_command.scan_hotel()
    kafka_device_command.scan_hotel(us.a_HotelB)
    kafka_load_consumables.load_consumable_all_board_no_wait(us.a_SP96XL1, load={'MGRK01': ('POS2', 'POS3', 'POS4')})
    yield
    # 用例执行完后下料
    kafka_push_consumables.push_consumable_all_boards_only_for_simulate(
        us.a_SP96XL1, pos_num=3, push={'MGRK01': ('POS2', 'POS3', 'POS4')})
    my_logger.info('执行上料用例结束')


@pytest.fixture(scope='class')
def init_app_hotel():
    my_logger.info('开始执行堆栈用例')
    yield
    kafka_device_command.release_hotel_no_wait()
    time.sleep(3)
    my_logger.info('执行堆栈用例结束')


@pytest.fixture(scope='class')
def init_app_device_log():
    my_logger.info('开始执行上料用例')
    kafka_device_command.scan_hotel()
    kafka_device_command.scan_hotel(us.a_HotelB)
    yield
    my_logger.info('执行上料用例结束')


@pytest.fixture(scope='class')
def init_app_startlet_bmg():
    my_logger.info('开始执行上料用例')
    kafka_device_command.scan_hotel()
    kafka_device_command.scan_hotel(us.a_HotelB)
    yield
    my_logger.info('执行上料用例结束')
