#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : JoannYang
# @Time   : 2020/3/10 15:34


aa = ([[{'addr': 'AH1R1L1', 'barcode': 'MGRK023026141887', 'pn': 'MGRK02', 'rack_id': 'MGRK017436485352'}],
       [{'addr': 'AH1R1L2', 'barcode': 'MGRK021325300285', 'pn': 'MGRK02', 'rack_id': 'MGRK017436485352'}],
       []])

for i in aa[:]:
    if i is None or i == []:
        continue
    elif i[0]['barcode'] == 'MGRK023026141887':
        aa.remove(i)

print(aa)
