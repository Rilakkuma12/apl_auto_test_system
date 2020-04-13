#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import random
import time
from tools.handle_log import my_logger
from tools.handle_config import config
from base import common as us

__SERVER_URL = config.get_value('swagger', 'server_url')

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
inputs = []
__swagger_inputs = '''
    {
        "BarCode": "%s",
        "SourceDeviceId": "%s",
        "SourcePosition": %d,
        "SourceRackIndex": %d,
        "SourceIndex": %d,
        "TargetDeviceId": "%s",
        "TargetPosition": %d,
        "TargetRackIndex": %d,
        "TargetIndex": %d,
        "IsPeel": %s,
        "IsPlateLoc": %s,
        "IsCentrifugal": %s
    }
'''


def query_hotel():
    api = __SERVER_URL + "Query/QueryHotel"
    return post(api)


def open_door(dst_id):
    api = __SERVER_URL + "Dispatcher/OpenDoor?taskid=" + new_task_id() + "&targetDeviceId=" + dst_id
    return post(api)


def close_door(dst_id):
    api = __SERVER_URL + "Dispatcher/CloseDoor?taskid=" + new_task_id() + "&targetDeviceId=" + dst_id
    return post(api)


def release_after_scan(dst_id):
    api = __SERVER_URL + "Dispatcher/ReleaseAfterScan?taskid=" + new_task_id() + "&targetDeviceId=" + dst_id
    return post(api)


def load_consumables_all(dest, is_pro_area=True, weight='5', sealing='false', tearing='false', centrifuge='false', **kwargs):
    if is_pro_area:
        area_type = 'FirstArea'
    else:
        area_type = 'LastArea'
    api = __SERVER_URL + "DispatcherQuene/Transfer?taskid=" + new_task_id() + "&areaType=" + area_type + "&weight=" + weight
    print(__task_id)
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
            swagger_inputs = __swagger_inputs % (barcode, hotel_id, 0, int(rack_idx), int(level_idx), dest, int(pos[3:]),
                                                 0, 0, sealing, tearing, centrifuge)
            swagger_inputs = json.loads(swagger_inputs)
            inputs.append(swagger_inputs)
            my_logger.info(api)
            my_logger.info(inputs)
    return post(api, inputs)


def post(url, data=None):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json-patch+json'}
    return requests.post(url, data=json.dumps(data), headers=headers)


__task_id = None


def new_task_id():
    global __task_id
    __task_id = str(random.randint(1, 9999999))
    return __task_id


# def new_task_id1():
# taskid = str(random.randint(1, 9999999))
# return taskid

def query_task(taskid):
    api = __SERVER_URL + "Query/QueryTask?taskid=" + taskid
    return post(api)


def retry(taskid):
    resp = query_task(taskid)
    while (resp.content != 'true'):
        resp = query_task(taskid)
        # print("query_task :"+taskid+"  result:"+ resp.content)
        time.sleep(1)


if __name__ == '__main__':
    load_consumables_all(us.a_SP96XL1, is_pro_area=True, load={'MGRK01': ('POS7', 'POS8')})
