#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2019/8/21 16:33
from base import common as us
from action import kafka_load_consumables


def main():
    # kafka_device_command.scan_hotel()
    # kafka_device_command.scan_hotel(us.a_HotelB)
    # 前区堆栈 < -->后区工位
    kafka_load_consumables.load_consumable_all_board_no_wait(us.b_SP96XL4, is_pro_area=True, load={'MGRK01': ('POS2', 'POS3', 'POS4')})
    kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4, is_pro_area=True, load={'MGRK01': ('POS7', 'POS8', 'POS9')})
    kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4, is_pro_area=True,
                                                     load={'MGRK02': ('POS12', 'POS13', 'POS14')})
    # kafka_push_consumables.push_consumable_all_boards_only_for_simulate(us.b_SP96XL4, pos_num=1, is_pro_area=True,
    #                                                                     push={'MGRK01': ('POS2',)})


if __name__ == '__main__':
    # 要先扫码
    # kafka_device_command.scan_hotel_no_wait()
    # kafka_device_command.scan_hotel(us.a_HotelB)
    # kafka_device_command.scan_hotel(us.b_HotelA)
    # kafka_device_command.scan_hotel(us.b_HotelB)

    main()
