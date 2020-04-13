#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/6/3 17:36
# 这个脚本用于存放通用函数，比如发送指令、查询任务完成等
import json
import uuid

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import os
from datetime import datetime
import datetime as dt
import socket
from handle_log import my_logger
from handle_config import config
import requests
import time
import copy
from handle_excel import HandleExcel
from constance import TIME_RECORD_PATH
from handle_postgres import my_pg

record_file = HandleExcel(TIME_RECORD_PATH)
__topic_device = config.get_value('kafka', 'topic_device')
__topic_storage_lims = config.get_value('kafka', 'topic_storage_lims')
__topic_task_lims = config.get_value('kafka', 'topic_task_lims')
__topic_storage_apl = config.get_value('kafka', 'topic_storage_apl')
topic_task_apl = config.get_value('kafka', 'topic_task_apl')
__KAFKA_SERVER = config.get_value('kafka', 'KAFKA_SERVER')
__TASK_ID = (datetime.now().isoformat()).replace(':', '-')
__SERVER_URL = config.get_value('swagger', 'server_url')

__topic_device_ = config.get_value('kafka', 'topic_device_')
__topic_storage_lims_ = config.get_value('kafka', 'topic_storage_lims_')
topic_task_lims_ = config.get_value('kafka', 'topic_task_lims_')
__topic_storage_apl_ = config.get_value('kafka', 'topic_storage_apl_')
__topic_task_apl_ = config.get_value('kafka', 'topic_task_apl_')

producer = KafkaProducer(bootstrap_servers=[__KAFKA_SERVER], retries=3)
consumer_device = KafkaConsumer(__topic_device, bootstrap_servers=[__KAFKA_SERVER])
consumer_storage_apl = KafkaConsumer(__topic_storage_apl, bootstrap_servers=[__KAFKA_SERVER])
consumer_task_apl = KafkaConsumer(topic_task_apl, bootstrap_servers=[__KAFKA_SERVER])

response_type = {__topic_storage_apl: 'device_response', topic_task_apl: 'complete'}

a_HotelA = my_pg.get_device_id(1, 'HotelA')
a_HotelB = my_pg.get_device_id(1, 'HotelB')
a_SP96XL1 = my_pg.get_device_id(1, 'MGISP-96XLEX')
# a_SP96XL2 = config.get_value('device id', 'a_SP96XL2')
# a_SP96XL3 = config.get_value('device id', 'a_SP96XL3')
a_interaction = my_pg.get_device_id(1, 'Interaction')
a_CytomatA =  my_pg.get_device_id(1, 'CytomatA')


b_SP96XL4 = my_pg.get_device_id(2, 'MGISP-96XLEX')
b_SP100 = my_pg.get_device_id(2, 'MGISP-100Plus')
b_HotelA = my_pg.get_device_id(2, 'HotelA')
b_HotelB = my_pg.get_device_id(2, 'HotelB')
b_interaction = my_pg.get_device_id(2, 'Interaction')
b_startlet = my_pg.get_device_id(2, 'B-STARlet-Simulated')
b_bmg = my_pg.get_device_id(2, 'B-BMG-Simulated')

var = ("hours", "minutes", "seconds")
time2sec = lambda x: int(dt.timedelta(**{k: int(v) for k, v in zip(var, x.strip().split(":"))}).total_seconds())
# MGRK02:7层，MGRK03:13层，MGRK04:18层，MGRK01、MGRK05、MGRK06:4层
__rack_to_pn = {
    'MGRK01': ('MGRK01', 'CRTP03', 'CRTF03'),  # Hamilton吸头（1mL）
    'MGRK02': ('MGRK02', 'GETP01', 'GETP02', 'GETF01', 'GETF02'),  # tips盒
    'MGRK03': ('MGRK03', 'DNDW01', 'BGBD01', 'BGBD02', 'BGBD03', 'BGBD04', 'BGBD05', 'BGTE01', 'BGTE02', 'BGTE03', 'BGET01', 'BGLE01', 'BGW101', 'BGW201'),  # 深孔板
    'MGRK04': ('MGRK04', 'BRMW01', 'BGMX01', 'BGMX02', 'BGMX03', 'BGMX04', 'BGBF01', 'BGBF02', 'BGBF03', 'BGEZ01', 'BGEZ02', 'BGPM01', 'BGBC01', 'EDUV01', 'MSMW01'),  # PCR板
    'MGRK05': ('MGRK05',),  # Hamilton吸头（50μL）
    'MGRK06': ('MGRK06', 'CRTP01', 'CRTP02', 'CRTF01', 'CRAF01', 'CRAF02', 'CRAF03', 'CRAP02')}  # Hamilton吸头（300μL）

