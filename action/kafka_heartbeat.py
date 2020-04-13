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

__topic = 'device'
__KAFKA_SERVER = '10.225.12.71'
# __GROUP_ID = 'Python-client'
__log = open(os.path.abspath(('./%s.log' % datetime.now().isoformat()).replace(':', '-')), mode='wt')
# __log = open(os.path.abspath(('./%s.log'%datetime.now().isoformat()).replace(':', '-')), mode='wt')

producer = KafkaProducer(bootstrap_servers=['10.225.12.71'], retries=3)


def logger():
    global __log
    return __log


def on_send_success(args):
    logger().writelines('send success. offset: %s' % args.offset)


def on_send_error(err):
    logger().writelines('send err. offset: %s' % err.offset)


def heartbeat():
    status = ['idle', 'running', 'pause', 'resume']
    rst = int(random()*4)
    hb = '''{
        "message_id": "UUID",
        "message_type": "device_heartbeat",
        "message_group": "device",
        "message_content": {
            "module_id": "7",
            "device_type": "MGISP-96XL",
            "device_id": "SZ13410_10-GENOMICS",
            "status": "%s",
            "status_time": ""
        }
    }
    ''' % status[rst]
    return hb


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
        for i in range(1, 100):
            send(heartbeat())
    except Exception as e:
        logger().writelines(u'error: %s\n' % e.message)
    finally:
        logger().flush()
        logger().close()
