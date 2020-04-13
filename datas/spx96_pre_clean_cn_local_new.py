# -*- coding: utf-8 -*-
"""
***Spx head example***
wangjian5@genomics.cn
jjseen@163.com
"""
# pos_type_map = {"POS1":[None,None,None],"POS2":["GETP01",None,None],"POS3":["GETP01",None,None],"POS4":["GETP01",None,None],"POS5":["GETP01",None,None],
                # "POS6":[None,None,None],"POS7":["PN003",None,None],"POS8":["PN003",None,None],"POS9":["PN003",None,None],"POS10":["PN004",None,None],
                # "POS11":[None,None,None],"POS12":["PN003",None,None],"POS13":["PN003",None,None],"POS14":["PN003",None,None],"POS15":["PN004",None,None],
                # "POS16":[None,None,None],"POS17":[None,None,None],"POS18":["PN004",None,None],"POS19":["PN004",None,None],"POS20":[None,None,"shake"],
                # "POS21":[None,None,None],"POS22":[None,None,None],"POS23":["PN004",None,None],"POS24":["PN004",None,None],"POS25":[None,None,None],
                # "POS26":["MGRK02",None,None],"POS27":["PN003",None,None],"POS28":["PN003",None,None],"POS29":["PN003",None,None],"POS30":[None,None,None],
                # "POS31":["PN003",None,None],"POS32":["PN003",None,None],"POS33":["PN003",None,None],"POS34":["PN003",None,None],"POS35":[None,None,"trash"],
                # "POS36":[None,None,None],"POS37":["PN004",None,None],"POS38":["PN004",None,None],"POS39":[None,None,None],"POS40":[None,None,None]}
#region HEAD
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
home()

scans_report(["POS2","POS4","POS5","POS6","POS7","POS8","POS9"])

report(phase = '接头连接', step = 'PCR与温控实验前准备')

# load_tips({'Module':'POS2','Col':1,'Row':1,'Tips':96})



def blockA(): 
    a_pcr_close_door()
    a_pcr_open_door()
    a_pcr_run_methods(method = 'START')
    a_pcr_run_methods(method = '25-4')
    
    
a = parallel_block(blockA) #PCRA已经开始...正在执行

c1_in() # 穿刺抓手进去

a.Wait()

report(phase = '接头连接', step = 'PCR A加连接mix和barcode')

load_tips({'Module':'POS2','Col':1,'Row':1,'Tips':96})

# aspirate({'Module' : 'POS12', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (80), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':10,'DelySeconds':0.5})
# empty({'Module' : 'POS12', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})

unload_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '接头连接', step = 'PCR A连接反应开始')


def blockD(): 
    a_pcr_close_door()
    
    
d = parallel_block(blockD) #PCRA已经开始连接反应...正在执行
d.Wait()

c1_out()

home()




