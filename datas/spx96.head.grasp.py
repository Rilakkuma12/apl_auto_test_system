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

binding_map(pos_type_map)
shake.binding(spx96)

#*************离线添加头部（离线请添加以下指令覆盖映射表）***********
pos_type_map = {"POS1":["PN006",None,None],"POS2":["PN006",None,None],"POS3":["PN006",None,None],"POS4":["PN006",None,None],
                "POS5":["PN006",None,None],"POS6":["PN006",None,None],"POS7":["PN006",None,None],"POS8":["PN006",None,None],
                "POS9":["PN006",None,None],"POS10":[None,None,None],"POS11":["PN001","PN005",None],"POS12":["PN001",None,None],
                "POS13":[None,None,None],"POS14":["PN001",None,None],"POS15":["PN001",None,None],"POS16":[None,None,None],
                "POS17":["PN004",None,None],"POS18":["PN004",None,None],"POS19":[None,None,None],"POS20":["PN004",None,"shake"],
                "POS21":["PN004",None,None],"POS22":["PN004",None,None],"POS23":["PN004",None,None],"POS24":["trash",None,None]}
binding_map(pos_type_map) 

c1_in()



#与之前版本一样的写法，但表示搬移单个物体，从上而下搬（即如果有盖子，则搬移盖子）

#新洗法，表示搬移所有的东西，放置处已在内部做了校验是否可以放下
# mvkit("POS11","POS16",True)
# mvkit("POS16","POS11",True)

#mvkit("POS15","POS13")
#mvkit("POS15","POS14")
##脚本写法与以前一样，并且结果一样
#mvkit("POS13","POS14")
#mvkit("POS14","POS15")
#mvkit("POS15","POS16")
#mvkit("POS16","POS13")
#
#jc("POS11")
#jc("POS12","POS24")
#
#jc(["POS20","POS18"])
#jc(["POS22","POS23"],"POS24")