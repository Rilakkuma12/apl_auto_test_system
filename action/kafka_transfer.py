#encoding=utf-8
import uuid
from common import base as us
from tools.handle_log import my_logger
from tools.handle_task_id import my_task_id
__TASK_ID = my_task_id.get_task_id()
barcodes = []

__msg = '''
{
    "message_id": "351e3a7cbc3b4b0c98e92ace8bca5e77",
    "message_type": "command", 
    "message_group": "%s", 
    "message_content": {
        "task_id": "%s", 
        "device_id": "%s",
        "command_id": "%s",
        "command": "load", 
        "parameters": {
            "inputs": [
                {
                    "material": "%s",
                    "position": "%s", 
                    "barcode": "%s", 
                    "device_type": "Module", 
                    "device_id": "%s",
                    "location": "%s", 
                    "rack_idx": "", 
                    "rack_id": "",
                    "level_idx": "",
                    "sealing": "%s", 
                    "tearing": "%s", 
                    "centrifuge": "%s", 
                    "idx": %d
                }
            ]
        }
    }
}'''


__msg_head = '''
{
    "message_id": "351e3a7cbc3b4b0c98e92ace8bca5e77",
    "message_type": "command", 
    "message_group": "%s", 
    "message_content": {
        "task_id": "%s", 
        "device_id": "%s",
        "command_id": "%s",
        "command": "load", 
        "parameters": {
            "inputs": []
        }
    }
}'''


__inputs = """
{
    "material": "%s",
    "position": "%s", 
    "barcode": "%s", 
    "device_type": "Module", 
    "device_id": "%s",
    "location": "%s", 
    "rack_idx": "", 
    "rack_id": "",
    "level_idx": "",
    "sealing": "%s", 
    "tearing": "%s", 
    "centrifuge": "%s", 
    "idx": %d
}
"""

__msg_2 = '''
{
    "message_id": "351e3a7cbc3b4b0c98e92ace8bca5e77",
    "message_type": "command", 
    "message_group": "task_lims_3fa", 
    "message_content": {
        "task_id": "2070", 
        "device_id": "5485e8dd28334c80a862b73be557972b",
        "command_id": "46e53ef8-012d-11ea-8bb6-10e7c642a382",
        "command": "load", 
        "parameters": {
            "inputs": [
                {
                    "material": "BRMW01",
                    "position": "POS2", 
                    "barcode": "BRMW010001000033", 
                    "device_type": "Module", 
                    "device_id": "687c1f6cbb22476ca06e40a102651d7a",
                    "location": "POS2", 
                    "rack_idx": "", 
                    "rack_id": "",
                    "level_idx": "",
                    "sealing": "false", 
                    "tearing": "false", 
                    "centrifuge": "false", 
                    "idx": 1
                },
                {
                    "material": "DNDW01",
                    "position": "POS3", 
                    "barcode": "DNDW010001000007", 
                    "device_type": "Module", 
                    "device_id": "687c1f6cbb22476ca06e40a102651d7a",
                    "location": "POS3", 
                    "rack_idx": "", 
                    "rack_id": "",
                    "level_idx": "",
                    "sealing": "false", 
                    "tearing": "false", 
                    "centrifuge": "false", 
                    "idx": 2
                }
            ]
        }
    }
}
'''


def __load_consumables(src, pos1, dest, pn, pos2, barcode, sealing='false', tearing='false', centrifuge='false', idx=1):
    # 测试设备操作：上料
    # rst = int(random()*3)
    command_id = uuid.uuid1()
    comm = __msg % (us.__topic_task_lims, __TASK_ID, dest, command_id, pn, pos2, barcode, src, pos1, sealing, tearing, centrifuge, idx)
    return comm, command_id, __TASK_ID


def load_consumables(src, pos1, dest, pn, pos2, barcode, sealing, tearing, centrifuge, idx):
    msg_load, com_id_load, task_id = __load_consumables(src, pos1, dest, pn, pos2, barcode, sealing, tearing, centrifuge, idx)
    my_logger.info('transfer,command id: {},task id: {}'.format(com_id_load, task_id))
    us.send(us.__topic_task_lims, msg_load)
    if us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_load):
        pass
    else:
        raise Exception


def transfer(src, pos1, dest, pos2):
    # 源设备ID、POS号，到目标设备ID,POS号
    barcode = us.pos_to_barcode(src, pos1)
    pn = us.barcode_to_pn(barcode)
    my_logger.info('transfer, from {}{} to {}{}'.format(us.get_name(src), pos1, us.get_name(dest), pos2))
    load_consumables(src, pos1, dest, pn, pos2, barcode, sealing='false', tearing='false', centrifuge='false', idx=1)


def transfer_2():
    us.send(us.__topic_task_lims, __msg_2)


if __name__ == "__main__":
    try:
        for i in range(1):
            transfer(us.a_SP96XL1, 'POS2', us.b_SP96XL4, 'POS7')
            # transfer(us.a_SP96XL1, 'POS3', us.b_SP96XL4, 'POS8')
            # transfer(us.a_SP96XL1, 'POS4', us.b_SP96XL4, 'POS9')
            #
            # transfer(us.b_SP96XL4, 'POS2', us.a_SP96XL1, 'POS7')
            # transfer(us.b_SP96XL4, 'POS3', us.a_SP96XL1, 'POS8')
            # transfer(us.b_SP96XL4, 'POS4', us.a_SP96XL1, 'POS9')
            # transfer(us.b_SP96XL4, 'POS7', us.a_SP96XL1, 'POS12')
            # transfer(us.b_SP96XL4, 'POS8', us.a_SP96XL1, 'POS13')
            # transfer(us.b_SP96XL4, 'POS9', us.a_SP96XL1, 'POS14')
            transfer_2()
    except Exception as e:
        my_logger.error(u'error: %s' % e)

