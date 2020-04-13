#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Tikyo
# @Time   : 2019/7/8 19:29
import requests
import json


class HttpRequests:
    def __init__(self):
        self.one_session = requests.Session()

    def to_request(self, method, url, data=None, is_json=False, **kwargs):
        method = method.upper()
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                print('异常为{}'.format(e))
                data = eval(data)
        if method == 'GET':
            res = self.one_session.request(method=method, url=url, params=data, **kwargs)
        elif method == 'POST':
            if is_json:
                res = self.one_session.request(method=method, url=url, json=data, **kwargs)
            else:
                res = self.one_session.request(method=method, url=url, data=data, **kwargs)
        else:
            res = None
            print('未定义的方法')
        return res

    def close(self):
        self.one_session.close()


do_request = HttpRequests()
if __name__ == '__main__':
    url0 = 'http://tj.lemonban.com/futureloan/mvc/api/member/login'
    url1 = 'http://tj.lemonban.com/futureloan/mvc/api/member/recharge'
    data0 = {'mobilephone': '15587898767',
             'pwd': '123456'}
    data1 = {'mobilephone': '15587898767',
             'amount': '123456'}
    do_request.to_request('post', url0, data0)
    resp = do_request.to_request('post', url1, data1)
    print(resp.text)
    print(type(resp.text))

