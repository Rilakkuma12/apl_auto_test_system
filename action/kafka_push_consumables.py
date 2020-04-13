#encoding=utf-8
import uuid
from common import base as us
from tools.handle_log import my_logger
import json
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
        "command": "move", 
        "parameters": {
            "outputs": [
                {
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
                }
            ]
        }
    }
}'''

__msg_new = '''
{
    "message_id": "351e3a7cbc3b4b0c98e92ace8bca5e77",
    "message_type": "command", 
    "message_group": "%s", 
    "message_content": {
        "task_id": "%s", 
        "device_id": "%s",
        "command_id": "%s",
        "command": "move", 
        "parameters": {
            "outputs": []
        }
    }
}'''

__outputs = '''
{
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


__msg_startlet = '''
{
    "message_id": "351e3a7cbc3b4b0c98e92ace8bca5e77",
    "message_type": "command",
    "message_group": "task_lims_3fa",
    "message_content": {
        "task_id": "1950",
        "device_id": "B-STARlet-01",
        "command_id": "22784708-010c-11ea-a820-10e7c642a382",
        "command": "move",
        "parameters": {
            "outputs": [
                {
                    "material": "CRAP02",
                    "position": "POS2",
                    "barcode": "CRAP020001000003",
                    "device_type": "Hotel",
                    "device_id": "c6ec6e0eea73488f81508ed0de3ab6b9",
                    "location": "",
                    "rack_idx": "5",
                    "rack_id": "MGRK060001000002",
                    "level_idx": "1",
                    "sealing": "false",
                    "tearing": "false",
                    "centrifuge": "false",
                    "idx": 1
                },
                {
                    "material": "EDUV01",
                    "position": "POS11",
                    "barcode": "EDUV010001000001",
                    "device_type": "Hotel",
                    "device_id": "c6ec6e0eea73488f81508ed0de3ab6b9",
                    "location": "",
                    "rack_idx": "3",
                    "rack_id": "MGRK040001000016",
                    "level_idx": "11",
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

__msg_startlet_3 = '''
{
    "message_id": "351e3a7cbc3b4b0c98e92ace8bca5e77",
    "message_type": "command",
    "message_group": "task_lims_3fa",
    "message_content": {
        "task_id": "2046",
        "device_id": "B-STARlet-01",
        "command_id": "ffcadf52-0125-11ea-9474-10e7c642a382",
        "command": "move",
        "parameters": {
            "outputs": [
                {
                    "material": "BRMW01",
                    "position": "POS13",
                    "barcode": "BRMW010000000003",
                    "device_type": "Hotel",
                    "device_id": "c6ec6e0eea73488f81508ed0de3ab6b9",
                    "location": "",
                    "rack_idx": "3",
                    "rack_id": "MGRK040001000016",
                    "level_idx": "4",
                    "sealing": "false",
                    "tearing": "false",
                    "centrifuge": "false",
                    "idx": 1
                },
                {
                    "material": "BRMW01",
                    "position": "POS14",
                    "barcode": "BRMW010001000036",
                    "device_type": "Hotel",
                    "device_id": "c6ec6e0eea73488f81508ed0de3ab6b9",
                    "location": "",
                    "rack_idx": "3",
                    "rack_id": "MGRK040001000016",
                    "level_idx": "5",
                    "sealing": "false",
                    "tearing": "false",
                    "centrifuge": "false",
                    "idx": 2
                },
                {
                    "material": "DNDW01",
                    "position": "POS18",
                    "barcode": "DNDW010001000007",
                    "device_type": "Hotel",
                    "device_id": "c6ec6e0eea73488f81508ed0de3ab6b9",
                    "location": "",
                    "rack_idx": "11",
                    "rack_id": "MGRK030001000005",
                    "level_idx": "2",
                    "sealing": "false",
                    "tearing": "false",
                    "centrifuge": "false",
                    "idx": 3
                }
            ]
        }
    }
}
'''


def __push_consumables(src, rack, rack_id, level, pn, barcode, dest, pos, sealing='false', tearing='false', centrifuge='false', idx=1):
    # 测试设备操作：下料
    # rst = int(random()*3)
    command_id = uuid.uuid1()
    comm = __msg % (us.__topic_task_lims_, __TASK_ID, dest, command_id, pn, pos, barcode, src, rack, rack_id, level, sealing, tearing, centrifuge, idx)
    return comm, command_id


def __push_consumables_all_board(src, msg):
    # 测试设备操作：上料
    # rst = int(random()*3)
    command_id = uuid.uuid1()
    comm = msg % (us.__topic_task_lims_, __TASK_ID, src, command_id)
    return comm, command_id, __TASK_ID


def push_consumables(src, rack, rack_id, level, pn, barcode, dest, pos, sealing, tearing, centrifuge, idx):
    msg_push, com_id_push = __push_consumables(src, rack, rack_id, level, pn, barcode, dest, pos, sealing, tearing, centrifuge, idx)
    my_logger.info('pushConsumables, command id: {}'.format(com_id_push))
    us.send(us.__topic_task_lims, msg_push)
    if us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_push):
        pass
    else:
        raise Exception


def __push_consumables_all_boards(src, msg):
    msg_load, com_id_load, task_id = __push_consumables_all_board(src, msg)
    my_logger.info('push consumables all boards,command id: {},task id: {}'.format(com_id_load, task_id))
    us.send(us.__topic_task_lims, msg_load)
    if us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_load):
        pass
    else:
        raise Exception


def __push_consumables_all_boards_no_wait(src, msg):
    msg_load, com_id_load, task_id = __push_consumables_all_board(src, msg)
    my_logger.info('push consumables all boards,command id: {},task id: {}'.format(com_id_load, task_id))
    us.send(us.__topic_task_lims, msg_load)


def push_from_pn(src, is_pro_area=True, **kwargs):
    """
    :param src: 96xl
    :param kwargs: pos
    :return:
    1.通过POS号获取对应barcode
    2.查询一遍堆栈，如果pn号匹配，count循环，只要位置为空就可以放
    """
    push = kwargs['push']
    pn_list = push.keys()
    for pn in pn_list:
        if not isinstance(push[pn], tuple):
            my_logger.error('非元组格式，无法处理，请重新输入')
        for pos in push[pn]:
            barcode = us.pos_to_barcode(src, pos)
            hotel_name, hotel_id, rack, level, rack_id = us.tell_which_pos_can_push(pn, is_pro_area)
            my_logger.info('pushConsumables, from {}{} to {}R{}L{}'.format(us.get_name(src), pos, hotel_name, rack, level))
            push_consumables(hotel_id, rack, rack_id, level, pn, barcode, src, pos, sealing='false', tearing='false', centrifuge='false', idx=1)


def push_consumable_all_boards(src, is_pro_area=True, is_cytomat=False, sealing='false', tearing='false', centrifuge='false', **kwargs):
    """
    1、获取pos pn号
    2、根据pn号得到堆栈可以存放的位置
    3、下料清单累积一起发
    :param src:工位
    :param kwargs:下料清单
    :return:
    """
    msg = json.loads(__msg_new)
    push_list = msg['message_content']['parameters']['outputs']
    push = kwargs['push']
    pn_list = push.keys()
    turn = 1
    for pn in pn_list:
        if not isinstance(push[pn], tuple):
            my_logger.error('非元组格式，无法处理，请重新输入')
        # 看下pn对应多少个pos
        pos_num = len(push[pn])
        can_push_list = us.tell_which_pos_can_push_more(pn, pos_num, is_pro_area, is_cytomat)
        if can_push_list is None:
            my_logger.error('pn:{}, 堆栈无位置可放'.format(pn))
            return
        for j in range(pos_num):
            pos = push[pn][j]
            barcode = us.pos_to_barcode(src, pos)
            hotel_name = can_push_list[j]['hotel_name']
            hotel_id = can_push_list[j]['hotel_id']
            rack = can_push_list[j]['rack_idx']
            level = can_push_list[j]['level']
            rack_id = can_push_list[j]['rack_id']

            my_logger.info('pushConsumables, from {}{} to {}R{}L{}'.format(us.get_name(src), pos, hotel_name, rack, level))
            outputs = __outputs % (pn, pos, barcode, hotel_id, rack, rack_id, level, sealing, tearing, centrifuge, turn)
            turn += 1
            outputs = json.loads(outputs)
            push_list.append(outputs)
    msg1 = json.dumps(msg, indent=4)
    __push_consumables_all_boards(src, msg1)


def push_consumable_all_boards_no_wait(src, is_pro_area=True, is_inter=False, sealing='false', tearing='false', centrifuge='false', **kwargs):
    msg = json.loads(__msg_new)
    push_list = msg['message_content']['parameters']['outputs']
    push = kwargs['push']
    pn_list = push.keys()
    turn = 1
    for pn in pn_list:
        if not isinstance(push[pn], tuple):
            my_logger.error('非元组格式，无法处理，请重新输入')
        # 看下pn对应多少个pos
        pos_num = len(push[pn])
        can_push_list = us.tell_which_pos_can_push_more(pn, pos_num, is_pro_area, is_inter)
        if can_push_list is None:
            my_logger.error('pn:{}, 堆栈无位置可放'.format(pn))
            return
        for j in range(pos_num):
            pos = push[pn][j]
            barcode = us.pos_to_barcode(src, pos)
            hotel_name = can_push_list[j]['hotel_name']
            hotel_id = can_push_list[j]['hotel_id']
            rack = can_push_list[j]['rack_idx']
            level = can_push_list[j]['level']
            rack_id = can_push_list[j]['rack_id']

            my_logger.info('pushConsumables, from {}{} to {}R{}L{}'.format(us.get_name(src), pos, hotel_name, rack, level))
            outputs = __outputs % (pn, pos, barcode, hotel_id, rack, rack_id, level, sealing, tearing, centrifuge, turn)
            turn += 1
            outputs = json.loads(outputs)
            push_list.append(outputs)
    msg1 = json.dumps(msg, indent=4)
    __push_consumables_all_boards_no_wait(src, msg1)


def push_consumable_all_boards_only_for_simulate(src, pos_num=6, is_pro_area=True, is_inter=False,
                                                 sealing='false', tearing='false', centrifuge='false', **kwargs):
    """
    1、获取pos pn号
    2、根据pn号得到堆栈可以存放的位置
    3、下料清单累积一起发
    :param src:工位
    :param kwargs:下料清单
    :return:
    """
    msg = json.loads(__msg_new)
    push_list = msg['message_content']['parameters']['outputs']
    push = kwargs['push']
    pn_list = push.keys()
    can_push_list = us.tell_which_pos_can_push_only_simulate('MGRK01', pos_num, is_pro_area, is_inter)
    turn = 1
    for pn in pn_list:
        if not isinstance(push[pn], tuple):
            my_logger.error('非元组格式，无法处理，请重新输入')
        # 看下pn对应多少个pos
        pos = len(push[pn])
        # can_push_list = us.tell_which_pos_can_push_more(pn, pos_num, is_pro_area, is_inter)
        if can_push_list is None:
            my_logger.error('pn:{}, 堆栈无位置可放'.format(pn))
            return
        for j in range(pos):
            pos = push[pn][j]
            barcode = us.pos_to_barcode(src, pos)
            hotel_name = can_push_list[:][j]['hotel_name']
            hotel_id = can_push_list[:][j]['hotel_id']
            rack = can_push_list[:][j]['rack_idx']
            level = can_push_list[:][j]['level']
            rack_id = can_push_list[:][j]['rack_id']

            # can_push_list.pop(j)

            my_logger.info('pushConsumables, from {}{} to {}R{}L{}'.format(us.get_name(src), pos, hotel_name, rack, level))
            outputs = __outputs % (pn, pos, barcode, hotel_id, rack, rack_id, level, sealing, tearing, centrifuge, turn)
            turn += 1
            outputs = json.loads(outputs)
            push_list.append(outputs)
    msg1 = json.dumps(msg, indent=4)
    __push_consumables_all_boards(src, msg1)


def push_consumables_startlet():
    us.send(us.__topic_task_lims, __msg_startlet)


if __name__ == "__main__":
    try:
        for i in range(1):
            # push_from_pn(us.a_SP96XL1, is_pro_area=True, push={'MGRK01': ('POS13', 'POS14', 'POS15'), 'MGRK02': ('POS26', 'POS27', 'POS28')})
            # push_consumable_all_boards(us.a_SP96XL1, is_pro_area=True, push={'MGRK01': ('POS2', 'POS7')})
            push_consumable_all_boards(us.b_SP100, is_pro_area=False, push={
                'BRMW01': ('POS11',),
                'DNDW01': ('POS7',),
                'GETP01': ('POS4',),
                'BGMX02': ('POS9',)
            })
            # push_consumable_all_boards(us.b_SP100, is_pro_area=False, push={
            #     'BRMW01': ('POS11',),
            #     'DNDW01': ('POS7',),
            #     'GETP01': ('POS4',)
            # })
            # push_consumable_all_boards_only_for_simulate(us.a_SP96XL1, pos_num=3, push={'MGRK01': ('POS7', 'POS12',), 'MGRK02': ('POS8',)})
            # push_consumable_all_boards_only_for_simulate(us.a_SP96XL1, pos_num=1, is_pro_area=False, push={'MGRK01': ('POS17',)})
            # push_consumable_all_boards_only_for_simulate(us.b_SP96XL4, pos_num=1, is_pro_area=True,
            #                                              push={'MGRK01': ('POS18',)})
            # push_consumable_all_boards_only_for_simulate(us.a_SP96XL1, pos_num=3, is_pro_area=True,
            #                                              push={'MGRK01': ('POS12', 'POS13', 'POS16')})
            # push_consumable_all_boards_only_for_simulate(
            #     us.a_SP96XL1, pos_num=1, push={'MGRK01': ('POS2',)})
            # push_consumable_all_boards(
            #     us.a_SP96XL1, push={'BRMW01': ('POS2',), 'DNDW01': ('POS3',), 'GETP01': ('POS4',)})
            # push_consumable_all_boards(us.b_SP100, is_pro_area=False,
            #                            push={'BRMW01': ('POS2',), 'DNDW01': ('POS3',), 'GETP01': ('POS4',)})

            # push_consumable_all_boards(us.b_SP96XL4,
            #                            is_pro_area=False,
            #                            push={'GETP01': ('POS3',)})

            # push_consumable_all_boards(us.a_SP96XL1,
            #                            is_cytomat=True,
            #                            push={'BRMW01': ('POS7',),
            #                                  'DNDW01': ('POS9',)})
            push_consumables_startlet()
    except Exception as e:
        my_logger.error(u'error: %s' % e)
