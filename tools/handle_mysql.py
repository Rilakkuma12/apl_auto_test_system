#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/7/9 20:52
import pymysql
from tools.handle_config import config
import random
from tools.handle_log import my_logger


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(
                host=config.get_value('sql', 'host'),
                user=config.get_value('sql', 'user'),
                password=config.get_value('sql', 'password'),
                db=config.get_value('sql', 'db'),
                port=config.get_int('sql', 'port'),
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
        self.cursor = self.conn.cursor()

    def run(self, sql, *args, is_more=False):
        self.cursor.execute(sql, args=args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def get_random_phone():
        """
        随机生成一个手机号码
        :return:
        """
        prefix = ['189', '155', '138', '188']
        num = random.sample('0123456789', 8)
        str_num = ''.join(num)
        return prefix[random.randint(0, 3)] + str_num

    def is_existed_phone(self, phone):
        """
        判断电话号码是否已存在
        :return: true/false
        """
        sql = 'SELECT MobilePhone FROM member WHERE MobilePhone = %s;'
        if self.run(sql, phone):
            return True
        else:
            return False

    def get_phone_unregister(self):
        """
        获取一个未注册过的手机号：
        1、生成一个随机电话号码；
        2、去数据库查一下此手机是否存在，若存在重复1步骤，若不存在，返回手机号码。
        """
        phone = self.get_random_phone()
        while self.is_existed_phone(phone):
            phone = self.get_random_phone()
        return phone

    def get_member_info(self, name):
        sql = 'SELECT Id, RegName, MobilePhone, Pwd FROM member WHERE RegName = %s;'
        return self.run(sql, name)

    def get_phone_registered(self):
        """
        获取一个已经注册的手机号：从数据库中直接获取
        :return:
        """
        sql = 'SELECT MobilePhone FROM member LIMIT 0, 1;'
        return self.run(sql)['MobilePhone']

    def get_phone_investor(self):
        sql = 'SELECT MobilePhone FROM member WHERE RegName = %s;'
        return self.run(sql, 'investor')['MobilePhone']


mysql = HandleMysql()
if __name__ == '__main__':
    # print(HandleMysql.get_random_phone())
    # print(mysql.is_existed_in_mysql('18330372028'))
    # print(mysql.get_phone_unregister())
    print(mysql.get_member_info('test_lemon_9253'))
    print(mysql.get_phone_investor())
