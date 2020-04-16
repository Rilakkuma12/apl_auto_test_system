#encoding=utf-8
import uuid
from common import base as us
import json
from tools.handle_log import HandleLogger
from tools.handle_task_id import my_task_id

my_logger = HandleLogger()
__TASK_ID = my_task_id.get_task_id()
holder_type_all = ['slider', 'rack']

__msg_push = '''
{
    "message_id": "UUID",
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
}
'''

__msg = '''
{
    "message_id": "UUID",
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
}
'''

__inputs = '''
{
    "material": "%s",
    "position": "%s",
    "barcode": "%s",
    "device_type": "Interaction",
    "device_id": "%s",
    "holder_type": "%s",
    "location": "",
    "rack_idx": "%s",
    "rack_id": "%s",
    "level_idx": "%s",
    "sealing": "%s",
    "tearing": "%s",
    "centrifuge": "%s",
    "idx": "%d"
}'''


__msg_all_rack_to_sp100_rack = '''{
    "message_id": "UUID",
    "message_type": "command",
    "message_group": "task_lims_3fa",
    "message_content": {
        "task_id": "984",
        "device_id": "687c1f6cbb22476ca06e40a102651d7a",
        "command_id": "12ba6736-fbc0-11e9-9d53-977a64c31dff",
        "command": "load",
        "parameters": {
            "inputs": [
                {
                    "material": "MGPH01",
                    "position": "POS4",
                    "barcode": "MGPH010001000001",
                    "device_type": "Interaction",
                    "device_id": "1ddae6cba61e46a0b13458d514e6204f",
                    "holder_type": "rack",
                    "location": "",
                    "rack_idx": "5",
                    "rack_id": "MGPH01",
                    "level_idx": "5",
                    "sealing": "false",
                    "tearing": "false",
                    "centrifuge": "false",
                    "idx": "1"
                },
                {
                    "material": "MGPH01",
                    "position": "POS5",
                    "barcode": "MGPH010001000001",
                    "device_type": "Interaction",
                    "device_id": "1ddae6cba61e46a0b13458d514e6204f",
                    "holder_type": "rack",
                    "location": "",
                    "rack_idx": "5",
                    "rack_id": "MGPH01",
                    "level_idx": "3",
                    "sealing": "false",
                    "tearing": "false",
                    "centrifuge": "false",
                    "idx": "2"
                }
            ]
        }
    }
} 
'''

__msg_all_rack_to_sp100_2 = '''{
    "message_id": "UUID",
    "message_type": "command",
    "message_group": "task_lims_3fa",
    "message_content": {
        "task_id": "984",
        "device_id": "687c1f6cbb22476ca06e40a102651d7a",
        "command_id": "12ba6736-fbc0-11e9-9d53-977a64c31dff",
        "command": "load",
        "parameters": {
            "inputs": [
                {
                    "material": "BRMW01",
                    "position": "POS4",
                    "barcode": "BRMW010001000001",
                    "device_type": "Interaction",
                    "device_id": "1ddae6cba61e46a0b13458d514e6204f",
                    "holder_type": "slider",
                    "location": "",
                    "rack_idx": "1",
                    "rack_id": "BRMW01",
                    "level_idx": "1",
                    "sealing": "false",
                    "tearing": "false",
                    "centrifuge": "false",
                    "idx": "1"
                },
                {
                    "material": "BRMW01",
                    "position": "POS5",
                    "barcode": "BRMW010001000001",
                    "device_type": "Interaction",
                    "device_id": "1ddae6cba61e46a0b13458d514e6204f",
                    "holder_type": "slider",
                    "location": "",
                    "rack_idx": "3",
                    "rack_id": "BRMW01",
                    "level_idx": "1",
                    "sealing": "false",
                    "tearing": "false",
                    "centrifuge": "false",
                    "idx": "2"
                }
            ]
        }
    }
} 
'''


