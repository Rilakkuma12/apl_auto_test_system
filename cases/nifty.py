# -*- coding: UTF-8
from base import common as us
from action import kafka_device_command
from tools.handle_log import my_logger
import asyncio


def async_run(task):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task))
    loop.close()


if __name__ == '__main__':
    try:
        count = 1
        for i in range(1):
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
            my_logger.info('cyc {} begin...'.format(count))
            # A、B开锁
            task1 = [kafka_device_command.unlock_hotel(us.HotelA),
                     kafka_device_command.unlock_hotel(us.HotelB)]
            async_run(task1)

            # A、B上锁
            task2 = [kafka_device_command.lock_hotel(us.HotelA),
                     kafka_device_command.lock_hotel(us.HotelB)]
            async_run(task2)

            # A、B扫码
            task3 = [kafka_device_command.scan_hotel(us.HotelA),
                     kafka_device_command.scan_hotel(us.HotelB)]
            async_run(task3)

            # A、B释放
            task4 = [kafka_device_command.release_hotel(us.HotelA),
                     kafka_device_command.release_hotel(us.HotelB)]
            async_run(task4)

            # # 工位1上料
            # kafka_load_consumables.load_from_pn(us.SP96XL1, load={'MGRK01': ('POS3', 'POS2'),
            #                                                       'MGRK02': ('POS12', 'POS20')})
            # # 工位1运行脚本
            # kafka_run_script.run_script(us.SP96XL1, 'spx96_pre_clean_cn_local_new.py')
            #
            # # 工位2上料
            #
            #
            # # 工位1向工位2转移
            #
            # # 工位2运行脚本
            #
            # # 异步工位1下料
            #
            # # 下料
            # kafka_push_consumables.push_from_pn(us.SP96XL1, push={'MGRK01': ('POS3', 'POS2'),
            #                                                       'MGRK02': ('POS12', 'POS20')})

            my_logger.info('cyc {} end...'.format(count))
            count += 1

    except Exception as e:
        my_logger.error(u'error: %s' % e)

