#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/6/3 17:36
# 这个脚本用于存放通用函数，比如发送指令、查询任务完成等
import json
import uuid
import sys

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import os
from datetime import datetime
import datetime as dt
import socket
from tools.handle_log import my_logger
from tools.handle_config import config
import requests
import time
import copy
from tools.handle_excel import HandleExcel
from tools.constance import TIME_RECORD_PATH
from tools.handle_postgres import my_pg


class Base:
    # 获取本机电脑名
    my_name = socket.getfqdn(socket.gethostname())
    # 获取本机ip
    my_addr = socket.gethostbyname(my_name)

    record_file = HandleExcel(TIME_RECORD_PATH)
    # kafka主题
    topic_device = config.get_value('kafka', 'topic_device')
    topic_storage_lims = config.get_value('kafka', 'topic_storage_lims')
    topic_task_lims = config.get_value('kafka', 'topic_task_lims')
    topic_storage_apl = config.get_value('kafka', 'topic_storage_apl')
    topic_task_apl = config.get_value('kafka', 'topic_task_apl')
    __KAFKA_SERVER = config.get_value('kafka', 'KAFKA_SERVER')
    __TASK_ID = (datetime.now().isoformat()).replace(':', '-')
    server_url = config.get_value('swagger', 'server_url')

    # __topic_device_ = config.get_value('kafka', 'topic_device_')
    # __topic_storage_lims_ = config.get_value('kafka', 'topic_storage_lims_')
    # topic_task_lims_ = config.get_value('kafka', 'topic_task_lims_')
    # __topic_storage_apl_ = config.get_value('kafka', 'topic_storage_apl_')
    # __topic_task_apl_ = config.get_value('kafka', 'topic_task_apl_')

    producer = KafkaProducer(bootstrap_servers=[__KAFKA_SERVER], retries=3)
    consumer_device = KafkaConsumer(topic_device, bootstrap_servers=[__KAFKA_SERVER])
    consumer_storage_apl = KafkaConsumer(topic_storage_apl, bootstrap_servers=[__KAFKA_SERVER])
    consumer_task_apl = KafkaConsumer(topic_task_apl, bootstrap_servers=[__KAFKA_SERVER])

    response_type = {topic_storage_apl: 'device_response', topic_task_apl: 'complete'}

    # 设备id
    a_HotelA = my_pg.get_device_id(1, 'HotelA')
    a_HotelB = my_pg.get_device_id(1, 'HotelB')
    a_SP96XL1 = my_pg.get_device_id(1, 'MGISP-96XLEX@')
    # a_SP96XL2 = config.get_value('device id', 'a_SP96XL2')
    a_SP96XL2 = 'b15842d15efa4f68a0051cbfcaf5e37d'
    # a_SP96XL3 = config.get_value('device id', 'a_SP96XL3')
    a_interaction = my_pg.get_device_id(1, 'Interaction')
    a_CytomatA =  my_pg.get_device_id(1, 'CytomatA')

    b_SP96XL4 = my_pg.get_device_id(2, 'MGISP-96XLEX')
    b_SP100 = my_pg.get_device_id(2, 'MGISP-100Plus')
    b_HotelA = my_pg.get_device_id(2, 'HotelA')
    b_HotelB = my_pg.get_device_id(2, 'HotelB')
    b_interaction = my_pg.get_device_id(2, 'Interaction')
    b_startlet = my_pg.get_device_id(2, 'Hamilton-Test-Last')
    b_bmg = my_pg.get_device_id(2, 'BMG-Test-Last')

    var = ("hours", "minutes", "seconds")
    time2sec = lambda x: int(dt.timedelta(**{k: int(v) for k, v in zip(var, x.strip().split(":"))}).total_seconds())
    # MGRK02:7层，MGRK03:13层，MGRK04:18层，MGRK01、MGRK05、MGRK06:4层
    rack_to_pn = {
        'MGRK01': ('MGRK01', 'CRTP03', 'CRTF03'),  # Hamilton吸头（1mL）
        'MGRK02': ('MGRK02', 'GETP01', 'GETP02', 'GETF01', 'GETF02'),  # tips盒
        'MGRK03': ('MGRK03', 'DNDW01', 'BGBD01', 'BGBD02', 'BGBD03', 'BGBD04', 'BGBD05', 'BGTE01', 'BGTE02', 'BGTE03', 'BGET01', 'BGLE01', 'BGW101', 'BGW201'),  # 深孔板
        'MGRK04': ('MGRK04', 'BRMW01', 'BGMX01', 'BGMX02', 'BGMX03', 'BGMX04', 'BGBF01', 'BGBF02', 'BGBF03', 'BGEZ01', 'BGEZ02', 'BGPM01', 'BGBC01', 'EDUV01', 'MSMW01'),  # PCR板
        'MGRK05': ('MGRK05',),  # Hamilton吸头（50μL）
        'MGRK06': ('MGRK06', 'CRTP01', 'CRTP02', 'CRTF01', 'CRAF01', 'CRAF02', 'CRAF03', 'CRAP02')}  # Hamilton吸头（300μL）

    rack_to_pn_cytomat = {
        'TMRK01': ('MGRK01', 'DNDW01',),
        'TMRK02': ('MGRK02', 'BRMW01',)}

    rack_to_level_num = {
        'MGRK01': 4,  # Hamilton吸头（1mL）
        'MGRK02': 7,  # tips盒
        'MGRK03': 13,  # 深孔板
        'MGRK04': 18,  # PCR板
        'MGRK05': 4,  # Hamilton吸头（50μL）
        'MGRK06': 4  # Hamilton吸头（300μL）
    }

    @classmethod
    def query_url(cls, param):
        url = cls.server_url + param
        response = requests.post(url)
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data

    # 这是一个获取函数名的装饰器
    @staticmethod
    def get_func_name(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f'执行函数名{func.__name__}')
        return wrapper

    @staticmethod
    def post(url, data=None):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json-patch+json'}
        return requests.post(url, data=json.dumps(data), headers=headers)

    @staticmethod
    def on_send_success(args):
        my_logger.info('send success. offset: %s' % args.offset)

    @staticmethod
    def on_send_error(err):
        my_logger.error('send err. offset: %s' % err.offset)

    def send(self, topic, msg):
        # global producer
        task_id = str(uuid.uuid1())
        try:
            r = self.producer.send(topic, msg.encode('ascii'),
                                   task_id.encode('ascii')).add_callback(self.on_send_success).add_errback(self.on_send_error)
            my_logger.debug(msg)
            return r.get(timeout=20)
        except KafkaError as e:
            print('KafkaError')
            my_logger.error(e)

    def wait_command_complete(self, consumer, topic,  comm_id):
        start = datetime.now()
        my_logger.info('waiting...')
        for msg in consumer:
            value = json.loads(msg.value.decode('utf-8'))
            if value is None:
                continue
            if not isinstance(value, dict):
                value = json.loads(value)
            # print(value)
            # print(value['message_content'])
            message_type = value['message_type']
            if message_type != self.response_type[topic]:
                continue
            content = value['message_content']
            if (str(comm_id) in content['command_id']) and ('done' in content['response']):
                end = datetime.now()
                processing_time = str(end - start)
                my_logger.info('task completed success! occupied: {} '.format(processing_time))
                # 将耗时写入记录文件
                # record_file.record_time(row=getattr(HandleExcel, 'current_row'), col=record_file.get_max_col(),
                #                         result=processing_time)
                return True
            elif (str(comm_id) in content['command_id']) and ('failure' in content['response']):
                end = datetime.now()
                processing_time = str(end - start)
                my_logger.info('task completed fail! occupied: {}'.format(processing_time))
                # 将耗时写入记录文件
                # record_file.record_time(row=getattr(HandleExcel, 'current_row'), col=record_file.get_max_col(),
                #                         result=processing_time)
                return False
            else:
                continue

    def wait_task_complete(self, consumer, topic, comm_id):
        start = datetime.now()
        my_logger.info('waiting...')
        for msg in consumer:
            value = json.loads(msg.value.decode('utf-8'))
            if value is None:
                continue
            if not isinstance(value, dict):
                value = json.loads(value)
            message_type = value['message_type']
            if message_type != self.response_type[topic]:
                continue
            content = value['message_content']
            if (str(comm_id) in content['command_id']) and ('success' in content['complete_status']):
                end = datetime.now()
                processing_time = str(end - start)
                my_logger.info('task completed success! occupied: {} '.format(processing_time))
                # 将耗时写入记录文件
                # write_to_record_file(processing_time)
                return True
            elif (str(comm_id) in content['command_id']) and ('failure' in content['complete_status']):
                end = datetime.now()
                processing_time = str(end - start)
                my_logger.info('task completed fail! occupied: {}'.format(processing_time))
                my_logger.error(f"failure reason: {content['msg']}")
                # 将耗时写入记录文件
                # write_to_record_file(processing_time)
                return False
            else:
                continue
