# encoding=utf-8
import uuid
from common.base import Base as us
import json
from tools.handle_log import HandleLogger
from tools.handle_task_id import my_task_id

my_logger = HandleLogger()


class KafkaLoad:
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

    def __init__(self):
        self.my_store = list(us.hotel_store())
        self.__TASK_ID = my_task_id.get_task_id()
        self.command_id = uuid.uuid1()
        self.topic = us.topic_task_lims
        self.__topic_task_apl = us.topic_task_apl

    def load_materials(self, dest, is_pre_area=True,
                       is_fridge=False, sealing=False, tear=False, centrifugal=False, **kwargs):
        """
        1.源设备：堆栈，冰箱，交互区
        2.源位置：rack， level
        3.目标设备：工位
        4.目标位置：pos
        5.中间过程：封膜、撕膜、离心
        6.上料过程：
            1.根据pn，找堆栈对应物料，获取barcode及对应位置rl
            2.发送消息
            3.记录日志
            4.等待响应返回
        :return:
        """
        msg = json.loads(self.__msg)  # 把msg转换为字典
        load_list = msg['message_content']['parameters']['inputs']
        load = kwargs['load']
        turn = 1
        for key in load.keys():
            nums = len(load[key])
            barcodes = us.pn_to_barcodes(self.my_store, key, is_pre_area, is_fridge)[: nums]
            for j in range(len(barcodes)):
                barcode = barcodes[j]
                # for hotel_store in self.my_store[:]:
                #     for store in hotel_store:
                #         if store is None or store == []:
                #             continue
                #         elif store[0]['barcode'] == barcode:
                #             hotel_store.remove(store)
                addr = us.barcode_to_addr(barcode, is_pre_area, is_fridge)
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
                rack_id = us.barcode_to_rack(barcode, is_pre_area, False)
                my_logger.info('loadConsumables all boards, from {}R{}L{} to {}{}'.format(hotel, rack_idx, level_idx,
                                                                                          us.get_name(dest), pos))
                # 将获取的上料信息插入msg字典
                inputs = self.__inputs % (
                    key, pos, barcode, hotel_id, rack_idx, rack_id, level_idx, sealing, tear, centrifugal, turn)
                turn += 1
                inputs = json.loads(inputs)
                load_list.append(inputs)
        # 再把msg转回字符串
        msg1 = json.dumps(msg, indent=4)
        self.load_consumables_all_boards(dest, msg1)

    def load_consumables_all_boards(self, dest, msg):
        msg_load, com_id_load, task_id = (msg % (self.topic, self.__TASK_ID, dest, self.command_id)), \
                                         self.command_id, \
                                         self.__TASK_ID
        my_logger.info('loadConsumables all boards,command id:{}，task id：{}'.format(com_id_load, task_id))
        us.send(self.topic, msg_load)
        if us.wait_task_complete(us.consumer_task_apl, us.topic_task_apl, com_id_load):
            pass
        else:
            raise Exception('上料任务失败结束')


if __name__ == "__main__":
    try:
        for i in range(1):
            aa = KafkaLoad()
            # aa.load_materials(us.a_SP96XL1, load={
            #     'BRMW01': ('POS2', 'POS11'),
            #     'GETP01': ('POS4',),
            #     'BGMX02': ('POS9', ),
            #     'DNDW01': ('POS7',)})
            aa.load_materials(us.a_interaction, load={
                'MGRK01': ('POS2', 'POS11'),
                'MGRK02': ('POS4',),
                'MGRK03': ('POS9',)})

    except Exception as e:
        my_logger.error(u'error: %s' % e)

