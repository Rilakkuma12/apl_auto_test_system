#encoding=utf-8
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from datetime import datetime
from time import sleep
from random import random
import base64
import io
import os

__topic = 'apl-webs'
__KAFKA_SERVER = '10.225.12.71:9092'
# __GROUP_ID = 'Python-client'
__log = open(os.path.abspath(('./logs/%s.log' % datetime.now().isoformat()).replace(':', '-')), mode='wt')
# __log = open(os.path.abspath(('./%s.log'%datetime.now().isoformat()).replace(':', '-')), mode='wt')

producer = KafkaProducer(bootstrap_servers=['10.225.12.71:9092'], retries=3)


def logger():
    global __log
    return __log


def on_send_success(args):
    logger().writelines('send success. offset: %s' % args.offset)


def on_send_error(err):
    logger().writelines('send err. offset: %s' % err.offset)


def device_operation(rst):
    # 测试设备操作，包括物料装载、存入物料、取出物料，是否少了从起始点送到目标点？是否撕膜、封膜、离心
    operation = ['load_stock', 'stock_in', 'stock_out']
    # rst = int(random()*3)
    comm = '''{
        "message_id": "UUID",
        "message_type": "%s",
        "message_group": "storage",
        "message_content": {
            "module_id": "7",
            "device_type": "Spx960",
            "device_id": "device000000SPX",
            "storage": [
                {
                    "rack": "numeric",
                    "slot": "",
                    "spec": "",
                    "barcode": ""
                }
            ]
        }
    }
    ''' % operation[rst]
    return comm


def send(msg):
    global producer, __topic
    try:
        logger().writelines([msg, '\n'])
        r = producer.send(__topic, msg.encode('ascii')).add_callback(on_send_success).add_errback(on_send_error)
        return r.get(timeout=20)
    except KafkaError as e:
        logger().writelines(e.message + '\n')


if __name__ == "__main__":
    try:
        for i in range(1, 2):
            send(device_operation(0))
    except Exception as e:
        logger().writelines(u'error: %s\n' % e.message)
    finally:
        logger().flush()
        logger().close()
