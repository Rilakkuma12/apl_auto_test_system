#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2019/9/23 16:36
import json
import time
from _datetime import datetime
from kafka import KafkaProducer, KafkaConsumer
from handle_config import config
from handle_log import my_logger
from common import base as us
import threading
from func_timeout import func_set_timeout, FunctionTimedOut

__topic_device = config.get_value('kafka', 'topic_device')
__topic_storage_lims = config.get_value('kafka', 'topic_storage_lims')
__topic_task_lims = config.get_value('kafka', 'topic_task_lims')
__topic_storage_apl = config.get_value('kafka', 'topic_storage_apl')
__topic_task_apl = config.get_value('kafka', 'topic_task_apl')
__KAFKA_SERVER = config.get_value('kafka', 'KAFKA_SERVER')
__TASK_ID = (datetime.now().isoformat()).replace(':', '-')
__SERVER_URL = config.get_value('swagger', 'server_url')

__topic_device_ = config.get_value('kafka', 'topic_device_')
__topic_storage_lims_ = config.get_value('kafka', 'topic_storage_lims_')
__topic_task_lims_ = config.get_value('kafka', 'topic_task_lims_')
__topic_storage_apl_ = config.get_value('kafka', 'topic_storage_apl_')
__topic_task_apl_ = config.get_value('kafka', 'topic_task_apl_')

producer = KafkaProducer(bootstrap_servers=[__KAFKA_SERVER], retries=3)
consumer_device = KafkaConsumer(__topic_device, bootstrap_servers=[__KAFKA_SERVER], auto_offset_reset='earliest')
consumer_storage_apl = KafkaConsumer(__topic_storage_apl, bootstrap_servers=[__KAFKA_SERVER], auto_offset_reset='earliest')
consumer_task_apl = KafkaConsumer(__topic_task_apl, bootstrap_servers=[__KAFKA_SERVER], auto_offset_reset='earliest')

msg_type = {
        'device': {
            'device_register': 'device_register',
            'device_heartbeat': 'device_heartbeat',
            'device_status': 'device_status',
            'device_alert': 'device_alert',
            'device_log': 'device_log',
            'robot_queue': 'robot_queue'
        },
        'task_lims': {
            'task_issue': 'task_issue',
            'run_response': 'run_response',
            'command': 'command',
            'control_command': 'control_command'
        },
        'task_apl': {
            'task_response': 'task_response',
            'run_request': 'run_request',
            'response': 'response',
            'control_response': 'control_response',
            'assist_complete': 'assist_complete',
            'putinplace': 'putinplace',
            'output': 'output',
            'complete': 'complete',
            'task_complete': 'task_complete'
                }}


def time_out(fn):
    def wrapper(*args, **kwargs):
        s_time = time.perf_counter()
        try:
            result = fn(*args, **kwargs)
            return result
        except FunctionTimedOut:
            e_time = time.perf_counter()
            my_logger.error(f'timeout! func name:{fn.__name__},takes:{e_time - s_time}')
            return TimeoutError
    return wrapper


class KafkaMsg:
    @staticmethod
    @time_out
    @func_set_timeout(2)
    def is_conform_to_task_msg(consumer=consumer_task_apl, msg_tp='response', comm_id=None, target_key='response', target_value=None):
        for msg in consumer:
            value = json.loads(msg.value.decode('utf-8'))
            if not isinstance(value, dict):
                value = json.loads(value)
            message_type = value['message_type']
            if message_type != msg_tp:
                continue
            content = value['message_content']
            if str(comm_id) in content['command_id'] and target_key in content.keys():
                if target_value in content[target_key]:
                    my_logger.info(f'hit!{msg.topic},{msg.partition}:{msg.offset},{value}')
                    return True
                else:
                    return False
            else:
                continue

    @staticmethod
    @time_out
    @func_set_timeout(10)
    def is_conform_to_device_log(consumer=consumer_device, msg_tp='device_log', comm_id=None, target_key='log_code', target_value=None):
        for msg in consumer:
            value = json.loads(msg.value.decode('utf-8'))
            if not isinstance(value, dict):
                value = json.loads(value)
            message_type = value['message_type']
            if message_type != msg_tp:
                continue
            content = value['message_content']
            if str(comm_id) in content['command_id'] and target_key in content.keys():
                if content[target_key] == target_value:
                    my_logger.info(f'hit!{msg.topic},{msg.partition}:{msg.offset},{value}')
                    return True
                else:
                    return False
            else:
                continue

    @staticmethod
    @time_out
    @func_set_timeout(5)
    def is_conform_to_storage_command_msg(consumer=consumer_storage_apl, msg_tp='device_response', comm_id=None,
                                          target_key='response', target_value=None):
        for msg in consumer:
            value = json.loads(msg.value.decode('utf-8'))
            if not isinstance(value, dict):
                value = json.loads(value)
            message_type = value['message_type']
            if message_type != msg_tp:
                continue
            content = value['message_content']
            if str(comm_id) in content['command_id'] and target_key in content.keys():
                if content[target_key] == target_value:
                    my_logger.info(f'hit!{msg.topic},{msg.partition}:{msg.offset},{value}')
                    return True
                else:
                    return False
            else:
                continue

    @staticmethod
    @time_out
    @func_set_timeout(10)
    def is_conform_to_storage_stock_msg(consumer=consumer_storage_apl, msg_tp='load_stock', dev_id=us.a_HotelA,
                                        target_key='storage'):
        for msg in consumer:
            value = json.loads(msg.value.decode('utf-8'))
            if not isinstance(value, dict):
                value = json.loads(value)
            message_type = value['message_type']
            if message_type != msg_tp:
                continue
            content = value['message_content']
            if dev_id in content['device_id'] and target_key in content.keys():
                if content[target_key] is not None:
                    my_logger.info(f'hit!{msg.topic},{msg.partition}:{msg.offset},{value}')
                    return True
                else:
                    return False
            else:
                continue

    @staticmethod
    @time_out
    @func_set_timeout(2)
    def demo(consumer=consumer_storage_apl):
        for msg in consumer:
            topic = msg.topic
            partition = msg.partition
            offset = msg.offset
            value = json.loads(msg.value.decode('utf-8'))
            if not isinstance(value, dict):
                value = json.loads(value)
            print(topic, partition, offset, value)

    @staticmethod
    @time_out
    @func_set_timeout(2)
    def is_conform_to_script_output(consumer=consumer_task_apl, msg_tp='output', comm_id=None, target_key='desc',
                                    target_value=None):
        for msg in consumer:
            value = json.loads(msg.value.decode('utf-8'))
            if not isinstance(value, dict):
                value = json.loads(value)
            message_type = value['message_type']
            if message_type != msg_tp:
                continue
            content = value['message_content']
            event = content['events'][0]
            if str(comm_id) in content['command_id'] and target_key in event.keys():
                if target_value in event[target_key]:
                    my_logger.info(f'hit!{msg.topic},{msg.partition}:{msg.offset},{value}')
                    return True
                else:
                    return False
            else:
                continue


km = KafkaMsg()


if __name__ == '__main__':
    # a = KafkaMsg().find_device_msg(consumer_device, msg_type['device']['robot_queue'], us.a_HotelA, 'message_content')
    # print(a)
    # b = KafkaMsg().is_conform_to_storage_command_msg(comm_id='c252eddc-e2a0-11e9-b0fe-484d7ec414ef', target_value='done')
    # print(b)
    # print(KafkaMsg.is_conform_to_storage_stock_msg())
    print(km.demo())

