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
        测试机械臂队列是否在web上正确显示                 
    """
    try:
        kafka_device_command.scan_hotel(us.a_HotelA)
        kafka_device_command.scan_hotel(us.a_HotelB)
        kafka_device_command.scan_hotel(us.b_HotelA)
        kafka_device_command.scan_hotel(us.b_HotelB)
        for i in range(1):
            kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4,
                                                             load={'MGRK01': ('POS2', 'POS3', 'POS4', 'POS5'),
                                                                   'MGRK02': ('POS7', 'POS8', 'POS9', 'POS10'),
                                                                   'MGRK03': (
                                                                   'POS11', 'POS12', 'POS13', 'POS14', 'POS15')})
            kafka_load_consumables.load_consumable_all_board(us.a_SP96XL1,
                                                             load={'MGRK01': ('POS2', 'POS3', 'POS4', 'POS5'),
                                                                   'MGRK02': ('POS7', 'POS8', 'POS9', 'POS10'),
                                                                   'MGRK03': (
                                                                   'POS11', 'POS12', 'POS13', 'POS14', 'POS15')})
            kafka_push_consumables.push_consumable_all_boards_only_for_simulate(us.b_SP96XL4, pos_num=13,
                                                                                is_pro_area=True, push={
                                                            'MGRK01': ('POS2', 'POS3', 'POS4', 'POS5'),
                                                            'MGRK02': ('POS7', 'POS8', 'POS9', 'POS10'),
                                                            'MGRK03': ('POS11', 'POS12', 'POS13', 'POS14', 'POS15')})

            kafka_push_consumables.push_consumable_all_boards_only_for_simulate(us.a_SP96XL1, pos_num=13, is_pro_area=False,
                                                                                push={'MGRK01': ('POS2', 'POS3', 'POS4', 'POS5'),
                                                                                    'MGRK02': ('POS7', 'POS8', 'POS9', 'POS10'),
                                                                                    'MGRK03': ('POS11', 'POS12', 'POS13', 'POS14', 'POS15')})
    except Exception as e:
        my_logger.error(u'error: %s' % e)