__rack_to_pn_cytomat = {
    'TMRK01': ('DNDW01',),
    'TMRK02': ('BRMW01',)}

__rack_to_level_num = {
    'MGRK01': 4,  # Hamilton吸头（1mL）
    'MGRK02': 7,  # tips盒
    'MGRK03': 13,  # 深孔板
    'MGRK04': 18,  # PCR板
    'MGRK05': 4,  # Hamilton吸头（50μL）
    'MGRK06': 4  # Hamilton吸头（300μL）
}


def post(url, data=None):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json-patch+json'}
    return requests.post(url, data=json.dumps(data), headers=headers)


def on_send_success(args):
    my_logger.info('send success. offset: %s' % args.offset)


def on_send_error(err):
    my_logger.error('send err. offset: %s' % err.offset)


# 获取本机电脑名
my_name = socket.getfqdn(socket.gethostname())
# 获取本机ip
my_addr = socket.gethostbyname(my_name)


def send(topic, msg):
    global producer
    task_id = str(uuid.uuid1())
    try:
        r = producer.send(topic, msg.encode('ascii'), task_id.encode('ascii')).add_callback(on_send_success).add_errback(on_send_error)
        my_logger.debug(msg)
        return r.get(timeout=20)
    except KafkaError as e:
        print('KafkaError')
        my_logger.error(e)
        # logger().writelines(e.message + '\n')


def wait_command_complete(consumer, topic,  comm_id):
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
        if message_type != response_type[topic]:
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


def wait_task_complete(consumer, topic, comm_id):
    start = datetime.now()
    my_logger.info('waiting...')
    for msg in consumer:
        value = json.loads(msg.value.decode('utf-8'))
        if value is None:
            continue
        if not isinstance(value, dict):
            value = json.loads(value)
        message_type = value['message_type']
        if message_type != response_type[topic]:
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
            # 将耗时写入记录文件
            # write_to_record_file(processing_time)
            return False
        else:
            continue


def query_hotel():
    url = __SERVER_URL + "Dispatcher/QueryHotel"
    response = requests.post(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data


def query_hotel_by_id(hotel_id):
    goods = []
    url = __SERVER_URL + "Dispatcher/QueryHotel?hotelId=" + hotel_id
    response = requests.post(url)
    hotel = json.loads(response.content.decode('utf-8'))
    for rack in hotel['Content']['Racks']:
        rack_id = rack['RackId']
        for consumable in rack['Consumables']:
            goods.append([{'addr': '{}R{}L{}'.format(get_name(hotel_id), consumable['RackIndex'], consumable['Index']), 'barcode': consumable['Code'], 'pn': consumable['PN'], 'rack_id': rack_id}])

    return goods


def hotel_store():
    hotel_goods_ah = []
    hotel_goods_bh = []
    hotel_goods_ac = []
    url = __SERVER_URL + "Dispatcher/QueryHotel"
    response = requests.post(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        for hotel in data['Content']:
            if hotel['Id'] == a_HotelA:
                prefix = 'AH1'
            elif hotel['Id'] == a_HotelB:
                prefix = 'AH2'
            elif hotel['Id'] == b_HotelA:
                # continue
                prefix = 'BH1'
            elif hotel['Id'] == b_HotelB:
                prefix = 'BH2'
            elif hotel['Id'] == a_CytomatA:
                prefix = 'AC1'
            else:
                my_logger.error('Unknown hotel {}'.format(hotel['Id']))
                continue
            for rack in hotel['Racks']:
                if rack == 'null':
                    continue
                elif rack is None:
                    continue
                try:
                    rack_id = rack['RackId']
                    for consumable in rack['Consumables']:
                        if 'AH' in prefix:
                            hotel_goods_ah.append([{'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']), 'barcode': consumable['Code'], 'pn': consumable['PN'], 'rack_id': rack_id}])
                        elif 'BH' in prefix:
                            hotel_goods_bh.append([{'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']), 'barcode': consumable['Code'], 'pn': consumable['PN'], 'rack_id': rack_id}])
                        elif 'AC' in prefix:
                            hotel_goods_ac.append([{'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']), 'barcode': consumable['Code'], 'pn': consumable['PN'], 'rack_id': rack_id}])
                except Exception as e:
                    my_logger.error(e)
        my_logger.debug('query hotel store, hotel ah:{}, hotel bh:{}'.format(hotel_goods_ah, hotel_goods_bh))
        return hotel_goods_ah, hotel_goods_bh, hotel_goods_ac


