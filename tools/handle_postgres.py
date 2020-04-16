#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/7/9 20:52
import psycopg2
from tools.handle_config import config
import random
from tools.handle_log import my_logger


class HandlePostgres:
    __instance = None

    def __new__(cls, *args, **kwargs):
        """单例模式"""
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self):
        self.conn = psycopg2.connect(
                host=config.get_value('postgres', 'host'),
                user=config.get_value('postgres', 'user'),
                password=config.get_value('postgres', 'password'),
                database=config.get_value('postgres', 'db'),
                port=config.get_int('postgres', 'port'),
            )
        self.cursor = self.conn.cursor()

    def run(self, sql, *args, is_more=False):
        self.cursor.execute(sql, vars=args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_device_id(self, area, device_name):
        """
        通过区域、设备名，查询返回设备id
        :param area: 
        :param device_name: 
        :return: 
        """
        sql = f"SELECT sn FROM public.apl_device WHERE area={area} and name like '{device_name}%%' order by last_online_time desc;"
        result = self.run(sql)
        if result:
            return result[0]
        else:
            # my_logger.error(f'query device id from db, find null, device_name:{device_name}, area:{area}')
            return None

    def get_rack_map_layer(self, pn):
        """查询料架对应的层数"""
        sql = f"select config_value from material_config  where material_id=(SELECT id FROM material where part_number='{pn}') and config_key='LevelCounts';"
        result = self.run(sql)
        if result:
            return int(result[0])
        else:
            my_logger.error(f'query layer of rack from db, find null, rack_pn:{pn}')
            return None


my_pg = HandlePostgres()
if __name__ == '__main__':
    print(my_pg.get_device_id(1, "HotelA"))
    print(my_pg.get_device_id(1, "MGISP-100"))
    a = my_pg.get_rack_map_layer('MGRK07')
    print(type(a))
    print(a)

