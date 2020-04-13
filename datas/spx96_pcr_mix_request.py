# -*- coding: utf-8 -*-
"""
***Spx head example***
wangjian5@genomics.cn
jjseen@163.com
"""

#region HEAD
spx96 = globals().get("Spx96")
pos_type_map = spx96.PosMap
#simplest way 
from spredo import *
#init
init(spx96) #most important

# binding_map(pos_type_map)
shake.binding(spx96)

binding_map(pos_type_map) 
report(phase = 'PCR-mix', step = 'PCR开始')

# pcr-mix之前向BGI-LIMS发送请求，直到BGI-LIMS返回True才执行下一步
# 注意事项：连接调度的时候不能单机跑此脚本，会报错，因为连接调度的时候需要task id绑定
request_pcr_mix()
report(phase = 'PCR-mix', step = 'PCR结束')
home()



