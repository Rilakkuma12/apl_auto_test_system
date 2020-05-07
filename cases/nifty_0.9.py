# -*- coding: UTF-8
from common.base import Base as us
from action.kafka_load_all import KafkaLoadAll
from action.kafka_task_issue import issue
from tools.handle_log import my_logger
from tools.handle_excel import HandleExcel
from tools.constance import TIME_RECORD_PATH
from action.kafka_device_command import scan_hotel
from action.kafka_run_script import RunScript

record_file = HandleExcel(TIME_RECORD_PATH)


if __name__ == '__main__':

    try:
        # scan_hotel(us.b_HotelB)
        # scan_hotel(us.b_HotelA)
        # 下发任务
        task_id = issue.task_issue(us.b_SP96XL4)
        # task_id = 2873
        # 上料
        load_all = KafkaLoadAll(task_id)
        load_all.load_materials_all(us.b_SP96XL4,
                                    load={
                                        'MGRK01': {
                                            'POS8': '2:hotel::sealing-False:tear-False:cen-True:GBRS01',
                                            'POS12': '2:interaction2:POS41:sealing-False:tear-False:cen-False:',
                                            'POS17': '2:interaction2:POS55:sealing-False:tear-False:cen-False:'
                                        }
                                    })
        # rr = RunScript(task_id)
        # rr.run_script(us.b_SP96XL4, 'spx96_home.py')

    except Exception as e:
        my_logger.error(u'error: %s' % e)
