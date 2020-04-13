#encoding=utf-8
import kafka

from kafka import KafkaConsumer
import datetime
import io

log = io.open('consume.log', mode='wt', encoding='utf-8')

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('task_lims_1',
                         #group_id='my-group',
                         bootstrap_servers=['10.225.12.71:19092'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    result = u"%s %s:%d:%d: key=%s value=%s\n" %(datetime.datetime.now(), message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value.decode('utf-8'))
    log.write(result)
    log.flush()

# consume earliest available messages, don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# consume json messages
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

# consume msgpack
KafkaConsumer(value_deserializer=msgpack.unpackb)

# StopIteration if no message after 1sec
KafkaConsumer(consumer_timeout_ms=1000)

# Subscribe to a regex topic pattern
consumer = KafkaConsumer()
consumer.subscribe(pattern='^awesome.*')

# Use multiple consumers in parallel w/ 0.9 kafka brokers
# typically you would run each on a different server / process / CPU
consumer1 = KafkaConsumer('my-topic',
                          group_id='my-group',
                          bootstrap_servers='my.server.com')
consumer2 = KafkaConsumer('my-topic',
                          group_id='my-group',
                          bootstrap_servers='my.server.com')