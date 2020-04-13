#encoding=utf-8
from kafka import KafkaConsumer
from tools.handle_log import HandleLogger
from common import base as us

logger = HandleLogger(log_name='consumer_device', name='case_device')

# To consume latest messages and auto-commit offsets
consumer1 = KafkaConsumer(us.__topic_device, bootstrap_servers=['10.225.12.71:19092'])
consumer2 = KafkaConsumer(us.__topic_storage_apl, bootstrap_servers=['10.225.12.71:19092'])
consumer3 = KafkaConsumer(us.__topic_storage_lims, bootstrap_servers=['10.225.12.71:19092'])
consumer4 = KafkaConsumer(us.__topic_task_apl, bootstrap_servers=['10.225.12.71:19092'])
consumer5 = KafkaConsumer(us.__topic_task_lims, bootstrap_servers=['10.225.12.71:19092'])
consumers = [consumer1, consumer2, consumer3, consumer4, consumer5]


for message in consumer1:
    result = u"%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value.decode('utf-8'))
    logger.debug(result)

# for message in consumer2:
#     result = u"%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value.decode('utf-8'))
#     logger.debug(result)
#
# for message in consumer3:
#     result = u"%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value.decode('utf-8'))
#     logger.debug(result)
#
# for message in consumer4:
#     result = u"%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value.decode('utf-8'))
#     logger.debug(result)
#
# for message in consumer5:
#     result = u"%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value.decode('utf-8'))
#     logger.debug(result)
