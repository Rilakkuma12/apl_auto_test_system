#encoding=utf-8
import uuid
from base import common as us
import json
from tools.handle_log import HandleLogger
from tools.handle_task_id import my_task_id
__TASK_ID = my_task_id.get_task_id()
my_logger = HandleLogger()


__msg = '''
{
    "message_id": "351e3a7cbc3b4b0c98e92ace8bca5e77",
    "message_type": "command", 
    "message_group": "task_lims", 
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

__inputs = '''{
                "material": "%s",
                "position": "%s", 
                "barcode": "%s", 
                "device_type": "Cytomat", 
                "device_id": "%s",
                "location": "", 
                "rack_idx": "%s", 
                "rack_id": "%s",
                "level_idx": "%s",
                "sealing": "%s", 
                "tearing": "%s", 
                "centrifuge": "%s", 
                "idx": %d
            }'''


def __load_consumables_all_board(dest, msg):
    # 测试设备操作：上料
    # rst = int(random()*3)
    command_id = uuid.uuid1()
    comm = msg % (__TASK_ID, dest, command_id)
    return comm, command_id, __TASK_ID


def __load_consumables_all_boards(dest, msg):
    msg_load, com_id_load, task_id = __load_consumables_all_board(dest, msg)
    my_logger.info('loadConsumables all boards,command id: {}'.format(com_id_load))
    us.send(us.__topic_task_lims, msg_load)
    if us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_load):
        pass
    else:
        raise Exception


def load_from_cytomat(dest, is_pro_area=True, is_inter=False, sealing='false', tearing='false', centrifuge='false', **kwargs):
    msg = json.loads(__msg)  # 把msg转换为字典
    load_list = msg['message_content']['parameters']['inputs']
    us.hotel_store()  # 先获取一下堆栈库存
    load = kwargs['load']
    turn = 1
    for key in load.keys():
        nums = len(load[key])
        barcodes = us.pn_to_barcodes(key, is_pro_area, is_inter)[: nums]
        for j in range(len(barcodes)):
            barcode = barcodes[j]
            addr = us.barcode_to_addr(barcode, is_pro_area, is_inter)
            hotel = addr[:3]
            rack_idx = addr[addr.find('R') + 1: addr.find('L')]
            level_idx = addr[addr.find('L') + 1:]
            if hotel == 'AH1':
                hotel_id = us.a_HotelA
            elif hotel == 'AH2':
                hotel_id = us.a_HotelB
            elif hotel == 'BH1':
                hotel_id = us.b_HotelA
            else:
                hotel_id = us.b_HotelB
            pos = load[key][j]
            rack_id = us.barcode_to_rack(barcode, is_pro_area, is_inter)
            my_logger.info('loadConsumables all boards, from {}R{}L{} to {}{}'.format(hotel, rack_idx, level_idx, us.get_name(dest), pos))
            # 将获取的上料信息插入msg字典
            inputs = __inputs % (key, pos, barcode, hotel_id, rack_idx, rack_id, level_idx, sealing, tearing, centrifuge, turn)
            turn += 1
            inputs = json.loads(inputs)
            load_list.append(inputs)
    # 再把msg转回字符串
    msg1 = json.dumps(msg, indent=4)
    __load_consumables_all_boards(dest, msg1)


if __name__ == "__main__":
    try:
        for i in range(1):
            load_from_cytomat(us.a_SP96XL2, load={'MGRK01': ('POS16', 'POS17', 'POS18')})

    except Exception as e:
        my_logger.error(u'error: %s' % e)

