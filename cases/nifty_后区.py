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
        1.AB开锁
        2.AB上锁
        3.AB扫码
        4.AB释放
        5.工位1上料
        6.工位1运行脚本
        7.工位2上料
        8.工位1向工位2转移
        9.asyn工位2运行脚本
        10.asyn同时判断如果工位2完成，则先转移工位2，否则工位1下料
        11.asyn同时判断如果工位2完成，则先转移工位2，否则工位1上料
        12.如果工位2完成，工位3上料，工位2向工位3转移，工位3运行脚本
        13.工位3下料                       
    """
    try:
        # # 开锁
        # kafka_device_command.unlock_hotel(us.b_HotelA)
        # kafka_device_command.unlock_hotel(us.b_HotelB)
        #
        # # 上锁
        # kafka_device_command.lock_hotel(us.b_HotelA)
        # kafka_device_command.lock_hotel(us.b_HotelB)

        # 扫码
        # kafka_device_command.scan_hotel_no_wait(us.b_HotelA)
        # kafka_device_command.scan_hotel(us.b_HotelB)

        # time.sleep(40)

        # # 释放
        # kafka_device_command.release_hotel(us.b_HotelA)
        # kafka_device_command.release_hotel(us.b_HotelB)

        # count = 1
        for i in range(1000):

            my_logger.info('cyc {} begin...'.format(i + 1))
            # 上料
            # kafka_interaction.load_consumable_from_inter(us.b_SP96XL4, rack_idx='5', level_idx='5', barcode='MGPH010001000001', load={'MGPH01': ('POS9',)})
            # 下料
            # kafka_interaction.push_consumable_to_inter(us.b_SP96XL4, rack_idx='5', level_idx='5', barcode='MGPH010001000001', push={'MGPH01': ('POS9',)})
            # kafka_interaction.load_consumable_from_inter(us.b_SP96XL4, rack_idx='1', level_idx='1', barcode='BGMX010001000001', load={'BGMX01': ('POS19',)})
            # kafka_interaction.push_consumable_to_inter(us.b_SP96XL4, rack_idx='1', level_idx='1', barcode='BGMX010001000001', push={'BGMX01': ('POS19',)})

            # kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4,
            #                                                  is_pro_area=False,
            #                                                  load={
            #                                                        'GETF01': ('POS4',)})

            # kafka_push_consumables.push_consumable_all_boards(us.b_SP96XL4,
            #                                                   is_pro_area=False,
            #                                                   sealing=False,
            #                                                   push={
            #                                                         'GETF01': ('POS4',)})
            # kafka_load_consumables.load_consumable_all_board(us.b_SP100,
            #                                                  is_pro_area=False,
            #                                                  tearing=True,
            #                                                  sealing=False,
            #                                                  load={'BRMW01': ('POS7',), 'DNDW01': ('POS9',)})
            # kafka_push_consumables.push_consumable_all_boards(us.b_SP96XL4,
            #                                                   is_pro_area=False,
            #                                                   sealing=False,
            #                                                   push={'BRMW01': ('POS14',), 'DNDW01': ('POS15',)})

            # kafka_transfer.transfer(us.b_SP96XL4, 'POS14', us.b_SP100, 'POS2')
            # kafka_transfer.transfer(us.b_SP96XL4, 'POS3', us.b_SP100, 'POS3')
            #

            # kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4,
            #                                                  is_pro_area=False,
            #                                                  load={'BRMW01': ('POS2',), 'DNDW01': ('POS3',), 'GETF01': ('POS4',)})
            # kafka_transfer.transfer(us.b_SP96XL4, 'POS2', us.b_SP100, 'POS2')
            # kafka_push_consumables.push_consumable_all_boards(us.b_SP96XL4,
            #                                                   is_pro_area=False,
            #                                                   sealing=False,
            #                                                   push={'BRMW01': ('POS2',), 'DNDW01': ('POS3',), 'GETF01': ('POS4',)})
            # kafka_push_consumables.push_consumable_all_boards(us.b_SP96XL4,
            #                                                   is_pro_area=False,
            #                                                   push={'GETF01': ('POS4',)})
            #
            # # # # # # # kafka_load_consumables.load_consumable_all_board_no_wait(us.b_SP96XL4,
            # # # # # #                                                  is_pro_area=False,
            # # # # #                                                  tearing='false',
            # # # #                                                  sealing='false',
            # # #                                                  load={'GETP01': ('POS4', 'POS3', 'POS9', 'POS8'),
            # #                                                        'BRMW01': ('POS38', 'POS39'),
            #                                                        'DNDW01': ('POS27', 'POS32', 'POS26', 'POS31')})
            # time.sleep(600)  # 10min

            # kafka_push_consumables.push_consumable_all_boards_no_wait(us.b_SP96XL4,
            #                                                   is_pro_area=False,
            #                                                   tearing='false',
            #                                                   sealing='false',
            #                                                   push={'BRMW01': ('POS38', 'POS39'),
            #                                                         'GETP01': ('POS8', 'POS9', 'POS3', 'POS4'),
            #                                                         'DNDW01': ('POS27', 'POS32', 'POS26', 'POS31')})
            # time.sleep(600)
            # 滑块
            kafka_interaction.load_2_consumable_from_inter_slider()
            kafka_interaction.push_consumable_to_inter(us.b_SP100, hotel=us.b_interaction, rack_idx='1', level_idx='1',
                                                       rack_id='BRMW01', barcode='BRMW010001000001', push={'BRMW01': ('POS4',)})
            kafka_interaction.push_consumable_to_inter(us.b_SP100, hotel=us.b_interaction, rack_idx='3', level_idx='1',
                                                       rack_id='BRMW01', barcode='BRMW010001000001', push={'BRMW01': ('POS5',)})

            # 交互区rack
            kafka_interaction.load_consumable_from_inter(us.b_SP100, src=us.b_interaction, rack_idx='5', level_idx='5',
                                                         load={'MGPH01': ('POS3',)})
            kafka_interaction.push_consumable_to_inter(us.b_SP100, hotel=us.b_interaction, rack_idx='5', level_idx='5',
                                                       push={'MGPH01': ('POS3',)})
            kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4,
                                                             is_pro_area=False,
                                                             load={'GETP01': ('POS4', 'POS3', 'POS9', 'POS8'),
                                                                   'DNDW01': ('POS25', 'POS15', 'POS27', 'POS32', 'POS26'),
                                                                   'BRMW01': ('POS38', 'POS39', 'POS17', 'POS22')
                                                                   })
            kafka_transfer.transfer(us.b_SP96XL4, 'POS4', us.b_SP100, 'POS5')
            kafka_push_consumables.push_consumable_all_boards(us.b_SP96XL4,
                                                              is_pro_area=False,
                                                              push={'GETP01': ('POS8', 'POS9', 'POS3'),
                                                                    'DNDW01': ('POS25', 'POS15', 'POS27', 'POS32', 'POS26'),
                                                                    'BRMW01': ('POS38', 'POS39', 'POS17', 'POS22')
                                                                    })
            kafka_load_consumables.load_consumable_all_board(us.b_SP100,
                                                             is_pro_area=False,
                                                             load={'GETF01': ('POS4',),
                                                                   'BRMW01': ('POS9',),
                                                                   'DNDW01': ('POS7',)})
            kafka_push_consumables.push_consumable_all_boards(us.b_SP100,
                                                              is_pro_area=False,
                                                              push={'DNDW01': ('POS7',),
                                                                    'GETP01': ('POS4', 'POS5'),
                                                                    'BRMW01': ('POS9',)
                                                                    })
            # kafka_load_consumables.load_consumable_all_board(us.b_startlet, is_pro_area=False, load={'CRAP03': ('POS1',)})

            # kafka_load_consumables.load_consumable_all_board(us.b_startlet,
            #                                                  is_pro_area=False,
            #                                                  load={
            #                                                        'BRMW01': ('POS13', 'POS14'),
            #                                                        'DNDW01': ('POS18',)
            #                                                        })
            # kafka_push_consumables.push_consumable_all_boards(us.b_startlet,
            #                                                   is_pro_area=False,
            #                                                   push={
            #                                                         'BRMW01': ('POS13', 'POS14'),
            #                                                         'DNDW01': ('POS18',)
            #                                                         })
            # kafka_load_consumables.load_consumable_all_board(us.b_startlet,
            #                                                  is_pro_area=False,
            #                                                  load={
            #                                                        'CRAP02': ('POS2',),
            #                                                        'EDUV01': ('POS11',)
            #                                                        })
            # kafka_push_consumables.push_consumables_startlet()
            # time.sleep(480)  # 等待8min
            # kafka_push_consumables.push_consumable_all_boards(us.b_startlet,
            #                                                   is_pro_area=False,
            #                                                   push={
            #                                                         'CRAP02': ('POS2',),
            #                                                         'EDUV01': ('POS11',)
            #                                                         })
            # kafka_load_consumables.load_consumable_all_board(us.b_startlet,
            #                                                  is_pro_area=False,
            #                                                  load={'CRTP03': ('POS1',),
            #                                                        'CRTP01': ('POS2', 'POS4', 'POS5'),
            #                                                        'DNDW01': ('POS11', 'POS12', 'POS13', 'POS14')
            #                                                        })
            # , 'GETP01': ('POS4',), 'GETF01': ('POS5',)
            # kafka_load_consumables.load_consumable_all_board(us.b_SP100,
            #                                                  is_pro_area=False,
            #                                                  load={'BRMW01': ('POS2',), 'DNDW01': ('POS3',), 'GETP01': ('POS4',)})
            # kafka_load_consumables.load_consumable_all_board(us.b_startlet,
            #                                                  is_pro_area=False,
            #                                                  load={'EDUV01': ('POS2', 'POS3')})

            # 转移
            # kafka_transfer.transfer(us.a_SP96XL1, 'POS2', us.a_SP96XL2, 'POS7')
            # kafka_transfer.transfer(us.a_SP96XL1, 'POS3', us.a_SP96XL2, 'POS8')
            # kafka_transfer.transfer(us.a_SP96XL1, 'POS4', us.a_SP96XL2, 'POS9')
            # kafka_transfer.transfer(us.a_SP96XL1, 'POS5', us.a_SP96XL2, 'POS10')
            #
            # kafka_transfer.transfer(us.a_SP96XL2, 'POS7', us.a_SP96XL3, 'POS7')
            # kafka_transfer.transfer(us.a_SP96XL2, 'POS8', us.a_SP96XL3, 'POS8')
            # kafka_transfer.transfer(us.a_SP96XL2, 'POS9', us.a_SP96XL3, 'POS9')
            # kafka_transfer.transfer(us.a_SP96XL2, 'POS2', us.a_SP96XL3, 'POS12')
            # kafka_transfer.transfer(us.a_SP96XL2, 'POS3', us.a_SP96XL3, 'POS13')
            # kafka_transfer.transfer(us.a_SP96XL2, 'POS4', us.a_SP96XL3, 'POS14')

            # kafka_push_consumables.push_consumable_all_boards(us.b_SP96XL4,
            #                                                   is_pro_area=False,
            #                                                   tearing='false',
            #                                                   sealing='false',
            #                                                   push={'BRMW01': ('POS2',), 'DNDW01': ('POS3',), 'GETP01': ('POS4',)})
            # , 'GETP01': ('POS4',), 'GETF01': ('POS5',)
            # kafka_push_consumables.push_consumable_all_boards(us.b_SP100,
            #                                                   is_pro_area=False,
            #                                                   push={'BRMW01': ('POS2',), 'DNDW01': ('POS3',),
            #                                                         'GETP01': ('POS4',)})
            # kafka_push_consumables.push_consumable_all_boards(us.b_startlet,
            #                                                   is_pro_area=False,
            #                                                   push={'EDUV01': ('POS2', 'POS3')})
            # kafka_load_consumables.load_consumable_all_board_no_wait(us.a_SP96XL1,
            #                                                          is_pro_area=True,
            #                                                          sealing='false',
            #                                                          tearing='false',
            #                                                          load={'GETP01': ('POS4', 'POS3', 'POS9', 'POS8'),
            #                                                                'DNDW01': (
            #                                                                    'POS25', 'POS15', 'POS27', 'POS32',
            #                                                                    'POS26', 'POS31'),
            #                                                                'BRMW01': (
            #                                                                    'POS38', 'POS39', 'POS17', 'POS22')
            #                                                                })
            my_logger.info('cyc {} end...'.format(i + 1))

    except Exception as e:
        my_logger.error(u'error: %s' % e)
