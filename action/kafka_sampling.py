#encoding=utf-8
import uuid
from datetime import datetime
from common.base import Base
# from common.common import logger
from tools.handle_task_id import my_task_id
from tools.handle_command_id import my_comm_id
from tools.handle_log import my_logger

us = Base()
__TASK_ID = my_task_id.get_task_id()


def quantification():
    # 测试设备操作：定量
    command_id = my_comm_id.get_command_id()
    comm = '''{
        "message_id": "25dead9b0c154b00adf9c0139f42b8a0",
        "message_type": "command",
        "message_group": "%s",
        "message_content": {
            "task_id": "%s",
            "device_id": "B-STARlet-01, B-BMG",
            "command_id": "%s",
            "command": "sampling",
            "parameters": {
                "script_code": "scriptname,noname",
                "script_name": "Quantification_NIFTY_20190910_Cycle, Exkubit",
                "normalize_data": [{
                    "sample_code": "MGRK011111110001",
                    "source_plate": "MGRK011111110001",
                    "source_well": "<string>",
                    "source_tube": "<string>",
                    "dest_plate": "<string>",
                    "dest_well": "<string>",
                    "dest_tube": "<string>",
                    "sample_vol": "<string>",
                    "mgw_vol": "<string>",
                    "te_vol": "<string>"
                }
            ]
            }
        }
    }''' % (us.topic_task_lims, __TASK_ID, command_id)
    return comm, command_id


def quant():
    msg_quant, com_id_quant = quantification()
    my_logger.info('command id: {}'.format(com_id_quant))
    us.send(us.topic_task_lims, msg_quant)
    us.wait_task_complete(us.consumer_task_apl, us.topic_task_apl, com_id_quant)


if __name__ == "__main__":
    try:
        for i in range(1):
            quant()
    except Exception as e:
        my_logger.error(e)
