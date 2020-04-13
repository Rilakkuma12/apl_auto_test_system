# -*- coding: UTF-8
from base import common as us
from action import kafka_load_consumables
from action import kafka_push_consumables
from action import kafka_device_command
from tools.handle_log import my_logger
from tools.handle_excel import HandleExcel
from tools.constance import TIME_RECORD_PATH

record_file = HandleExcel(TIME_RECORD_PATH)


if __name__ == '__main__':
    """
        测试逆向转移
        1、sp1上料
        2、sp1向sp2转移
        3、sp2向sp1转移
        2、sp1下料                   
    """
    try:
        for i in range(1):
            kafka_device_command.scan_hotel(us.a_HotelA)
            kafka_device_command.scan_hotel(us.a_HotelB)
            kafka_load_consumables.load_consumable_all_board(us.a_SP96XL1, load={'MGRK01': ('POS3',)})
            # kafka_transfer.transfer(us.a_SP96XL1, 'POS3', us.b_SP96XL4, 'POS4')
            # kafka_transfer.transfer(us.b_SP96XL4, 'POS4', us.a_SP96XL1, 'POS3')
            kafka_push_consumables.push_consumable_all_boards_only_for_simulate(us.a_SP96XL1, pos_num=1, push={'MGRK01': ('POS3',)})

    except Exception as e:
        my_logger.error(u'error: %s' % e)

