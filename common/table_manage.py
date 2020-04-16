"""台面库存管理"""
import json
import sys

import requests
from tools.handle_log import my_logger
from common.base import Base as us


class TableManage:
    def pos_to_barcode(self, device, pos):
        data = us.query_url('Dispatcher/QueryBoards')
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

