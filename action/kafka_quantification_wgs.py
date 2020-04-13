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
    "message_content":{
        "command":"quant",
        "message_group":"%s",
        "task_id":"%s",
        "command_id":"%s",
        "device_id":"STARlet-6,BMG-6",
        "parameters":{
            "inputs":[
                {
                    "barcode":"EDUV010003000004",
                    "column":"-1",
                    "group":"1",
                    "position":"POS11"
                },
                {
                    "barcode":"EDUV010003000006",
                    "column":"1",
                    "group":"1",
                    "position":"POS16"
                },
                {
                    "barcode":"EDUV010003000005",
                    "column":"-1",
                    "group":"2",
                    "position":"POS12"
                },
                {
                    "barcode":"EDUV010003000006",
                    "column":"3",
                    "group":"2",
                    "position":"POS16"
                }
            ],
            "script_code":"Quantification_pcr,pcr_std_quant,Quantification_pcr,pcr_quant",
            "script_content":"MQ==",
            "script_name":"pcr_quantification,pcr_std_quant,pcr_quantification,pcr_quant"
        }
        
    },
    "message_id":"bf0e44391af942a6891302d91f5c3105",
    "message_type":"command"
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
