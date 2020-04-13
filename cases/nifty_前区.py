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
        # # 开锁
        # kafka_device_command.unlock_hotel(us.b_HotelA)
        # kafka_device_command.unlock_hotel(us.b_HotelB)

        # 上锁
        # kafka_device_command.lock_hotel(us.b_HotelA)
        # kafka_device_command.lock_hotel(us.b_HotelB)
        #
        # 扫码
        # kafka_device_command.scan_hotel_no_wait(us.a_HotelA)
        # kafka_device_command.scan_hotel(us.a_HotelB)
        # time.sleep(20)

        # # 释放
        # kafka_device_command.release_hotel(us.b_HotelA)
        # kafka_device_command.release_hotel(us.b_HotelB)

        # count = 1
        for i in range(1):

            my_logger.info('cyc {} begin...'.format(i + 1))
            # kafka_load_consumables.load_consumable_all_board(us.a_SP96XL3,
            #                                                  is_cytomat=False,
            #                                                  load={'BRMW01': ('POS10',),
                                                                    # 'BGBD01': ('POS9',)
                                                                   # })
            # kafka_load_consumables.load_consumable_all_board(us.a_SP96XL1,
            #                                                  load={'GETF01': ('POS2', 'POS3', 'POS4')})
            # kafka_load_consumables.load_consumable_all_board(us.a_SP96XL2,
            #                                                  load={'GETF01': ('POS2', 'POS3', 'POS4', 'POS5')})
            # kafka_push_consumables.push_consumable_all_boards(us.a_SP96XL1,
            #                                                   push={'GETF01': ('POS2', 'POS3', 'POS4')})

            # kafka_push_consumables.push_consumable_all_boards(us.a_SP96XL2,
            #                                                   push={'GETF01': ('POS2', 'POS3', 'POS4', 'POS5')})
            # 工位1上料
            # kafka_load_consumables.load_consumable_all_board_no_wait(us.a_SP96XL1,
            #                                                          load={'GETF01': ('POS4', 'POS2', 'POS9', 'POS7'),
            #                                                                'DNDW01': ('POS11', 'POS13', 'POS18', 'POS23', 'POS25', 'POS26', 'POS27', 'POS28', 'POS29', 'POS12')})
            # 工位1转移
            # kafka_transfer.transfer(us.a_SP96XL3, 'POS10', us.b_SP96XL4, 'POS10')
            # kafka_transfer.transfer(us.a_SP96XL3, 'POS9', us.b_SP96XL4, 'POS9')
            # 工位1转移
            # kafka_transfer.transfer(us.a_SP96XL1, 'POS18', us.a_SP96XL2, 'POS17')
            # kafka_transfer.transfer(us.a_SP96XL1, 'POS23', us.a_SP96XL2, 'POS22')
            # 工位1下料  'POS18', 'POS23',
            # kafka_push_consumables.push_consumable_all_boards(us.a_SP96XL1,
            #                                                          push={'GETF01': ('POS7', 'POS9', 'POS2', 'POS4'),
            #                                                                'DNDW01': ('POS11', 'POS13','POS25', 'POS26', 'POS27', 'POS28', 'POS29', 'POS12')})
            # 工位2上料
            # kafka_load_consumables.load_consumable_all_board_no_wait(us.a_SP96XL1,
            #                                                          load={'GETF01': ('POS5', 'POS4', 'POS10', 'POS9', 'POS8', 'POS7'),
            #                                                                'DNDW01': (
            #                                                                'POS25', 'POS13', 'POS14', 'POS28', 'POS29', 'POS19'
            #                                                                'POS24', 'POS33', 'POS34'),
            #                                                                'BRMW01': ('POS17', 'POS22')
            #                                                                })
            # 工位3上料
            # kafka_load_consumables.load_consumable_all_board_no_wait(us.a_SP96XL1,
            #                                                          load={'GETF01': ('POS4', 'POS3', 'POS2', 'POS9', 'POS8', 'POS7'),
            #                                                                'DNDW01': (
            #                                                                    'POS7', 'POS15', 'POS28', 'POS33',
            #                                                                    'POS27', 'POS32'),
            #                                                                'BRMW01': ('POS26', 'POS31', 'POS36', 'POS39', 'POS37', 'POS38', 'POS40', 'POS17', 'POS22')
            #                                                                })

            my_logger.info('cyc {} end...'.format(i + 1))

    except Exception as e:
        my_logger.error(u'error: %s' % e)
