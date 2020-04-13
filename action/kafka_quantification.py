#encoding=utf-8
import uuid
from common import base as us
# from common.common import logger
from datetime import datetime

from handle_log import my_logger

__TASK_ID = (datetime.now().isoformat()).replace(':', '-')


def quantification():
    # 测试设备操作：定量
    command_id = uuid.uuid1()
    comm = '''{
        "message_type": "command",
        "message_group": "%s",
        "message_content": {
            "task_id": "%s",
            "device_id": "B-STARlet-01, B-BMG",
            "command_id": "%s",
            "command": "quant",
            "parameters": {
                "script_code": "scriptname,noname",
                "script_name": "Quantification_NIFTY_20190910_Cycle, Exkubit",
                "inputs": [{
                    "material": "MGRK01",
                    "position": "POS02",
                    "barcode": "MGRK011111110001",
                    "column": "1"
                }
            ]
            }
        },
        "message_id": "25dead9b0c154b00adf9c0139f42b8a0"
    }''' % (us.__topic_task_lims, __TASK_ID, command_id)
    return comm, command_id


def quant():
    msg_quant, com_id_quant = quantification()
    my_logger.info('command id: {}'.format(com_id_quant))
    us.send(us.__topic_task_lims, msg_quant)
    us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_quant)


if __name__ == "__main__":
    try:
        for i in range(1):
            quant()
    except Exception as e:
        my_logger.error(e)
