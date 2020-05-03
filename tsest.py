#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2020/3/10 15:34
#
# import sys
# # 这是一个获取函数名的装饰器
# def get_func_name(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print(f'执行函数名{func.__name__}')
#     return wrapper
#
#
# # @get_func_name
# def func():
#     print('执行函数')
#     fun_name = sys._getframe().f_code.co_name
#     print(fun_name)
#
#
# # print('函数名：{}'.format(func.__name__))
# func()
# aa = []
# bb = aa[:]
# aa = ['aaa', 'bbb', 'cccc']
#
#
# aa.remove('aaa')
# pass
# import json
#
# qq = '''{
#         "final_command": "False"
#         }'''
# aa = json.loads(qq)
# print(aa)

# aa = [[{'addr': 'BH1R1L2', 'barcode': 'MGRK025441140816', 'pn': 'MGRK02', 'rack_id': 'MGRK017720826447'}], ]
# bb = str(aa)
# if 'BH1R1L1' not in bb:
#     print('yes')

aa = 'AH1R14L7'

bb = aa[aa.index('R') + 1: aa.index('L')]
print(bb)
