#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2019/8/21 10:31
import random
import os
from tools.constance import TASK_ID_FILE_PATH
random_num = ''.join(random.sample('0123456789', 3))


class HandleTaskId:
    file_path = TASK_ID_FILE_PATH

    def __init__(self):
        """先赋予个初始值100"""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                f.write('100')

    def read_task_id(self):
        with open(self.file_path, 'r') as f:
            return f.readline()

    def write_task_id(self, value):
        with open(self.file_path, 'w') as f:
            f.write(value)

    def get_task_id(self):
        try:
            task_id = self.read_task_id()
            task_id_new = int(task_id) + 1
            self.write_task_id(str(task_id_new))
        except ValueError:
            task_id = 100
        finally:
            return task_id


my_task_id = HandleTaskId()
if __name__ == '__main__':
    # my_task_id = HandleTaskId()
    print(my_task_id.get_task_id())
    # print(my_task_id.read_task_id())
    # my_task_id.write_task_id('101')

