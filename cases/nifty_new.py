# -*- coding: UTF-8
from base import common as us
from action import kafka_load_consumables
from action import kafka_push_consumables
from action import kafka_run_script
from action import kafka_device_command
from action import kafka_transfer
from tools.handle_log import my_logger


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
        # kafka_device_command.unlock_hotel(us.a_HotelB)

        # 上锁
        kafka_device_command.lock_hotel()

        # 扫码
        kafka_device_command.scan_hotel()
        kafka_device_command.scan_hotel(us.a_HotelB)
        kafka_device_command.scan_hotel(us.b_HotelA)
        kafka_device_command.scan_hotel(us.b_HotelB)

        # 释放
        kafka_device_command.release_hotel()
        count = 1
        for i in range(10000):
            my_logger.info('cyc {} begin...'.format(count))
            # 上料
            kafka_load_consumables.load_consumable_all_board(us.a_SP96XL1, load={'MGRK01': ('POS3', 'POS2'), 'MGRK02': ('POS12', 'POS20')})
            # 运行脚本
            kafka_run_script.run_script(us.a_SP96XL1, 'spx96_pre_clean_cn_local_new.py')

            # 转移
            kafka_transfer.transfer(us.a_SP96XL1, 'POS2', us.b_SP96XL4, 'POS17')

            kafka_transfer.transfer(us.b_SP96XL4, 'POS17', us.a_SP96XL1, 'POS2')

            # 下料
            kafka_push_consumables.push_consumable_all_boards(us.a_SP96XL1, push={'MGRK01': ('POS3', 'POS2'), 'MGRK02': ('POS12', 'POS20')})

            my_logger.info('cyc {} end...'.format(count))
            count += 1

    except Exception as e:
        my_logger.error(u'error: %s' % e)

