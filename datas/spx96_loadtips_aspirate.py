# -*- coding: utf-8 -*-
"""
***Spx head example***
wangjian5@genomics.cn
jjseen@163.com
"""

spx96 = globals().get("Spx96")
pos_type_map = spx96.PosMap
#simplest way 
from spredo import *
#init
init(spx96) #most important
binding_map(pos_type_map)

shake.binding(spx96)


"""
不要修改HEAD
"""

# load_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'Tips':96}) #①转移样品+beads1   1′45
# unload_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})
aspirate({'Module' : 'POS3', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (80), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS3', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})









