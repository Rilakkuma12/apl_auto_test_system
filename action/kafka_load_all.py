# encoding=utf-8
import uuid
from common.base import Base
import json
from tools.handle_log import HandleLogger
from action.kafka_load import KafkaLoad
from common.hotel_manage import HotelManage
from common.table_manage import TableManage
from tools.handle_task_id import my_task_id
from tools.handle_command_id import HandleCommandId
my_logger = HandleLogger()
my_hotel = HotelManage()
my_table = TableManage()
us = Base()
my_command_id = HandleCommandId()


class KafkaLoadAll:
    topic = us.topic_task_lims
    turn = 0
    device_list = {
        'module1': us.a_SP96XL1,
        'module2': us.a_SP96XL2,
        'module3': us.a_SP96XL1,
        'interaction1': us.a_interaction,
        'interaction2': us.b_interaction
    }
    holder_type_all = ['slider', 'rack']
    # 1代表前区，2代表后区
    area_map = {'1': True, '2': False}

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
    }
    '''

    __inputs_hotel = '''
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
        "idx": %d,
        "centrifuge_pn": "%s"
    }'''

    __inputs_module = """
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
        "idx": %d,
        "centrifuge_pn": "%s"
    }
    """

    __inputs_inter = '''
    {
        "material": "%s",
        "position": "%s",
        "barcode": "%s",
        "device_type": "Interaction",
        "device_id": "%s",
        "holder_type": "%s",
        "location": "",
        "rack_idx": "%s",
        "rack_id": "",
        "level_idx": "%s",
        "sealing": "%s",
        "tearing": "%s",
        "centrifuge": "%s",
        "idx": %d,
        "centrifuge_pn": "%s"
    }'''

    msg = json.loads(__msg)  # 把msg转换为字典
    load_list = msg['message_content']['parameters']['inputs']

    sealing = False
    tear = False
    centrifugal = False
    centrifuge_pn = ''

    def __init__(self, task_id=my_task_id.get_task_id()):
        self.task_id = task_id

    def load_materials_all(self, dest, **kwargs):
        self.get_load_materials_input(**kwargs)
        msg_str = json.dumps(self.msg, indent=4)
        self.load_consumables_all_boards(dest, msg_str)
        # 上完一轮料，清空上料列表，清空idx
        self.load_list.clear()
        self.turn = 0

    def find_material_from_hotel(self, key, is_pre, is_fridge):
        barcode = my_hotel.pn_to_barcode(key, is_pre, is_fridge)
        addr = my_hotel.barcode_to_addr(barcode, is_pre, is_fridge)
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
        rack_id = my_hotel.barcode_to_rack(barcode, is_pre, is_fridge)
        return barcode, hotel_id, rack_idx, rack_id, level_idx

    def get_load_materials_input(self, **kwargs):
        """返回input数组"""
        load = kwargs['load']

        for material_list in load.items():
            pn = material_list[0][:6]
            for item in material_list[1].items():
                pos = item[0]
                area, src, location, sealing, tear, centrifugal, centrifuge_pn = self.get_param_list(item[1])

                if src == 'hotel':
                    # 从冰箱上料
                    barcode, hotel_id, rack_idx, rack_id, level_idx = self.find_material_from_hotel(pn,
                                                                                                    self.area_map[area],
                                                                                                    False)
                    input_hotel = self.__inputs_hotel % (pn, pos, barcode, hotel_id,
                                                         rack_idx, rack_id, level_idx,
                                                         sealing, tear, centrifugal, self.turn, centrifuge_pn)
                    self.turn += 1
                    input_hotel = json.loads(input_hotel)
                    self.load_list.append(input_hotel)

                elif src == 'fridge':
                    # 从冰箱上料
                    barcode, hotel_id, rack_idx, rack_id, level_idx = self.find_material_from_hotel(pn,
                                                                                                    self.area_map[area],
                                                                                                    True)
                    input_hotel = self.__inputs_hotel % (pn, pos, barcode, hotel_id,
                                                         rack_idx, rack_id, level_idx,
                                                         sealing, tear, centrifugal, self.turn, centrifuge_pn)
                    self.turn += 1
                    input_hotel = json.loads(input_hotel)
                    self.load_list.append(input_hotel)

                elif 'module' in src:
                    # 从工位转移
                    barcode = my_table.pos_to_barcode(self.device_list[src], location)
                    input_module = self.__inputs_module % (pn, pos, barcode,
                                                           self.device_list[src],
                                                           location, sealing, tear, centrifugal,
                                                           self.turn, centrifuge_pn)
                    self.turn += 1
                    input_module = json.loads(input_module)
                    self.load_list.append(input_module)

                elif 'inter' in src:
                    # 从交互区上料
                    if location[3] in '1234':
                        barcode = 'BRMW010000000001'
                        # barcode = 'GBRS010000000001'
                        holder_type = self.holder_type_all[0]
                    else:
                        barcode = 'MGPH010001000001'
                        holder_type = self.holder_type_all[1]
                    input_inter = self.__inputs_inter % (pn, pos, barcode,
                                                         self.device_list[src],
                                                         holder_type,
                                                         location[3], location[4],
                                                         sealing, tear, centrifugal, self.turn, centrifuge_pn)

                    self.turn += 1
                    input_inter = json.loads(input_inter)
                    self.load_list.append(input_inter)

    def get_param_list(self, param_lists):
        param_list = param_lists.split(':')
        area = param_list[0]
        src = param_list[1]
        location = param_list[2]

        sealing = eval(param_list[3].split('-')[1]) if param_list[3] is not None else self.sealing
        tear = eval(param_list[4].split('-')[1]) if param_list[4] is not None else self.tear
        centrifugal = eval(param_list[5].split('-')[1]) if param_list[5] is not None else self.centrifugal
        centrifugal_pn = param_list[6] if param_list[6] is not None else self.centrifuge_pn

        return area, src, location, sealing, tear, centrifugal, centrifugal_pn

    def load_consumables_all_boards(self, dest, msg):
        command_id = my_command_id.get_command_id()
        __TASK_ID = self.task_id
        msg_load, com_id_load, task_id = \
            (msg % (self.topic, __TASK_ID, dest, command_id)), command_id, __TASK_ID
        my_logger.info('loadConsumables all boards,command id:{}，task id：{}'.format(com_id_load, task_id))
        us.send(self.topic, msg_load)
        if us.wait_task_complete(us.consumer_task_apl, us.topic_task_apl, com_id_load):
            pass
        else:
            raise Exception('上料任务失败结束')


load_all = KafkaLoadAll()
if __name__ == '__main__':

    load_all.load_materials_all(us.b_SP100,
                            load={
                                'BRMW01': {
                                        'POS4': '2:interaction2:POS11:sealing-False:tear-False:cen-False:',
                                        # # 'POS3': '2:fridge::sealing-False:tear-False:cen-False:',
                                        # # 'POS4': '1:module1:POS4:sealing-False:tear-False:cen-False:',
                                        # 'POS9': '2:interaction2:POS41:sealing-False:tear-False:cen-False:',
                                        # 'POS10': '2:interaction2:POS55:sealing-False:tear-False:cen-False:'
                                        }
                                })

