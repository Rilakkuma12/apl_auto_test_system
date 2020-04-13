#encoding=utf-8
import uuid
from common import base as us
from datetime import datetime
import json
from tools.handle_log import my_logger
import time
from action import kafka_load_consumables
from action import kafka_transfer

__TASK_ID = (datetime.now().isoformat()).replace(':', '-')

__msg = '''
{
    "message_id": "UUID",
    "message_type": "run_response",
    "message_group": "%s",
    "message_content": {
        "task_id": "%s",
        "command_id": "%s",
        "request_id": "%s",
        "response": "%s",
        "attributes": {}
    }

}'''


def __pcr_mix_rep(task_id, request_id, response=0):
    # 测试设备操作：pcrmix响应
    rep = ['success', 'failure']
    command_id = uuid.uuid1()
    comm = __msg % (us.__topic_task_lims, task_id, command_id, request_id, rep[int(response)])
    return comm, command_id


def pcr_mix_rep(device, response):
    task_id, request_id = us.get_pcr_mix_request_info()
    time.sleep(3)
    msg_load, com_id_load = __pcr_mix_rep(task_id, request_id, response)
    my_logger.info('pcr_mix response,command id: {}'.format(com_id_load))
    us.send(us.__topic_task_lims, msg_load)


if __name__ == "__main__":
    # while True:
    try:
        # for i in range(2):
        #     0成功 1失败
            # pcr_mix_rep(us.a_SP96XL3, 1)
            # time.sleep(2)
        # pcr_mix_rep(us.a_SP96XL3, 0)
        # 收到pcr-mix请求之后工位4开始跨区转移
        # kafka_load_consumables.load_consumable_all_board(us.b_SP96XL4,
        #                                                  is_pro_area=False,
        #                                                  load={'GETP01': ('POS4', 'POS3')})
        # kafka_transfer.transfer(us.a_SP96XL3, 'POS26', us.b_SP96XL4, 'POS17')
        kafka_transfer.transfer(us.a_SP96XL3, 'POS31', us.b_SP96XL4, 'POS22')
    except Exception as e:
        my_logger.error(u'error: %s' % e)

