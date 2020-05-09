# -*- coding: UTF-8
import time

from common.base import Base as us
from action.kafka_load_all import KafkaLoadAll
from action.kafka_push_all import KafkaPushAll
from action.kafka_task_issue import issue
from tools.handle_log import my_logger
from tools.handle_excel import HandleExcel
from tools.constance import TIME_RECORD_PATH
from action.kafka_device_command import scan_hotel
from action.kafka_run_script import RunScript

record_file = HandleExcel(TIME_RECORD_PATH)


if __name__ == '__main__':
    load_all = KafkaLoadAll()
    push_all = KafkaPushAll()

    for i in range(10000):

        # scan_hotel(us.b_HotelB)
        # scan_hotel(us.b_HotelA)
        # # 下发任务
        # task_id = issue.task_issue(us.a_SP96XL1)
        # # 上料

        load_all.load_materials_all(us.a_SP96XL1,
                                    load={
                                        'DNDW01': {
                                            'POS8': '1:hotel::sealing-False:tear-False:cen-False:',
                                        },
                                        'BRMW01': {
                                            'POS7': '1:fridge::sealing-False:tear-False:cen-False:',
                                            'POS14': '1:interaction1:POS11:sealing-False:tear-False:cen-False:',
                                        },
                                        'MGPH01': {
                                            'POS18': '1:interaction1:POS55:sealing-False:tear-False:cen-False:',
                                        }
                                    })

        push_all.push_materials_all(us.a_SP96XL1,
                                    push={
                                        'DNDW01': {
                                            'POS8': '1:hotel::sealing-False:tear-False:cen-False:',
                                        },
                                        'BRMW01': {
                                            'POS7': '1:fridge::sealing-False:tear-False:cen-False:',
                                            'POS14': '1:interaction1:POS11:sealing-False:tear-False:cen-False:',
                                        },
                                        'MGPH01': {
                                            'POS18': '1:interaction1:POS55:sealing-False:tear-False:cen-False:',
                                        }
                                    })

        # # 上料
        load_all.load_materials_all(us.a_SP96XL2,
                                    load={
                                        'DNDW01': {
                                            'POS8': '1:hotel::sealing-False:tear-False:cen-False:',
                                        },
                                        'BRMW01': {
                                            'POS7': '1:fridge::sealing-False:tear-False:cen-False:',
                                            'POS14': '1:interaction1:POS11:sealing-False:tear-False:cen-False:',
                                        },
                                        'MGPH01': {
                                            'POS18': '1:interaction1:POS55:sealing-False:tear-False:cen-False:',
                                        }
                                    })

        push_all.push_materials_all(us.a_SP96XL2,
                                    push={
                                        'DNDW01': {
                                            'POS8': '1:hotel::sealing-False:tear-False:cen-False:',
                                        },
                                        'BRMW01': {
                                            'POS7': '1:fridge::sealing-False:tear-False:cen-False:',
                                            'POS14': '1:interaction1:POS11:sealing-False:tear-False:cen-False:',
                                        },
                                        'MGPH01': {
                                            'POS18': '1:interaction1:POS55:sealing-False:tear-False:cen-False:',
                                        }
                                    })

        # # 上料
        load_all.load_materials_all(us.a_SP96XL3,
                                    load={
                                        'DNDW01': {
                                            'POS8': '1:hotel::sealing-False:tear-False:cen-False:',
                                        },
                                        'BRMW01': {
                                            'POS7': '1:fridge::sealing-False:tear-False:cen-False:',
                                            'POS14': '1:interaction1:POS11:sealing-False:tear-False:cen-False:',
                                        },
                                        'MGPH01': {
                                            'POS18': '1:interaction1:POS55:sealing-False:tear-False:cen-False:',
                                        }
                                    })

        push_all.push_materials_all(us.a_SP96XL3,
                                    push={
                                        'DNDW01': {
                                            'POS8': '1:hotel::sealing-False:tear-False:cen-False:',
                                        },
                                        'BRMW01': {
                                            'POS7': '1:fridge::sealing-False:tear-False:cen-False:',
                                            'POS14': '1:interaction1:POS11:sealing-False:tear-False:cen-False:',
                                        },
                                        'MGPH01': {
                                            'POS18': '1:interaction1:POS55:sealing-False:tear-False:cen-False:',
                                        }
                                    })

    # except Exception as e:
    #     my_logger.error(u'error: %s' % e)
