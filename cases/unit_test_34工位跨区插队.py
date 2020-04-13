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
        前提：需开启脚本kafka_pcr_mix.py
        1.工位3上料
        2.请求pcr-mix
        3.进行pcr-mix并同时工位4上料
        4.pcr-mix结束后工位3下料，同时工位4上料完毕，发送跨区插队任务                     
    """
    try:
        # # 扫码
        # kafka_device_command.scan_hotel_no_wait()
        # # kafka_device_command.scan_hotel_no_wait(us.b_HotelA)
        # kafka_device_command.scan_hotel(us.a_HotelB)
        # # kafka_device_command.scan_hotel(us.b_HotelB)
        # time.sleep(50)
        # 'BGTE01': ('POS15',),
        # 'BGBD01': ('POS28', 'POS33', 'POS27', 'POS32'),
        # 'BGEZ01': ('POS37', 'POS38', 'POS40'),
        # 'BGMX01': ('POS17', 'POS22')
        # 'BGTE01': ('POS36', 'POS37', 'POS38', 'POS39'),
        # 'BGBD01': ('POS28', 'POS33', 'POS27', 'POS32'),
        # 'BGEZ01': ('POS37', 'POS38', 'POS39', 'POS40'),

        # 工位3上料
        # kafka_load_consumables.load_consumable_all_board(us.a_SP96XL3,
        #                                                  load={'GETF01': ('POS4', 'POS3', 'POS2', 'POS9', 'POS8', 'POS7'),
        #                                                        'BGBD01': ('POS25',),
        #                                                        'BRMW01': ('POS26', 'POS31', 'POS36', 'POS39')
        #                                                        })
        # kafka_run_script.run_script(us.a_SP96XL3, 'spx96_pcr_mix_request.py')

        # 工位3下料
        kafka_push_consumables.push_consumable_all_boards(us.a_SP96XL3,
                                                          push={
                                                                'GETF01': ('POS7', 'POS8', 'POS9', 'POS2', 'POS3', 'POS4'),
                                                                'BGBD01': ('POS25',),
                                                                'BRMW01': ('POS36', 'POS39')
                                                                              })

    except Exception as e:
        my_logger.error(u'error: %s' % e)
