# -*- coding: UTF-8 -*-

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
    "rcmd_register": "/zlims/resources/instance"
}

payload = '''
{
        "serial_number": "SZ13410_10-GENOMICS_3",
        "part_number": "MGISP-960",
        "metadata": {
            "instrument_status": "Idle",
            "control_software_version": "1.0.0",
            "location": "Shenzhen",
            "lab": "BGI SZ Auto Lab",
            "other metadata": ""
        }
}
'''

url = server["host"] + ":" + server["port"] + apis["rcmd_register"]
r = requests.post(url, data=payload, auth=(server["username"], server["password"]), headers=headers)
print(r.json())
if r.status_code == requests.codes.ok:
    print("device_register test pass!")
else:
    print("device_register test fail!")