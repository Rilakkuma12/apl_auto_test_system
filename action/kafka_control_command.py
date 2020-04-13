#encoding=utf-8
import uuid
from base import common as us
from base.common import logger
from datetime import datetime

__TASK_ID = (datetime.now().isoformat()).replace(':', '-')


def control_command(rst):
    # 0 暂停 1 恢复 2 停止
    command = ["pause", "resume", "stop"]
    command_id = uuid.uuid1()
    # rst = int(random()*3)
    comm = '''{
        "message_id": "UUID",
        "message_type": "control_command",
        "message_group": "task_lims",
        "message_content": {
            "task_id": "%s",
            "device_id": "%s",
            "command_id": "%s",
            "command": "%s",
            "parameters": {}
        }
    }
    ''' % (__TASK_ID, us.SP96XL, command_id, command[rst])
    return comm, command_id


if __name__ == "__main__":
    try:
        for i in range(1, 2):
            # 0 暂停 1 恢复 2 停止
            msg3, com_id3 = control_command(0)
            print('release, command id: {}'.format(com_id3))
            us.send(us.__topic_task_lims, msg3)
            # us.wait_command_complete(us.consumer_task_apl, us.__topic_task_apl, com_id3)
            # time.sleep(10)
    except Exception as e:
        logger().writelines(u'error: %s\n' % e.message)
    finally:
        logger().flush()
        logger().close()
