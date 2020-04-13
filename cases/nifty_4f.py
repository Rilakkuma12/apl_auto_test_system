# -*- coding: UTF-8
from base import common as us
from action import kafka_push_consumables, kafka_device_command
from action import kafka_transfer
from tools.handle_log import my_logger
from tools.handle_excel import HandleExcel
from tools.constance import TIME_RECORD_PATH

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
        # kafka_device_command.unlock_hotel()
        # kafka_device_command.unlock_hotel(us.a_HotelB)
        #
        # # 上锁
        # kafka_device_command.lock_hotel()
        # kafka_device_command.lock_hotel(us.a_HotelB)

        # 扫码
        kafka_device_command.scan_hotel()
        kafka_device_command.scan_hotel(us.a_HotelB)
        # kafka_device_command.scan_hotel(us.b_HotelA)
        # kafka_device_command.scan_hotel(us.b_HotelB)

        # # 释放
        # kafka_device_command.release_hotel()
        # kafka_device_command.release_hotel(us.a_HotelB)

        for i in range(1):
            setattr(HandleExcel, 'current_row', i + 2)
            record_file.record_time(row=getattr(HandleExcel, 'current_row'), col=1, result=i+1)
            my_logger.info('cyc {} begin...'.format(i + 1))
            # # 上料
            # # kafka_interaction.load_consumable_from_inter(us.a_SP96XL1, rack_idx='1', level_idx='1', rack_id='MGRK01', barcode='MGRK010001000001', load={'MGRK01': ('POS17',)})
            # kafka_load_consumables.load_consumable_all_board(us.a_SP96XL1,
            #                                                  load={'MGRK01': ('POS2',), 'MGRK02': ('POS3',),
            #                                                        'MGRK03': ('POS4',)})
            #
            # kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4, is_pro_area=False,
            #                                                  load={'MGRK01': ('POS2',), 'MGRK02': ('POS3',), 'MGRK03': ('POS4',)})
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

            # kafka_interaction.push_consumable_to_inter(us.a_SP96XL1, rack_idx='1', level_idx='1', rack_id='MGRK01', barcode='MGRK010001000001', push={'MGRK01': ('POS17',)})

            my_logger.info('cyc {} end...'.format(i + 1))

    except Exception as e:
        my_logger.error(u'error: %s' % e)

