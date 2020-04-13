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
                # "POS6":[None,None,None],"POS7":["BRMW01",None,None],"POS8":["BRMW01",None,None],"POS9":["BRMW01",None,None],"POS10":["BRMW01",None,None],
                # "POS11":[None,None,None],"POS12":["BRMW01",None,None],"POS13":["BRMW01",None,None],"POS14":["BRMW01",None,None],"POS15":["BRMW01",None,None],
                # "POS16":[None,None,None],"POS17":[None,None,None],"POS18":["DNDW01",None,None],"POS19":["DNDW01",None,None],"POS20":[None,None,"shake"],
                # "POS21":[None,None,None],"POS22":[None,None,None],"POS23":["DNDW01",None,None],"POS24":["DNDW01",None,None],"POS25":[None,None,None],
                # "POS26":["DNDW01",None,None],"POS27":["DNDW01",None,None],"POS28":["BRMW01",None,None],"POS29":["BRMW01",None,None],"POS30":[None,None,None],
                # "POS31":["DNDW01",None,None],"POS32":["DNDW01",None,None],"POS33":["BRMW01",None,None],"POS34":["BRMW01",None,None],"POS35":[None,None,"trash"],
                # "POS36":[None,None,None],"POS37":["DNDW01",None,None],"POS38":["DNDW01",None,None],"POS39":[None,None,None],"POS40":[None,None,None]}
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

# scans(['POS26', 'POS27', 'POS28', 'POS29'])
# export_barcodes()

scans(["POS1", "POS2", "POS3", "POS4", "POS5", "POS6", "POS7", "POS8"])
# scans_report(["POS2", "POS4", "POS5", "POS7", "POS8", "POS9", "POS26", "POS27"])






