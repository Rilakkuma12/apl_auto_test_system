#encoding=utf-8
import uuid
import base as us
import json
from handle_log import HandleLogger
from handle_task_id import my_task_id
__TASK_ID = my_task_id.get_task_id()
my_logger = HandleLogger()


__msg_old = '''
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
            "inputs": [
            {
                "material": "%s",
                "position": "%s", 
                "barcode": "%s", 
                "device_type": "Hotel", 
                "device_id": "%s",
                "location": "", 
                "rack_idx": "%s", 
                "rack_id": "",
                "level_idx": "%s",
                "sealing": "%s", 
                "tearing": "%s", 
                "centrifuge": "%s", 
                "idx": %d
            }]
        }
    }
}'''

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
            "inputs": []
        }
    }
}'''

__inputs = '''{
                "material": "%s",
                "position": "%s", 
                "barcode": "%s", 
                "device_type": "Hotel", 
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


def __load_consumables(src, rack, level, pn, barcode, dest, pos, sealing='false', tearing='false', centrifuge='false', idx=1):
    # 测试设备操作：上料
    # rst = int(random()*3)
    command_id = uuid.uuid1()
    comm = __msg_old % (__TASK_ID, dest, command_id, pn, pos, barcode, src, rack, level, sealing, tearing, centrifuge, idx)
    return comm, command_id


def __load_consumables_all_board(dest, msg):
    # 测试设备操作：上料
    # rst = int(random()*3)
    command_id = uuid.uuid1()
    comm = msg % (us.__topic_task_lims_, __TASK_ID, dest, command_id)
    return comm, command_id, __TASK_ID


def load_consumables(src, rack, level, pn, barcode, dest, pos, sealing, tearing, centrifuge, idx):
    msg_load, com_id_load = __load_consumables(src, rack, level, pn, barcode, dest, pos, sealing, tearing, centrifuge, idx)
    my_logger.info('loadConsumables,command id: {}'.format(com_id_load))
    us.send(us.__topic_task_lims, msg_load)
    if us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_load):
        pass
    else:
        raise Exception


def __load_consumables_all_boards(dest, msg):
    msg_load, com_id_load, task_id = __load_consumables_all_board(dest, msg)
    my_logger.info('loadConsumables all boards,command id:{}，task id：{}'.format(com_id_load, task_id))
    us.send(us.__topic_task_lims, msg_load)
    if us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_load):
        pass
    else:
        raise Exception


def __load_consumables_all_boards_no_wait(dest, msg):
    msg_load, com_id_load, task_id = __load_consumables_all_board(dest, msg)
    my_logger.info('loadConsumables all boards,command id: {}'.format(com_id_load))
    us.send(us.__topic_task_lims, msg_load)
    return com_id_load


def load_from_pn(dest, is_pro_area=True, **kwargs):
    # 一个一个找，找到PN号对应的barcode，上料
    us.hotel_store()  # 先获取一下堆栈库存
    load = kwargs['load']
    for key in load.keys():
        nums = len(load[key])
        barcodes = us.pn_to_barcodes(key, is_pro_area)[: nums]
        for j in range(len(barcodes)):
            barcode = barcodes[j]
            addr = us.barcode_to_addr(barcode, is_pro_area)
            hotel = addr[:3]
            rack_idx = addr[4]
            level_idx = addr[6]
            if hotel == 'AH1':
                hotel_id = us.a_HotelA
            elif hotel == 'AH2':
                hotel_id = us.a_HotelB
            elif hotel == 'BH1':
                hotel_id = us.b_HotelA
            else:
                hotel_id = us.b_HotelB
            pos = load[key][j]
            my_logger.info('loadConsumables, from {}R{}L{} to {}{}'.format(hotel, rack_idx, level_idx, us.get_name(dest), pos))
            # 把上料信息存到文件
            # with open('store.txt', 'a') as f:
            #     f.write('{},{},{},{},{}\n'.format(pos, barcode, hotel_id, rack_idx, level_idx))
            load_consumables(hotel_id, rack_idx, level_idx, key, barcode, dest, pos, sealing='false',
                             tearing='true', centrifuge='true', idx=1)