# def hotel_store_for_push():
#     hotel_goods_ah = []
#     hotel_goods_bh = []
#     url = __SERVER_URL + "Query/QueryHotel"
#     response = requests.post(url)
#     if response.status_code == 200:
#         data = json.loads(response.content.decode('utf-8'))
#         for hotel in data:
#             if hotel['Id'] == a_HotelA:
#                 prefix = 'AH1'
#             elif hotel['Id'] == a_HotelB:
#                 prefix = 'AH2'
#             elif hotel['Id'] == b_HotelA:
#                 prefix = 'BH1'
#             elif hotel['Id'] == b_HotelB:
#                 prefix = 'BH2'
#             else:
#                 my_logger.error('Unknown hotel {}'.format(hotel['Name']))
#             for rack in hotel['Racks']:
#                 rack_id = rack['RackId']
#                 for consumable in rack['Consumables']:
#                     if 'AH' in prefix:
#                         hotel_goods_ah.append([{'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']), 'barcode': consumable['Code'], 'pn': consumable['PN'], 'rack_id': rack_id}])
#                     else:
#                         hotel_goods_bh.append([{'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']), 'barcode': consumable['Code'], 'pn': consumable['PN'], 'rack_id': rack_id}])
#         my_logger.debug('query hotel store, hotel ah:{}, hotel bh:{}'.format(hotel_goods_ah, hotel_goods_bh))
#         return hotel_goods_ah, hotel_goods_bh

    @staticmethod
    def get_name(arg):
        gl = globals().copy()
        for i in gl:
            if gl[i] is arg:
                return i

    def get_pcr_mix_request_info(self):
        my_logger.info('getting pcr_mix request...')
        for msg in self.consumer_task_apl:
            value = json.loads(msg.value.decode('utf-8'))
            if not isinstance(value, dict):
                value = json.loads(value)
            message_type = value['message_type']
            if message_type != 'run_request':
                continue
            else:
                content = value['message_content']
                task_id = content['task_id']
                request_id = content['request_id']
                return task_id, request_id

    def get_robot_request_exception_info(self):
        my_logger.info('getting robot exception request...')
        for msg in self.consumer_task_apl:
            if msg is None:
                continue
            value = json.loads(msg.value.decode('utf-8'))
            if value is None:
                continue
            if not isinstance(value, dict):
                value = json.loads(value)
            message_type = value['message_type']
            if message_type != 'transfer_request':
                continue
            else:
                content = value['message_content']
                request_id = content['request_id']
                task_id = content['task_id']
                barcode = content['parameters']['plate_barcode']
                idx = content['parameters']['idx']
                my_logger.info('received robot exception request_id: {}'.format(request_id))
                return task_id, request_id, barcode, idx

    def get_inter_request_info(self):
        my_logger.info('getting interaction request...')
        for msg in self.consumer_task_apl:
            if msg is None:
                continue
            value = json.loads(msg.value.decode('utf-8'))
            if value is None:
                continue
            if not isinstance(value, dict):
                value = json.loads(value)
            message_type = value['message_type']
            if message_type != 'load_request':
                continue
            else:
                content = value['message_content']
                # task_id = content['task_id']
                request_id = content['request_id']
                param = content['parameters']
                target_device_id = param['target_device_id']
                position = param['position']
                barcode = param['barcode']
                source_device_id = param['source_device_id']
                rack_idx = param['rack_idx']
                level_idx = param['level_idx']
                my_logger.info('received interaction request_id: {}'.format(request_id))
                return request_id, target_device_id, position, barcode, source_device_id, rack_idx, level_idx

    def ack_task(self, task_id):
        api = self.server_url + "Query/QueryTask?taskid=" + task_id
        return self.post(api)

    def wait_task_complete_api(self, task_id):
        resp = self.ack_task(task_id)
        while resp.text != 'true':
            resp = self.ack_task(task_id)
            time.sleep(1)

    def write_to_record_file(self, data):
        # 将耗时写入记录文件
        try:
            row = getattr(HandleExcel, 'current_row')
        except Exception as e:
            my_logger.debug("err: {}".format(e))
            row = 2
        col = 1
        while self.record_file.get_cell_value(row=row, col=col) is not None:
            col += 1
        self.record_file.record_time(row=row, col=col, result=data)


if __name__ == '__main__':
    bb = Base()
    print(bb.a_HotelA, bb.a_HotelB, bb.b_HotelA, bb.b_HotelB)
    print(bb.b_startlet, bb.b_bmg)

