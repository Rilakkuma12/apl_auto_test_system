"""堆栈库存管理"""
import json
import sys

import requests
from tools.handle_log import my_logger
from common.base import Base as us


class HotelManage:
    hotel_goods_ah = []
    hotel_goods_bh = []
    hotel_goods_ac = []
    hotel_goods_ah_backup, hotel_goods_bh_backup, hotel_goods_ac_backup = None, None, None

    def __init__(self):
        self.get_hotel_store()

    @staticmethod
    def query_hotel():
        """获取堆栈数据转换成dict格式"""
        return us.query_url("Dispatcher/QueryHotel")

    def get_hotel_store(self):
        """堆栈、冰箱库存转换及分类，分成A区堆栈、B区堆栈、A区冰箱"""
        data = self.query_hotel()

        for hotel in data['Content']:
            if hotel['Id'] == us.a_HotelA:
                prefix = 'AH1'
            elif hotel['Id'] == us.a_HotelB:
                prefix = 'AH2'
            elif hotel['Id'] == us.b_HotelA:
                prefix = 'BH1'
            elif hotel['Id'] == us.b_HotelB:
                prefix = 'BH2'
            elif hotel['Id'] == us.a_CytomatA:
                prefix = 'AC1'
            else:
                my_logger.error('Unknown hotel {}, func_name: {}'.format(hotel['Id'], sys._getframe().f_code.co_name))
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
                            self.hotel_goods_ah.append([{
                                'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']),
                                'barcode': consumable['Code'],
                                'pn': consumable['PN'],
                                'rack_id': rack_id}])
                        elif 'BH' in prefix:
                            self.hotel_goods_bh.append([{
                                'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']),
                                'barcode': consumable['Code'],
                                'pn': consumable['PN'],
                                'rack_id': rack_id}])
                        elif 'AC' in prefix:
                            self.hotel_goods_ac.append([{
                                'addr': '{}R{}L{}'.format(prefix, consumable['RackIndex'], consumable['Index']),
                                'barcode': consumable['Code'],
                                'pn': consumable['PN'],
                                'rack_id': rack_id}])
                except Exception as e:
                    my_logger.error(e)
        my_logger.debug('query hotel store, hotel ah:{}, hotel bh:{}'.format(self.hotel_goods_ah, self.hotel_goods_bh))
        self.hotel_goods_ah_backup, self.hotel_goods_bh_backup, self.hotel_goods_ac_backup = \
            self.hotel_goods_ah[:], self.hotel_goods_bh[:], self.hotel_goods_ac[:]
        return self.hotel_goods_ah, self.hotel_goods_bh, self.hotel_goods_ac

    @staticmethod
    def barcode_to_pn(barcode):
        """截取barcode前6位为PN"""
        return barcode[:6]

    def barcode_to_rack(self, barcode, is_pro_area, is_fridge):
        """查询barcode对应的rack id"""
        if is_pro_area:
            if is_fridge:
                target = [x for x in self.hotel_goods_ac_backup if x[0]['barcode'] == barcode]
            else:
                target = [x for x in self.hotel_goods_ah_backup if x[0]['barcode'] == barcode]
        else:
            target = [x for x in self.hotel_goods_bh_backup if x[0]['barcode'] == barcode]
        if len(target) == 0:
            my_logger.error(
                'barcode {} not in hotel list, func_name: {}'.format(barcode, sys._getframe().f_code.co_name))
        else:
            return target[0][0]['rack_id']

    def barcode_to_addr(self, barcode, is_pro_area, is_cytomat):
        """查询barcode对应的堆栈行列号，格式：'addr': 'AH1R1L2'"""
        if is_pro_area:
            if is_cytomat:
                target = [x for x in self.hotel_goods_ac_backup if x[0]['barcode'] == barcode]
            else:
                target = [x for x in self.hotel_goods_ah_backup if x[0]['barcode'] == barcode]
        else:
            target = [x for x in self.hotel_goods_bh_backup if x[0]['barcode'] == barcode]
        # target = [x for x in goods if x[0]['barcode'] == barcode]
        if len(target) == 0:
            my_logger.error(
                'barcode {} not in hotel list, func_name: {}'.format(barcode, sys._getframe().f_code.co_name))
        else:
            return target[0][0]['addr']

    def pn_to_barcodes(self, pn, is_pre_area, is_cytomat):
        """通过PN查找所有符合条件的barcode,不会扣库存"""
        barcodes = []

        if is_cytomat:
            target = [x for x in self.hotel_goods_ac if x[0]['barcode'][:6] == pn]
        elif is_pre_area:
            target = [x for x in self.hotel_goods_ah if x[0]['barcode'][:6] == pn]
        else:
            target = [x for x in self.hotel_goods_bh if x[0]['barcode'][:6] == pn]
        if len(target) == 0:
            my_logger.error('pn {} not in hotel list, func_name: {}'.format(pn, sys._getframe().f_code.co_name))
        else:
            for item in target:
                barcodes.append(item[0]['barcode'])
        return barcodes[0]

    def pn_to_barcode(self, pn, is_pre_area, is_cytomat):
        """通过PN查找符合条件的barcode,只返回一个，并扣减库存"""
        if is_cytomat:
            target = [x for x in self.hotel_goods_ac if x[0]['barcode'][:6] == pn]
            # 扣库存
            if target is None:
                my_logger.error('pn {} not in hotel list, func_name: {}'.format(pn, sys._getframe().f_code.co_name))
                return None
            self.hotel_goods_ac.remove(target[0])
            return target[0][0]['barcode']
        elif is_pre_area:
            target = [x for x in self.hotel_goods_ah if x[0]['barcode'][:6] == pn]
            if target is None:
                my_logger.error('pn {} not in hotel list, func_name: {}'.format(pn, sys._getframe().f_code.co_name))
                return None
            self.hotel_goods_ah.remove(target[0])
            return target[0][0]['barcode']
        else:
            target = [x for x in self.hotel_goods_bh if x[0]['barcode'][:6] == pn]
            if target is None:
                my_logger.error('pn {} not in hotel list, func_name: {}'.format(pn, sys._getframe().f_code.co_name))
                return None
            self.hotel_goods_bh.remove(target[0])
            return target[0][0]['barcode']



    @staticmethod
    def pn_to_rack(pn):
        """查找pn对应的所有可能堆栈rack类型"""
        try:
            for key in us.rack_to_pn.keys():
                if pn in us.rack_to_pn[key]:
                    return key
        except Exception as e:
            my_logger.error(e)

    @staticmethod
    def pn_to_rack_cytomat(pn):
        try:
            for key in us.rack_to_pn_cytomat.keys():
                if pn in us.rack_to_pn_cytomat[key]:
                    return key
        except Exception as e:
            my_logger.error(e)

    @staticmethod
    def rack_to_level_num(rack):
        try:
            return us.rack_to_level_num[rack]
        except Exception as e:
            my_logger.error(e)

    def tell_which_pos_can_push_more(self, pn, num, is_pro_area, is_cytomat):
        push_list_used = []
        n = 0
        hotel_goods = self.query_hotel()
        if is_cytomat:
            hotel_list = [us.a_CytomatA]
            rack_id = self.pn_to_rack_cytomat(pn)
        elif is_pro_area:
            hotel_list = [us.a_HotelA, us.a_HotelB]
            rack_id = self.pn_to_rack(pn)
        else:
            hotel_list = [us.b_HotelA, us.b_HotelB]
            rack_id = self.pn_to_rack(pn)
        # 获取到rack类型
        for i in range(len(hotel_goods['Content'])):
            hotel = hotel_goods['Content'][i]
            if hotel['Id'] not in hotel_list:
                continue
            for rack in hotel['Racks']:
                if rack['RackId'][:6] != rack_id:
                    # 模拟模式下注释，真实模式需要放开
                    my_logger.debug('hotel:{} searching rack to push, rack{} not match, to next.'.format(hotel['Name'],
                                                                                                         rack['Index']))
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


if __name__ == '__main__':
    my_store = HotelManage()
    # print(my_store.get_hotel_store())
    print(my_store.hotel_goods_ac)
    aa = my_store.pn_to_barcode(pn='MGRK01', is_pre_area=True, is_cytomat=False)
    print(aa)




