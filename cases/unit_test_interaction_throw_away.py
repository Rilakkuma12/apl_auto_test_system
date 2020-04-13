# -*- coding: UTF-8
from common import base as us
from action import kafka_run_script
from action import kafka_interaction
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
        for i in range(1):

            # 上料
            kafka_interaction.load_consumable_from_inter(us.b_SP100, src=us.b_interaction, rack_idx='5', level_idx='5', load={'MGPH01': ('POS3',)})
            # kafka_interaction.load_2_consumable_from_inter()
            # kafka_run_script.run_script(us.b_SP100, 'spx96_throw_lid_request.py', if_final=True)
            kafka_interaction.push_consumable_to_inter(us.b_SP100, hotel=us.b_interaction, rack_idx='9', level_idx='5', push={'MGPH01': ('POS3',)})
            # kafka_interaction.push_consumable_to_inter(us.b_SP100, hotel=us.b_interaction, rack_idx='7', level_idx='5',
            #                                            push={'MGPH01': ('POS5',)})

            # kafka_interaction.load_consumable_from_inter(us.a_SP96XL1, src=us.a_interaction, rack_idx='5', level_idx='5', load={'MGPH01': ('POS3',)})
            # kafka_run_script.run_script(us.a_SP96XL1, 'spx96_throw_lid_request.py')
            # kafka_interaction.push_consumable_to_inter(us.a_SP96XL1, hotel=us.a_interaction, rack_idx='5', level_idx='5',  push={'MGPH01': ('POS3',)})
            #
            # kafka_interaction.load_consumable_from_inter(us.a_SP96XL1, rack_idx='5', level_idx='3', rack_id='MGRK01',
            #                                              barcode='MGRK010001000001', load={'MGRK01': ('POS16',)})
            # kafka_run_script.run_script(us.a_SP96XL1, 'spx96_throw_lid_request.py')
            # kafka_interaction.push_consumable_to_inter(us.a_SP96XL1, rack_idx='5', level_idx='3', rack_id='MGRK01',
            #                                            barcode='MGRK010001000001', push={'MGPH01': ('POS16',)})
            #
            # kafka_interaction.load_consumable_from_inter(us.a_SP96XL1, rack_idx='5', level_idx='2', rack_id='MGRK01',
            #                                              barcode='MGRK010001000001', load={'MGRK01': ('POS15',)})
            # kafka_run_script.run_script(us.a_SP96XL1, 'spx96_throw_lid_request.py')
            # kafka_interaction.push_consumable_to_inter(us.a_SP96XL1, rack_idx='5', level_idx='2', rack_id='MGRK01',
            #                                            barcode='MGRK010001000001', push={'MGPH01': ('POS15',)})
            #
            # kafka_interaction.load_consumable_from_inter(us.a_SP96XL1, rack_idx='5', level_idx='1', rack_id='MGRK01',
            #                                              barcode='MGRK010001000001', load={'MGRK01': ('POS14',)})
            # kafka_run_script.run_script(us.a_SP96XL1, 'spx96_throw_lid_request.py')
            # kafka_interaction.push_consumable_to_inter(us.a_SP96XL1, rack_idx='5', level_idx='1', rack_id='MGRK01',
            #                                            barcode='MGRK010001000001', push={'MGPH01': ('POS14',)})

    except Exception as e:
        my_logger.error(u'error: %s' % e)