def hotel_store_for_push():
    hotel_goods_ah = []
    hotel_goods_bh = []
    url = __SERVER_URL + "Query/QueryHotel"
    response = requests.post(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        for hotel in data:
            if hotel['Id'] == a_HotelA:
                prefix = 'AH1'
            elif hotel['Id'] == a_HotelB:
                prefix = 'AH2'
            elif hotel['Id'] == b_HotelA:
                prefix = 'BH1'
            elif hotel['Id'] == b_HotelB:
                prefix = 'BH2'
            else:
                my_logger.error('Unknown hotel {}'.format(hotel['Name']))
            for rack in hotel['Racks']:
                rack_id = rack['RackId']
                for consumable in rack['Consumables']:
                    if 'AH' in prefix:
                        hotel_goods_ah.append([{'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']), 'barcode': consumable['Code'], 'pn': consumable['PN'], 'rack_id': rack_id}])
                    else:
                        hotel_goods_bh.append([{'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']), 'barcode': consumable['Code'], 'pn': consumable['PN'], 'rack_id': rack_id}])
        my_logger.debug('query hotel store, hotel ah:{}, hotel bh:{}'.format(hotel_goods_ah, hotel_goods_bh))
        return hotel_goods_ah, hotel_goods_bh


def pn_to_barcodes(hotel_stores, pn, is_pre_area, is_cytomat):
    """
    还要区分前后区，如果目标设备在后区，则返回后区的barcode
    :param pn:
    :return:
    """
    hotel_goods_ah, hotel_goods_bh, hotel_goods_ac = hotel_stores
    barcodes = []

    if is_cytomat:
        target = [x for x in hotel_goods_ac if x[0]['barcode'][:6] == pn]
    elif is_pre_area:
        target = [x for x in hotel_goods_ah if x[0]['barcode'][:6] == pn]
    else:
        target = [x for x in hotel_goods_bh if x[0]['barcode'][:6] == pn]
    if len(target) == 0:
        my_logger.error('barcode {} not in hotel list'.format(pn))
    else:
        for item in target:
            barcodes.append(item[0]['barcode'])
    return barcodes


def barcode_to_pn(barcode):
    return barcode[:6]


def barcode_to_rack(barcode, is_pro_area, is_inter):
    hotel_goods_ah, hotel_goods_bh, hotel_goods_ai = hotel_store()
    if is_pro_area:
        if is_inter:
            target = [x for x in hotel_goods_ai if x[0]['barcode'] == barcode]
        else:
            target = [x for x in hotel_goods_ah if x[0]['barcode'] == barcode]
    else:
        target = [x for x in hotel_goods_bh if x[0]['barcode'] == barcode]
    if len(target) == 0:
        my_logger.error('barcode {} not in hotel list'.format(barcode))
    else:
        return target[0][0]['rack_id']


def barcode_to_addr(barcode, is_pro_area, is_cytomat):
    hotel_goods_ah, hotel_goods_bh, hotel_goods_ac = hotel_store()
    if is_pro_area:
        if is_cytomat:
            target = [x for x in hotel_goods_ac if x[0]['barcode'] == barcode]
        else:
            target = [x for x in hotel_goods_ah if x[0]['barcode'] == barcode]
    else:
        target = [x for x in hotel_goods_bh if x[0]['barcode'] == barcode]
    # target = [x for x in goods if x[0]['barcode'] == barcode]
    if len(target) == 0:
        my_logger.error('barcode {} not in hotel list'.format(barcode))
    else:
        return target[0][0]['addr']


