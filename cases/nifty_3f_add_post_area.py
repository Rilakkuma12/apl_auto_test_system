# -*- coding: UTF-8
from base import common as us
from action import kafka_load_consumables
from action import kafka_push_consumables
from action import kafka_device_command
from action import kafka_transfer
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
        # 开锁
        kafka_device_command.unlock_hotel()
        kafka_device_command.unlock_hotel(us.a_HotelB)

        # 上锁
        kafka_device_command.lock_hotel()
        kafka_device_command.lock_hotel(us.a_HotelB)

        # 扫码
        kafka_device_command.scan_hotel_no_wait()
        kafka_device_command.scan_hotel(us.a_HotelB)
        time.sleep(20)

        # 释放
        kafka_device_command.release_hotel()
        kafka_device_command.release_hotel(us.a_HotelB)

        # count = 1
        for i in range(1000):
            setattr(HandleExcel, 'current_row', i + 2)
            record_file.record_time(row=getattr(HandleExcel, 'current_row'), col=1, result=i + 1)
            my_logger.info('cyc {} begin...'.format(i + 1))
            # 上料
            kafka_interaction.load_consumable_from_inter(us.b_SP96XL4, rack_idx='3', level_idx='1', load={'BRMW01': ('POS5',)})
            kafka_interaction.push_consumable_to_inter(us.b_SP96XL4, rack_idx='1', level='1', push={'BRMW01': ('POS5',)})
            kafka_interaction.load_consumable_from_inter(us.a_SP96XL1, rack_idx='5', level_idx='5', barcode='MGPH010001000001', load={'MGPH01': ('POS5',)})

            kafka_load_consumables.load_consumable_all_board(us.a_SP96XL1,
                                                             load={'BRMW01': ('POS2',), 'DNDW01': ('POS3',), 'GETP01': ('POS4',)})
            kafka_load_consumables.load_consumable_all_board(us.a_SP96XL2,
                                                             load={'BRMW01': ('POS2',), 'DNDW01': ('POS3',), 'GETP01': ('POS4',)})
            kafka_load_consumables.load_consumable_all_board(us.a_SP96XL3,
                                                             load={'BRMW01': ('POS2',), 'DNDW01': ('POS3',), 'GETP01': ('POS4',)})

            # 转移
            kafka_transfer.transfer(us.a_SP96XL1, 'POS2', us.a_SP96XL2, 'POS7')
            kafka_transfer.transfer(us.a_SP96XL1, 'POS3', us.a_SP96XL2, 'POS8')
            kafka_transfer.transfer(us.a_SP96XL1, 'POS4', us.a_SP96XL2, 'POS9')
            kafka_transfer.transfer(us.a_SP96XL1, 'POS5', us.a_SP96XL2, 'POS10')

            kafka_transfer.transfer(us.a_SP96XL2, 'POS2', us.a_SP96XL3, 'POS7')
            kafka_transfer.transfer(us.a_SP96XL2, 'POS3', us.a_SP96XL3, 'POS8')
            kafka_transfer.transfer(us.a_SP96XL2, 'POS4', us.a_SP96XL3, 'POS9')
            kafka_transfer.transfer(us.a_SP96XL2, 'POS7', us.a_SP96XL3, 'POS12')
            kafka_transfer.transfer(us.a_SP96XL2, 'POS8', us.a_SP96XL3, 'POS13')
            kafka_transfer.transfer(us.a_SP96XL2, 'POS9', us.a_SP96XL3, 'POS14')
            kafka_transfer.transfer(us.a_SP96XL2, 'POS10', us.a_SP96XL3, 'POS15')

            # 下料
            kafka_push_consumables.push_consumable_all_boards(us.a_SP96XL3, push={'BRMW01': ('POS2', 'POS7', 'POS12'),
                                                                                  'DNDW01': ('POS3', 'POS8', 'POS13'),
                                                                                  'GETP01': ('POS4', 'POS9', 'POS14')})

            kafka_interaction.push_consumable_to_inter(us.a_SP96XL3, rack_idx='5', level='5', push={'MGPH01': ('POS15',)})

            my_logger.info('cyc {} end...'.format(i + 1))

    except Exception as e:
        my_logger.error(u'error: %s' % e)