def __load_consumables_all_board(dest, msg):
    # 测试设备操作：上料
    # rst = int(random()*3)
    command_id = uuid.uuid1()
    comm = msg % (us.__topic_task_lims, __TASK_ID, dest, command_id)
    return comm, command_id, __TASK_ID


def __load_consumables_all_boards(dest, msg):
    msg_load, com_id_load, task_id = __load_consumables_all_board(dest, msg)
    my_logger.info('loadConsumables from interaction,command id: {}'.format(com_id_load))
    us.send(us.__topic_task_lims, msg_load)
    if us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_load):
        pass
    else:
        raise Exception


def load_consumable_from_inter(dest, src=us.a_interaction, rack_idx='6', level_idx='5', rack_id='MGPH01', barcode='MGPH010001000001', sealing='false', tearing='false', centrifuge='false', **kwargs):
    msg = json.loads(__msg)  # 把msg转换为字典
    load_list = msg['message_content']['parameters']['inputs']
    # us.hotel_store()  # 先获取一下堆栈库存
    load = kwargs['load']
    turn = 1
    for key in load.keys():
        nums = len(load[key])
        for j in range(nums):
            hotel_id = src
            if rack_idx in '1234':
                level_idx = '1'
                holder_type = holder_type_all[0]
            else:
                holder_type = holder_type_all[1]
            # if hotel == 'AI1':
            #     hotel_id = us.a_interaction
            # else:
            #     hotel_id = None
            pos = load[key][j]
            # rack_id = 'MGPH01'
            my_logger.info('loadConsumables all boards, from {}R{}L{} to {}{}'.format(us.get_name(src), rack_idx, level_idx, us.get_name(dest), pos))
            # 将获取的上料信息插入msg字典
            inputs = __inputs % (key, pos, barcode, hotel_id, holder_type, rack_idx, rack_id, level_idx, sealing, tearing, centrifuge, turn)
            turn += 1
            inputs = json.loads(inputs)
            load_list.append(inputs)
    # 再把msg转回字符串
    msg1 = json.dumps(msg, indent=4)
    __load_consumables_all_boards(dest, msg1)


def load_2_consumable_from_inter_slider():
    com_id_load, task_id = ('12ba6736-fbc0-11e9-9d53-977a64c31dff', '984')
    my_logger.info('loadConsumables from interaction,command id: {}'.format(com_id_load))
    us.send(us.__topic_task_lims, __msg_all_rack_to_sp100_2)
    if us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_load):
        pass
    else:
        raise Exception


def load_2_consumable_from_inter_rack():
    com_id_load, task_id = ('12ba6736-fbc0-11e9-9d53-977a64c31dff', '984')
    my_logger.info('loadConsumables from interaction,command id: {}'.format(com_id_load))
    us.send(us.__topic_task_lims, __msg_all_rack_to_sp100_rack)
    if us.wait_task_complete(us.consumer_task_apl, us.__topic_task_apl, com_id_load):
        pass
    else:
        raise Exception


def push_consumable_to_inter(src, hotel=us.a_interaction, rack_idx='5', level_idx='5', rack_id='MGPH01', barcode='MGPH010001000001',
                             sealing='false', tearing='false', centrifuge='false', **kwargs):
    msg = json.loads(__msg_push)
    push_list = msg['message_content']['parameters']['outputs']
    push = kwargs['push']
    pn_list = push.keys()
    turn = 1
    for pn in pn_list:
        if not isinstance(push[pn], tuple):
            my_logger.error('非元组格式，无法处理，请重新输入')
        # 看下pn对应多少个pos
        pos_num = len(push[pn])
        for j in range(pos_num):
            pos = push[pn][j]
            hotel_name = 'AI1'
            hotel_id = hotel
            if rack_idx in '1234':
                holder_type = holder_type_all[0]
            else:
                holder_type = holder_type_all[1]
            my_logger.info('pushConsumables, from {}{} to {}R{}L{}'.format(us.get_name(src), pos, hotel_name, rack_idx, level_idx))
            outputs = __inputs % (pn, pos, barcode, hotel_id, holder_type, rack_idx, rack_id, level_idx, sealing, tearing, centrifuge, turn)
            turn += 1
            outputs = json.loads(outputs)
            push_list.append(outputs)
    msg1 = json.dumps(msg, indent=4)
    __load_consumables_all_boards(src, msg1)


