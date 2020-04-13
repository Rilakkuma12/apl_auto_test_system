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
# pos_type_map = {"POS1":[None,None,None],"POS2":[None,None,None],"POS3":["useless",None,None],"POS4":["useless",None,None],"POS5":["useless",None,None],
                # "POS6":[None,None,None],"POS7":["PCRMST96DM",None,None],"POS8":["PCRMST96DM",None,None],"POS9":["PCRMST96DM",None,None],"POS10":["PCRMST96DM",None,None],
                # "POS11":[None,None,None],"POS12":["PCRMST96DM",None,None],"POS13":["PCRMST96DM",None,None],"POS14":["PCRMST96DM",None,None],"POS15":["PCRMST96DM",None,None],
                # "POS16":[None,None,None],"POS17":[None,None,None],"POS18":["DeepwellPlateDT7350504",None,None],"POS19":["DeepwellPlateDT7350504",None,None],"POS20":[None,None,"shake"],
                # "POS21":[None,None,None],"POS22":[None,None,None],"POS23":["DeepwellPlateDT7350504",None,None],"POS24":["DeepwellPlateDT7350504",None,None],"POS25":[None,None,None],
                # "POS26":["PCRMST96DM",None,None],"POS27":["PCRMST96DM",None,None],"POS28":["PCRMST96DM",None,None],"POS29":["PCRMST96DM",None,None],"POS30":[None,None,None],
                # "POS31":["PCRMST96DM",None,None],"POS32":["PCRMST96DM",None,None],"POS33":["PCRMST96DM",None,None],"POS34":["PCRMST96DM",None,None],"POS35":[None,None,"trash"],
                # "POS36":[None,None,None],"POS37":["DeepwellPlateDT7350504",None,None],"POS38":["DeepwellPlateDT7350504",None,None],"POS39":[None,None,None],"POS40":[None,None,None]}

#region HEAD
spx96 = globals().get("Spx96")
pos_type_map = spx96.PosMap
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
aspirate({'Module' : 'POS27', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (80), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS27', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
# uvon()
# hoodon()
# lightoff()

# dely(900)

# hoodoff()

# dely(300)

# uvoff()
# lighton()
# unlock()









