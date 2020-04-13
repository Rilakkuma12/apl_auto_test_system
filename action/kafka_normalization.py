#encoding=utf-8
import uuid
from base import common as us
from base.common import logger
from datetime import datetime
__TASK_ID = (datetime.now().isoformat()).replace(':', '-')


def normalization():
    # 测试设备操作：均一化
    command_id = uuid.uuid1()
    comm = '''{
        "message_type": "command",
        "message_group": "task_lims",
        "message_content": {
            "task_id": "%s",
            "device_id": "B-STARlet-01",
            "command_id": "%s",
            "command": "norm",
            "parameters": {
                "script_code": "normalization",
                "script_name": "Normalization_NIFTY_20190927_Cycle",
                "normaliza_data": [{
                    "sample_code": "1",
                    "source_plate": "1",
                    "source_well": "1",
                    "source_tube": "1",
                    "dest_plate": "1",
                    "dest_well": "1",
                    "dest_tube": "1",
                    "sample_vol": "1",
                    "mgw_vol": "1",
                    "te_vol": "1"
                }]
            }
        },
        "message_id": "25dead9b0c154b00adf9c0139f42b8a0"
    }''' % (__TASK_ID, command_id)
    return comm, command_id


def normalize():
    msg_norm, com_id_norm = normalization()
    print('command id: {}'.format(com_id_norm))
    us.send(us.__topic_task_lims, msg_norm)
    us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_norm)


if __name__ == "__main__":
    try:
        for i in range(1, 2):
            normalize()
    except Exception as e:
        logger().writelines(u'error: %s\n' % e.message)
    finally:
        logger().flush()
        logger().close()