if __name__ == "__main__":
    try:
        for i in range(1):
            # kafka_device_command.scan_hotel(us.a_interaction)
            # load_consumable_from_inter(us.a_SP96XL1, rack_idx='5', level_idx='1', barcode='MGPH010001000001', load={'MGPH01': ('POS5',)})
            load_2_consumable_from_inter_rack()
            push_consumable_to_inter(us.a_SP96XL1, rack_idx='9', level_idx='3', barcode='MGPH010001000001',
                                     push={'MGPH01': ('POS4',)})
            push_consumable_to_inter(us.a_SP96XL1, rack_idx='9', level_idx='5', barcode='MGPH010001000001',
                                     push={'MGPH01': ('POS5',)})
            load_consumable_from_inter(us.a_SP96XL1, rack_idx='5', level_idx='3', barcode='MGPH010001000001', load={'MGPH01': ('POS4',)})
            # push_consumable_to_inter(us.a_SP96XL1, rack_idx='5', level_idx='3', barcode='MGPH010001000001', push={'MGPH01': ('POS4',)})

            # load_consumable_from_inter(us.a_SP96XL1, rack_idx='5', level_idx='5', barcode='MGPH010001000001', load={'MGPH01': ('POS3',)})
            # push_consumable_to_inter(us.a_SP96XL1, rack_idx='5', level_idx='5', barcode='MGPH010001000001', push={'MGPH01': ('POS3',)})

            # load_consumable_from_inter(us.b_SP96XL4, src=us.b_interaction, rack_idx='1', level_idx='1', rack_id='BRMW01', barcode='BGMW010001000001', load={'BRMW01': ('POS15',)})
            # push_consumable_to_inter(us.b_SP96XL4, hotel=us.b_interaction, rack_idx='1', level_idx='1', rack_id='BRMW01', barcode='BGMW010001000001', push={'BRMW01': ('POS15',)})

            # load_consumable_from_inter(us.b_SP100, src=us.b_interaction,
            #                            tearing='true',
            #                            rack_idx='2', level_idx='1',
            #                            rack_id='BRMW01', barcode='BRMW010001000001', load={'BRMW01': ('POS9',)})
            # push_consumable_to_inter(us.b_SP100, hotel=us.b_interaction, rack_idx='1', level_idx='1',
            #                          rack_id='BRMW01', barcode='BRMW010001000001', push={'BRMW01': ('POS2',)})
            # load_consumable_from_inter(us.a_SP96XL1, rack_idx='1', level_idx='1', rack_id='MGRK01',
            #                            barcode='MGRK010001000001', load={'MGRK01': ('POS17',)})
            # load_consumable_from_inter(us.a_SP96XL1, rack_idx='5', level_idx='5', rack_id='MGRK01',
            #                            barcode='MGRK010001000001', load={'MGRK01': ('POS18',)})
            # load_2_consumable_from_inter_slider()
            # push_consumable_to_inter(us.b_SP100, hotel=us.b_interaction, rack_idx='2', level_idx='1',
            #                          rack_id='BRMW01', barcode='BRMW010001000001', push={'BRMW01': ('POS4',)})
            # push_consumable_to_inter(us.b_SP100, hotel=us.b_interaction, rack_idx='4', level_idx='1',
            #                          rack_id='BRMW01', barcode='BRMW010001000001', push={'BRMW01': ('POS5',)})

    except Exception as e:
        my_logger.error(u'error: %s' % e)

