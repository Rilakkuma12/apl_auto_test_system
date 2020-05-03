#encoding=utf-8
import uuid
from common.base import Base
from tools.handle_log import my_logger
import json
from tools.handle_task_id import my_task_id
from common.table_manage import TableManage
from common.hotel_manage import HotelManage
from tools.handle_command_id import my_comm_id, HandleCommandId

__TASK_ID = my_task_id.get_task_id()
barcodes = []
my_hotel = HotelManage()
my_table = TableManage()
us = Base()
my_command_id = HandleCommandId()


class KafkaPushAll:
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
                "outputs": []
            }
        }
    }'''

    __outputs_hotel = '''
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

    __outputs_inter = '''
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
        "idx": %d
    }'''

    topic = us.topic_task_lims
    msg = json.loads(__msg)  # 把msg转换为字典
    push_list = msg['message_content']['parameters']['outputs']
    turn = 0
    sealing = False
    tear = False
    centrifugal = False
    area_map = {'1': True, '2': False}
    holder_type_all = ['slider', 'rack']
    device_list = {
        'module1': us.a_SP96XL1,
        'module2': us.a_SP96XL2,
        'module3': us.a_SP96XL1,
        'interaction1': us.a_interaction,
        'interaction2': us.b_interaction,
        'AH1': us.a_HotelA,
        'AH2': us.a_HotelB,
        'BH1': us.b_HotelA,
        'BH2': us.b_HotelB,
        'AC1': us.a_CytomatA,
    }

    def push_consumables_all_boards(self, src, msg):
        comm_id = my_command_id.get_command_id()
        task_id = my_task_id.get_task_id()
        msg_push = msg % (self.topic, task_id, src, comm_id)
        my_logger.info('push consumables all boards,command id: {},task id: {}'.format(comm_id, task_id))
        us.send(us.topic_task_lims, msg_push)
        if us.wait_task_complete(us.consumer_task_apl, us.topic_task_apl, comm_id):
            pass
        else:
            raise Exception

    def push_materials_all(self, src, **kwargs):
        self.get_push_materials_output(src, **kwargs)
        msg_str = json.dumps(self.msg, indent=4)
        self.push_consumables_all_boards(src, msg_str)
        # 上完一轮料，清空上料列表，清空idx
        self.push_list.clear()
        self.turn = 0

    def get_push_materials_output(self, src, **kwargs):
        push = kwargs['push']
        for material_list in push.items():
            pn = material_list[0][:6]
            for item in material_list[1].items():
                pos = item[0]
                barcode = my_table.pos_to_barcode(src, pos)
                area, dest, location, sealing, tear, centrifugal = \
                    self.get_param_list(item[1])

                if dest == 'hotel':
                    # 堆栈下料
                    hotel_id, rack_idx, rack_id, level_idx = self.find_pos_from_hotel(pn, self.area_map[area], False)
                    output_hotel = self.__outputs_hotel % (pn, pos, barcode, hotel_id, rack_idx, rack_id, level_idx,
                                                           sealing, tear, centrifugal, self.turn)
                    self.turn += 1
                    output_hotel = json.loads(output_hotel)
                    self.push_list.append(output_hotel)

                elif dest == 'fridge':
                    # 冰箱下料
                    hotel_id, rack_idx, rack_id, level_idx = self.find_pos_from_hotel(pn, self.area_map[area], True)
                    output_hotel = self.__outputs_hotel % (pn, pos, barcode, hotel_id, rack_idx, rack_id, level_idx,
                                                           sealing, tear, centrifugal, self.turn)
                    self.turn += 1
                    output_hotel = json.loads(output_hotel)
                    self.push_list.append(output_hotel)

                elif 'inter' in dest:
                    # 从交互区上料
                    if location[3] in '1234':
                        holder_type = self.holder_type_all[0]
                    else:
                        holder_type = self.holder_type_all[1]
                    output_inter = self.__outputs_inter % (pn, pos, barcode,
                                                           self.device_list[dest],
                                                           holder_type,
                                                           location[3], location[4],
                                                           sealing, tear, centrifugal, self.turn)

                    self.turn += 1
                    output_inter = json.loads(output_inter)
                    self.push_list.append(output_inter)

    def get_param_list(self, param_lists):
        param_list = param_lists.split(':')
        area = param_list[0]
        src = param_list[1]
        location = param_list[2]

        sealing = eval(param_list[3].split('-')[1]) if param_list[3] is not None else self.sealing
        tear = eval(param_list[4].split('-')[1]) if param_list[4] is not None else self.tear
        centrifugal = eval(param_list[5].split('-')[1]) if param_list[5] is not None else self.centrifugal
        return area, src, location, sealing, tear, centrifugal

    def find_pos_from_hotel(self, pn, is_pre, is_fridge):
        can_push_addr = my_hotel.tell_which_pos_can_push(pn, is_pre, is_fridge)
        if can_push_addr is None:
            my_logger.error('pn:{}, 堆栈无位置可放'.format(pn))
            return
        hotel_name = can_push_addr[:3]
        hotel_id = self.device_list[hotel_name]
        rack = can_push_addr[can_push_addr.index('R') + 1: can_push_addr.index('L')]
        level = can_push_addr[can_push_addr.index('L') + 1:]
        rack_id = my_hotel.addr_to_rack_id(can_push_addr)
        return hotel_id, rack, rack_id, level


if __name__ == "__main__":
    try:
        pushall = KafkaPushAll()
        # pushall.push_materials_all(us.b_SP96XL4,
        #                         push={
        #                             'BRMW01': {
        #                                 # 'POS8': '2:interaction2:POS41:sealing-False:tear-False:cen-False',
        #                                 'POS9': '2:interaction2:POS11:sealing-False:tear-False:cen-False',
        #                                 # 'POS8': '2:hotel::sealing-False:tear-False:cen-False',
        #                             }
        #                             # 'MGRK01-1': {
        #                             #     'POS6': '1:hotel::sealing-False:tear-False:cen-False',
        #                             # }
        #                         })
        # pushall.push_materials_all(us.b_SP96XL4,
        #                            push={
        #                                'MGPH01': {
        #                                    # 'POS8': '2:hotel::sealing-False:tear-False:cen-False',
        #                                    'POS10': '2:interaction2:POS41:sealing-False:tear-False:cen-False'
        #                                }
        #                            })
        pushall.push_materials_all(us.b_SP96XL4,
                                   push={
                                       'MGRK01': {
                                           'POS8': '2:hotel::sealing-False:tear-False:cen-False',
                                           # 'POS3': '2:fridge::sealing-False:tear-False:cen-False',
                                           # 'POS4': '1:module1:POS4:sealing-False:tear-False:cen-False',
                                           'POS10': '2:interaction2:POS55:sealing-False:tear-False:cen-False',
                                           'POS9': '2:interaction2:POS41:sealing-False:tear-False:cen-False'
                                       }
                                   })
    except Exception as e:
        my_logger.error(u'error: %s' % e)
