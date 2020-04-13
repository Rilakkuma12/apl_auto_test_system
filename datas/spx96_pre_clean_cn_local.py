# -*- coding: utf-8 -*-
"""
***Spx head example***
wangjian5@genomics.cn
jjseen@163.com
"""
#region pos and kit type mapping table
#three write methods:empty-None; pcr-"pcr"; kit-"kit" ;cannot grasp/loose-"useless"  shake-([,"shake"])
# pos_type_map = {"POS1":None,"POS2":None,"POS3":None,"POS4":None,"POS5":None,"POS6":None,"POS7":None,"POS8":None,"POS9":None,"POS10":None,
                # "POS11":None,"POS12":None,"POS13":None,"POS14":None,"POS15":None,"POS16":None,
                # "POS17":None,"POS18":None,"POS19":None,"POS20":[None,"shake"],"POS21":None,
                # "POS22":None,"POS23":None,"POS24":None}
pos_type_map = {"POS1":[None,None,None],"POS2":["GETP01",None,None],"POS3":["GETP01",None,None],"POS4":["GETP01",None,None],"POS5":["GETP01",None,None],
                "POS6":[None,None,None],"POS7":["PN003",None,None],"POS8":["PN003",None,None],"POS9":["PN003",None,None],"POS10":["PN004",None,None],
                "POS11":[None,None,None],"POS12":["PN003",None,None],"POS13":["PN003",None,None],"POS14":["PN003",None,None],"POS15":["PN004",None,None],
                "POS16":[None,None,None],"POS17":[None,None,None],"POS18":["PN004",None,None],"POS19":["PN004",None,None],"POS20":[None,None,"shake"],
                "POS21":[None,None,None],"POS22":[None,None,None],"POS23":["PN004",None,None],"POS24":["PN004",None,None],"POS25":[None,None,None],
                "POS26":["MGRK02",None,None],"POS27":["PN003",None,None],"POS28":["PN003",None,None],"POS29":["PN003",None,None],"POS30":[None,None,None],
                "POS31":["PN003",None,None],"POS32":["PN003",None,None],"POS33":["PN003",None,None],"POS34":["PN003",None,None],"POS35":[None,None,"trash"],
                "POS36":[None,None,None],"POS37":["PN004",None,None],"POS38":["PN004",None,None],"POS39":[None,None,None],"POS40":[None,None,None]}

#region HEAD
spx96 = globals().get("Spx96")
# pos_type_map = spx96.PosMap
#simplest way 
from head import *
#init
init(spx96) #most important
binding_map(pos_type_map)

shake.binding(spx96)


"""
不要修改HEAD
"""

# home()
# pcr_open_door()
# mvkit('POS27','POS28') 
aspirate({'Module' : 'POS26', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (80), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS26', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
sleep(10)
# uvon()
# hoodon()
# lightoff()

# dely(900)

# hoodoff()

# dely(300)

# uvoff()
# lighton()
# unlock()