def pos_to_barcode(device, pos):
    url = __SERVER_URL + 'Dispatcher/QueryBoards'
    response = requests.post(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        if not data:
            my_logger.error('get boards info null')
        my_pos = int(pos[3:])
        is_existed = False
        for item in data['Content'][device]:
            if item['Position'] == my_pos:
                is_existed = True
                return item['BarCode']
        if not is_existed:
            my_logger.error(f'{pos} is null')


def pn_to_rack(pn):
    try:
        for key in __rack_to_pn.keys():
            if pn in __rack_to_pn[key]:
                return key
    except Exception as e:
        my_logger.error(e)


def pn_to_rack_cytomat(pn):
    try:
        for key in __rack_to_pn_cytomat.keys():
            if pn in __rack_to_pn_cytomat[key]:
                return key
    except Exception as e:
        my_logger.error(e)


def rack_to_level_num(rack):
    try:
        return __rack_to_level_num[rack]
    except Exception as e:
        my_logger.error(e)


def tell_which_pos_can_push(pn, is_pro_area):
    """
    1.根据pn找到Rack号
    2.判断该Rack里面是否有空位置
    3.确定空位置
    :param pn: 物料pn
    :param is_pro_area: true前区 false后区
    :return:
    """
    hotel_goods = query_hotel()
    if is_pro_area:
        hotel_list = [a_HotelA, a_HotelB]
    else:
        hotel_list = [b_HotelA, b_HotelB]
    # 获取到rack类型
    rack_id = pn_to_rack(pn)
    for i in range(len(hotel_goods)):
        hotel = hotel_goods[i]
        if hotel['Id'] not in hotel_list:
            continue
        for rack in hotel['Racks']:
            if rack['RackId'][:6] != rack_id:
                my_logger.debug('hotel:{} searching rack to push, rack{} not match, to next.'.format(hotel['Name'], rack['Index']))
                continue
            elif len(rack['Consumables']) >= rack_to_level_num(rack_id):
                my_logger.debug('{}, rack{} is full, to next.'.format(hotel['Name'], rack['Index']))
                continue
            else:
                my_logger.debug('{}, rack{} is not full, can push.'.format(hotel['Name'], rack['Index']))
                level_num = rack_to_level_num(rack_id)
                # j代表level数
                for j in range(1, level_num + 1):
                    can_not_push = []
                    rack_idx = 1
                    for level in rack['Consumables']:
                        rack_idx = level['RackIndex']
                        if j == level['Index']:
                            can_not_push.append(level['Index'])
                    if j not in can_not_push:
                        # 如果i已经使用过了就下一个
                        return hotel['Name'], hotel['Id'], rack_idx, j, rack['RackId']  # rack['Consumables']['RackIndex']
                        # yield hotel['Name'], hotel['Id'], rack_idx, j, rack['RackId']  # rack['Consumables']['RackIndex']
                    else:
                        continue


def tell_which_pos_can_push_more(pn, num, is_pro_area, is_cytomat):
    push_list_used = []
    n = 0
    hotel_goods = query_hotel()
    if is_cytomat:
        hotel_list = [a_CytomatA]
        rack_id = pn_to_rack_cytomat(pn)
    elif is_pro_area:
        hotel_list = [a_HotelA, a_HotelB]
        rack_id = pn_to_rack(pn)
    else:
        hotel_list = [b_HotelA, b_HotelB]
        rack_id = pn_to_rack(pn)
    # 获取到rack类型
    for i in range(len(hotel_goods['Content'])):
        hotel = hotel_goods['Content'][i]
        if hotel['Id'] not in hotel_list:
            continue
        for rack in hotel['Racks']:
            if rack['RackId'][:6] != rack_id:
                # 模拟模式下注释，真实模式需要放开
                my_logger.debug('hotel:{} searching rack to push, rack{} not match, to next.'.format(hotel['Name'], rack['Index']))
                continue
            # if len(rack['Consumables']) >= rack_to_level_num(rack_id):
            elif len(rack['Consumables']) >= rack['Count']:
                my_logger.debug('{}, rack{} is full, to next.'.format(hotel['Name'], rack['Index']))
                continue
            else:
                my_logger.debug('{}, rack{} is not full, can push.'.format(hotel['Name'], rack['Index']))
                level_num = rack['Count']
                # j代表level数
                for j in range(1, level_num + 1):
                    can_not_push = []
                    rack_idx = rack['Index']
                    for level in rack['Consumables']:
                        rack_idx = level['RackIndex']
                        if j == level['Index']:
                            can_not_push.append(level['Index'])
                    if j not in can_not_push:
                        # 如果i已经使用过了就下一个
                        push_list_used.append({'hotel_name': hotel['Name'],
                                               'hotel_id': hotel['Id'],
                                               'rack_idx': rack_idx,
                                               'level': j,
                                               'rack_id': rack['RackId']})
                        n += 1
                        if n < num:
                            continue
                        else:
                            return push_list_used
                    else:
                        continue


def tell_which_pos_can_push_only_simulate(pn, num, is_pro_area, is_inter):
    push_list_used = []
    n = 0
    hotel_goods = query_hotel()
    if is_inter:
        hotel_list = [a_interaction]
    elif is_pro_area:
        hotel_list = [a_HotelA, a_HotelB]
    else:
        hotel_list = [b_HotelA, b_HotelB]
    # 获取到rack类型
    rack_id = pn_to_rack(pn)
    for i in range(len(hotel_goods['Content'])):
        hotel = hotel_goods['Content'][i]
        if hotel['Id'] not in hotel_list:
            continue
        for rack in hotel['Racks']:
            if len(rack['Consumables']) >= rack['Count']:
                my_logger.debug('{}, rack{} is full, to next.'.format(hotel['Name'], rack['Index']))
                continue
            else:
                my_logger.debug('{}, rack{} is not full, can push.'.format(hotel['Name'], rack['Index']))
                # level_num = rack_to_level_num(rack_id)
                # j代表level数
                for j in range(1, rack['Count'] + 1):
                    can_not_push = []
                    rack_idx = 1
                    for level in rack['Consumables']:
                        rack_idx = level['RackIndex']
                        if j == level['Index']:
                            can_not_push.append(level['Index'])
                    if j not in can_not_push:
                        # 如果i已经使用过了就下一个
                        push_list_used.append({'hotel_name': hotel['Name'],
                                               'hotel_id': hotel['Id'],
                                               'rack_idx': rack_idx,
                                               'level': j,
                                               'rack_id': rack['RackId']})
                        n += 1
                        if n < num:
                            continue
                        else:
                            return push_list_used
                    else:
                        continue


def get_name(arg):
    gl = globals().copy()
    for i in gl:
        if gl[i] is arg:
            return i


def get_pcr_mix_request_info():
    my_logger.info('getting pcr_mix request...')
    for msg in consumer_task_apl:
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


def get_robot_request_exception_info():
    my_logger.info('getting robot exception request...')
    for msg in consumer_task_apl:
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


def get_inter_request_info():
    my_logger.info('getting interaction request...')
    for msg in consumer_task_apl:
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


def ack_task(task_id):
    api = __SERVER_URL + "Query/QueryTask?taskid=" + task_id
    return post(api)


def wait_task_complete_api(task_id):
    resp = ack_task(task_id)
    while resp.text != 'true':
        resp = ack_task(task_id)
        time.sleep(1)


def write_to_record_file(data):
    # 将耗时写入记录文件
    try:
        row = getattr(HandleExcel, 'current_row')
    except Exception as e:
        my_logger.debug("err: {}".format(e))
        row = 2
    col = 1
    while record_file.get_cell_value(row=row, col=col) is not None:
        col += 1
    record_file.record_time(row=row, col=col, result=data)


if __name__ == '__main__':
    # send(consumer_storage_apl, msg="haha")
    # a = query_hotel_by_id(a_HotelA)
    # print(a)
    # print(get_name(a_HotelA))
    # print(pn_to_barcodes(a_HotelA, 'MGRK01', is_pro_area=True, is_inter=False))
    # print(pos_to_barcode(a_SP96XL1, 'POS2'))
    # print(tell_which_pos_can_push_only_simulate('MGRK01', 2, is_pro_area=True, is_inter=False))
    # print(hotel_store())
    a = hotel_store()
    print(a)
    print(type(a))
