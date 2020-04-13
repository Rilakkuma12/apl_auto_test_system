#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2019/8/21 16:33
from base import common as us
from action import kafka_load_consumables
from action import kafka_push_consumables
from action import kafka_interaction

"""
测试跨区上下料:
    上料：
    前区交互区<-->后区工位
    前区堆栈<-->后区工位
    前区冰箱<-->后区工位
    下料：
    前区工位<-->后区堆栈
    前区工位<-->后区交互区
    前区工位<-->后区冰箱
"""


def main():
    # 前区交互区 < -->后区工位
    kafka_interaction.load_consumable_from_inter(us.b_SP96XL4, rack_idx='1', level_idx='1', rack_id='MGRK01',
                                                 barcode='MGRK010001000001', load={'MGRK01': ('POS17',)})
    kafka_interaction.push_consumable_to_inter(us.b_SP96XL4, rack_idx='1', level_idx='1', rack_id='MGRK01',
                                               barcode='MGRK010001000001', push={'MGRK01': ('POS17',)})

    # 前区堆栈 < -->后区工位
    kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4, is_pro_area=True, load={'MGRK01': ('POS2',)})
    kafka_push_consumables.push_consumable_all_boards_only_for_simulate(us.b_SP96XL4, pos_num=1, is_pro_area=True,
                                                                        push={'MGRK01': ('POS2',)})

    # 前区冰箱 < -->后区工位

    # 前区工位 < -->后区交互区

    # 前区工位 < -->后区堆栈
    kafka_load_consumables.load_consumable_all_board(us.a_SP96XL1, is_pro_area=False, load={'MGRK01': ('POS2',)})
    kafka_push_consumables.push_consumable_all_boards_only_for_simulate(us.a_SP96XL1, pos_num=1, is_pro_area=False,
                                                                        push={'MGRK01': ('POS2',)})

    # 前区工位 < -->后区冰箱


if __name__ == '__main__':
    # 要先扫码
    # kafka_device_command.scan_hotel_no_wait()
    # kafka_device_command.scan_hotel(us.a_HotelB)
    # kafka_device_command.scan_hotel(us.b_HotelA)
    # kafka_device_command.scan_hotel(us.b_HotelB)

    main()
