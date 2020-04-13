#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2019/9/26 10:54
from common import base as us
from action import kafka_push_consumables, kafka_device_command, kafka_load_consumables, kafka_interaction
from action import kafka_transfer
from tools.handle_log import my_logger

if __name__ == '__main__':
    try:
        # 开锁
        kafka_device_command.unlock_hotel()
        kafka_device_command.unlock_hotel(us.a_HotelB)

        # 上锁
        kafka_device_command.lock_hotel()
        kafka_device_command.lock_hotel(us.a_HotelB)

        # 扫码
        kafka_device_command.scan_hotel()
        kafka_device_command.scan_hotel(us.a_HotelB)
        kafka_device_command.scan_hotel(us.b_HotelA)
        kafka_device_command.scan_hotel(us.b_HotelB)

        # 释放
        kafka_device_command.release_hotel()
        kafka_device_command.release_hotel(us.a_HotelB)

        for i in range(1):
            my_logger.info('cyc {} begin...'.format(i + 1))
            # 上料
            kafka_interaction.load_consumable_from_inter(us.a_SP96XL1, rack_idx='1', level_idx='1', rack_id='MGRK01', barcode='MGRK010001000001', load={'MGRK01': ('POS17',)})
            kafka_interaction.push_consumable_to_inter(us.a_SP96XL1, rack_idx='1', level_idx='1', rack_id='MGRK01', barcode='MGRK010001000001', push={'MGRK01': ('POS17',)})

            kafka_interaction.load_consumable_from_inter(us.a_SP96XL1, rack_idx='5', level_idx='1', barcode='MGPH010001000001', load={'MGPH01': ('POS5',)})
            kafka_interaction.push_consumable_to_inter(us.a_SP96XL1, rack_idx='5', level_idx='1', barcode='MGPH010001000001', push={'MGPH01': ('POS5',)})

            kafka_load_consumables.load_consumable_all_board(us.a_SP96XL1,
                                                             tearing='true',
                                                             sealing='true',
                                                             centrifuge='false',
                                                             load={'MGRK01': ('POS2',), 'MGRK02': ('POS3',), 'MGRK03': ('POS4',)})

            kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4, is_pro_area=False,
                                                             load={'MGRK01': ('POS2',), 'MGRK02': ('POS3',), 'MGRK03': ('POS4',)})
            # 转移
            kafka_transfer.transfer(us.a_SP96XL1, 'POS2', us.b_SP96XL4, 'POS7')
            kafka_transfer.transfer(us.a_SP96XL1, 'POS3', us.b_SP96XL4, 'POS8')
            kafka_transfer.transfer(us.a_SP96XL1, 'POS4', us.b_SP96XL4, 'POS9')

            kafka_transfer.transfer(us.b_SP96XL4, 'POS2', us.a_SP96XL1, 'POS7')
            kafka_transfer.transfer(us.b_SP96XL4, 'POS3', us.a_SP96XL1, 'POS8')
            kafka_transfer.transfer(us.b_SP96XL4, 'POS4', us.a_SP96XL1, 'POS9')

            # 下料
            kafka_push_consumables.push_consumable_all_boards_only_for_simulate(us.a_SP96XL1, pos_num=3, push={'MGRK01': ('POS7',), 'MGRK02': ('POS8',), 'MGRK03': ('POS9',)})
            kafka_push_consumables.push_consumable_all_boards_only_for_simulate(us.b_SP96XL4, pos_num=3, is_pro_area=False, push={'MGRK01': ('POS7',), 'MGRK02': ('POS8',), 'MGRK03': ('POS9',)})

            my_logger.info('cyc {} end...'.format(i + 1))

    except Exception as e:
        my_logger.error(u'error: %s' % e)
