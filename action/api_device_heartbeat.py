# -*- coding: UTF-8

import requests
import json
# import urllib.parse
import base64

server = {
    "host": "http://zlims-isw-01.genomics.cn",
    "port": "8000",
    "username": "zlims_be",
    "password": "zlims_be"
}

headers = {'content-type': 'application/json'}

apis = {
    "version": "/zlims/utils/version",
    "rcmd_heartbeat": "/zlims/heartbeat/submit"
}

payload = '''
{
    "part_number": "MGISP-960",
    "serial_number": "SZ13410_10-GENOMICS",
    "inputs": {
        "instrument_status": "running",
        "disk": {
            "total": "10G",
            "used": "1G"
        },
        "temperature": {
            "motor_temperature": "90",
            "motherboard_temperature": "40",
            "liquor_temperature": "10"
        }
    }
}
'''

url = server["host"] + ":" + server["port"] + apis["rcmd_heartbeat"]
r = requests.post(url, data=payload, auth=(server["username"], server["password"]), headers=headers)
print(r.json())
# # print(r)
if r.status_code == requests.codes.ok:
    print("device_heartbeat test pass!")
else:
    print("device_heartbeat test fail!")