def load_consumable_all_board(dest, is_pro_area=True, is_cytomat=False,
                              is_inter=False, sealing='false', tearing='false', centrifuge='false', **kwargs):
    """is_pro_area=True 代表前区，false后区"""
    msg = json.loads(__msg)  # 把msg转换为字典
    load_list = msg['message_content']['parameters']['inputs']
    us.hotel_store()  # 先获取一下堆栈库存
    load = kwargs['load']
    turn = 1
    for key in load.keys():
        nums = len(load[key])
        barcodes = us.pn_to_barcodes(key, is_pro_area, is_cytomat)[: nums]
        for j in range(len(barcodes)):
            barcode = barcodes[j]
            addr = us.barcode_to_addr(barcode, is_pro_area, is_cytomat)
            hotel = addr[:3]
            rack_idx = addr[addr.find('R') + 1: addr.find('L')]
            level_idx = addr[addr.find('L') + 1:]
            if hotel == 'AH1':
                hotel_id = us.a_HotelA
            elif hotel == 'AH2':
                hotel_id = us.a_HotelB
            elif hotel == 'BH1':
                hotel_id = us.b_HotelA
            elif hotel == 'AC1':
                hotel_id = us.a_CytomatA
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


def load_consumable_all_board_no_wait(dest, is_pro_area=True, is_inter=False, sealing='false', tearing='false', centrifuge='false', **kwargs):
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
            my_logger.info('loadConsumables all boards, from {}R{}L{} to {}{}'.format(hotel, rack_idx, level_idx,
                                                                                      us.get_name(dest), pos))
            # 将获取的上料信息插入msg字典
            inputs = __inputs % (
            key, pos, barcode, hotel_id, rack_idx, rack_id, level_idx, sealing, tearing, centrifuge, turn)
            turn += 1
            inputs = json.loads(inputs)
            load_list.append(inputs)
    # 再把msg转回字符串
    msg1 = json.dumps(msg, indent=4)
    return __load_consumables_all_boards_no_wait(dest, msg1)


if __name__ == "__main__":
    try:
        for i in range(1):
            load_consumable_all_board(us.b_SP100, is_pro_area=False, load={'BRMW01': ('POS2', 'POS11'),
                                                                           'GETP01': ('POS4',),
                                                                           'BGMX02': ('POS9', ),
                                                                           'DNDW01': ('POS7',)})
            # load_consumable_all_board(us.b_SP100, is_pro_area=False, load={'DNDW01': ('POS7',)})
            # load_consumable_all_board(us.a_SP96XL1, load={'MGRK01': ('POS12',)})
            # load_consumable_all_board(us.b_SP96XL4, is_pro_area=False, load={'MGRK01': ('POS18',)})
            # load_consumable_all_board(us.a_SP96XL1,
            #                           sealing='true',
            #                           tearing='true',
            #                           load={'MGRK01': ('POS7', 'POS8')})
            # load_consumable_all_board(us.a_SP96XL1, load={'MGRK01': ('POS2',)})
            # load_consumable_all_board(us.a_SP96XL1, load={'MGRK01': ('POS2', 'POS3', 'POS4', 'POS5',
            #                                                          'POS7', 'POS8', 'POS9', 'POS10',
            #                                                          'POS11', 'POS12', 'POS13', 'POS14', 'POS15',
            #                                                          'POS16', 'POS17', 'POS18', 'POS19', 'POS20',
            #                                                          'POS21', 'POS22', 'POS23', 'POS24', 'POS25',
            #                                                          'POS26', 'POS27', 'POS28', 'POS29', 'POS30',
            #                                                          'POS31', 'POS32', 'POS33', 'POS34', 'POS35',
            #                                                          'POS36', 'POS37', 'POS38', 'POS39', 'POS40')})
            # load_consumable_all_board(us.a_SP96XL1, load={'BRMW01': ('POS3',)})
            # load_consumable_all_board(us.b_SP96XL4, is_pro_area=False,
            #                           load={'BRMW01': ('POS3',)})

            load_consumable_all_board(us.b_SP100, is_pro_area=True,
                                      load={'MGRK01': ('POS2', 'POS3', 'POS4', 'POS5', 'POS6,'
                                                                                       'POS7', 'POS8', 'POS9')})
            # load_consumable_all_board(us.a_SP96XL1,
            #                           is_cytomat=True,
            #                           load={'BRMW01': ('POS7',),
            #                                 'DNDW01': ('POS9',)})
            # load_consumable_all_board(us.b_startlet,
            #                           is_pro_area=False,
            #                           load={
            #                               'CRAP03': ('POS1',),
            #                               'CRAP02': ('POS2', 'POS4', 'POS5'),
            #                               'CRTP01': ('POS6', 'POS7', 'POS9', 'POS10'),
            #                               'EDUV01': ('POS11', 'POS12'),
            #                               'BRMW01': ('POS13', 'POS14'),
            #                               'DNDW01': ('POS18',)
            #                           })
            # load_consumable_all_board(us.b_startlet,
            #                           is_pro_area=False,
            #                           load={
            #                               'MGRK01': ('POS1',),
            #                               'MGRK02': ('POS2',)
            #                           })
    except Exception as e:
        my_logger.error(u'error: %s' % e)

