import re
from tools.handle_mysql import HandleMysql
# one_str = '{"mobilephone": "${not_exited_tel}"}'
#
# # match从头开始找，一一匹配，匹配不上返回none
# # 匹配上返回match对象
# mtch = re.match(r'{"mobile', one_str)
# print(mtch.group())
#
# # search
# res = re.search(r'mobile', one_str)
# print(res.group())
#
# # sub替换
# haha = re.sub('\$\{not_exited_tel\}', '13829939393', one_str)
# print(haha)


class Context:
    not_existed_phone_pattern = r'\$\{not_existed_tel\}'
    existed_phone_pattern = r'\$\{existed_tel\}'
    investor_phone_pattern = r'\$\{investor_tel\}'

    def __init__(self):
        pass

    @classmethod
    def not_existed_phone_replace(cls, data):
        """
        替换未注册的手机号
        :return:
        """
        mysql = HandleMysql()
        if re.search(cls.not_existed_phone_pattern, data):
            new_phone = mysql.get_phone_unregister()
            data = re.sub(cls.not_existed_phone_pattern, new_phone, data)
        mysql.close()
        return data

    @classmethod
    def existed_phone_replace(cls, data):
        mysql = HandleMysql()
        if re.search(cls.existed_phone_pattern, data):
            existed_phone = mysql.get_phone_registered()
            data = re.sub(cls.existed_phone_pattern, existed_phone, data)
        mysql.close()
        return data

    @classmethod
    def investor_phone_replace(cls, data):
        mysql = HandleMysql()
        if re.search(cls.investor_phone_pattern, data):
            investor_phone = mysql.get_phone_investor()
            data = re.sub(cls.existed_phone_pattern, investor_phone, data)
        mysql.close()
        return data


if __name__ == '__main__':
    data1 = "{mobilephone': ‘${existed_tel}’, 'pwd': '123456', 'regname': 'lemon'}"
    data1 = Context.existed_phone_replace(data1)
    print(data1)
