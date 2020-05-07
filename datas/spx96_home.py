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

#*************离线添加头部（离线请添加以下指令覆盖映射表）***********
# pos_type_map = {"POS1":["PN006",None,None],"POS2":["PN006",None,None],"POS3":["PN006",None,None],"POS4":["PN006",None,None],
                # "POS5":["PN006",None,None],"POS6":["PN006",None,None],"POS7":["PN006",None,None],"POS8":["PN006",None,None],
                # "POS9":["PN006",None,None],"POS10":[None,None,None],"POS11":["PN001","PN005",None],"POS12":["PN001",None,None],
                # "POS13":[None,None,None],"POS14":["PN001",None,None],"POS15":["PN001",None,None],"POS16":[None,None,None],
                # "POS17":["PN004",None,None],"POS18":["PN004",None,None],"POS19":[None,None,None],"POS20":["PN004",None,"shake"],
                # "POS21":["PN004",None,None],"POS22":["PN004",None,None],"POS23":["PN004",None,None],"POS24":[None,None,"trash"]}
binding_map(pos_type_map) 
report(phase = '这是个普通的home脚本', step = '脚本开始')

home()

dely(5)

for i in range(10):
    report(phase = '这是个普通的home脚本{}'.format(i), step = '脚本结束')
    dely(5)

home()


