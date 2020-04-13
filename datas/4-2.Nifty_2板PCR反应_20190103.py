# -*- coding: utf-8 -*-
"""
***Spx head example***
wangjian5@genomics.cn
jjseen@163.com
"""
#region pos and kit type mapping table
#three write methods:empty-None; pcr-"pcr"; kit-"kit" ;cannot grasp/loose-"useless"  shake-([,"shake"])
pos_type_map = {"POS1":["useless",None,None],"POS2":["useless",None,None],"POS3":["TipGEBAF250A",None,None],"POS4":["TipGEBAF250A",None,None],"POS5":["useless",None,None],
                "POS6":["useless",None,None],"POS7":["useless",None,None],"POS8":["TipGEBAF250A",None,None],"POS9":["TipGEBAF250A",None,None],"POS10":[None,None,None],
                "POS11":[None,None,None],"POS12":[None,None,None],"POS13":[None,None,None],"POS14":[None,None,None],"POS15":["DeepwellPlateDT7350504",None,None],
                "POS16":["useless",None,None],"POS17":["PCRBioRadHSP9601",None,None],"POS18":["PCRMGILIDHOLD","PCRMGILID",None],"POS19":[None,None,None],"POS20":[None,None,"shake"],
                "POS21":["useless",None,None],"POS22":["PCRBioRadHSP9601",None,None],"POS23":["PCRMGILIDHOLD","PCRMGILID",None],"POS24":[None,None,None],"POS25":["DeepwellPlateDT7350504",None,None],
                "POS26":["DeepwellPlateDT7350504",None,None],"POS27":["DeepwellPlateDT7350504",None,None],"POS28":[None,None,None],"POS29":[None,None,None],"POS30":["useless",None,None],
                "POS31":["DeepwellPlateDT7350504",None,None],"POS32":["DeepwellPlateDT7350504",None,None],"POS33":[None,None,None],"POS34":[None,None,None],"POS35":[None,None,"trash"],
                "POS36":[None,None,None],"POS37":[None,None,None],"POS38":["PCRMST96DM",None,None],"POS39":["PCRMST96DM",None,None],"POS40":[None,None,None]}

#region HEAD
spx96 = globals().get("Spx96")

#simplest way 
from head import *
#init
init(spx96) #most important
binding_map(pos_type_map)

shake.binding(spx96)
#litter complex way, more hummable and readable
#from head import init
#from head import warn
#from head import info

#from head import aspirate
#from head import dispense
#from head import grasp
#from head import loosen
#from head import empty
#from head import load_tips
#from head import unload_tips
#from head import mix
#from head import mvkit
#from head import mvkit2
#from head import  

#from head import pcr_close_door
#from head import pcr_get_temp
#from head import pcr_open_door
#from head import pcr_run_methods
#from head import pcr_stop_heating

#from head import temp_check
#from head import temp_get_temp
#from head import temp_set
#from head import temp_sleep

#from shake import binding
#from shake import shaking
#from shake import shaking_with_time
#from shake import stop
#from shake import rate
#from shake import direct
#from time import sleep



#from head import binding
#from head import dely # seconds , 0.1s = 100ms
#from head import parallel_block # 
#from head import report
#from head import home #robot home

#init(spx96) #most important

#binding(spx96)

"""
不要修改HEAD
第一次调试修改时间-20180910，全程1h30'
"""
#20181022 更正PCR反应前加胶垫顺序。原来为先关门再加胶垫，现改为先加胶垫后关门。优化两台PCR的并行逻辑。 by 王岩琦
#20181024 将18与23号板位最底层改为PCRMGILIDHOLD by 王岩琦
#20190103 最后吸取洗脱DNA改为一吸两喷，以避免最终板底部出现气泡，使得QC前不用再离心 by 王岩琦

report(phase = 'PCR反应', step = 'PCR A反应开始')

home()

a_pcr_open_door()
b_pcr_open_door()



mvkit('POS18','POS17')
def blockA(): 
    a_pcr_close_door()
    a_pcr_run_methods(method = 'START')
    a_pcr_run_methods(method = '25-4')
    a_pcr_run_methods(method = 'Nifty_PCR')
a = parallel_block(blockA) #PCRA已经开始...正在执行

report(phase = 'PCR反应', step = 'PCR B反应开始')

mvkit('POS23','POS22')
def PCRB(): 
    b_pcr_close_door()
    b_pcr_run_methods(method = 'START')
    b_pcr_run_methods(method = '25-4')
    b_pcr_run_methods(method = 'Nifty_PCR')
b = parallel_block(PCRB) #PCRB已经开始...正在执行

a.Wait()

report(phase = 'PCR后纯化', step = '第一板磁珠结合开始')

a_pcr_open_door()
mvkit('POS17','POS18')

load_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'Tips':96}) #①样品+beads   2′
aspirate({'Module' : 'POS17', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.2,'AspirateVolume': (60), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS27', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
#底部吹打使磁珠不贴壁
mix({'Module' : 'POS27', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (15),'MixLoopVolume': (80),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':230,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
mix({'Module' : 'POS27', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':4,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (15),'MixLoopVolume': (80),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

b.Wait()

report(phase = 'PCR后纯化', step = '第二板磁珠结合开始')

b_pcr_open_door()
mvkit('POS22','POS23')

load_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'Tips':96}) #②样品+beads   2′
aspirate({'Module' : 'POS22', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.2,'AspirateVolume': (60), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS32', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
#底部吹打使磁珠不贴壁
mix({'Module' : 'POS32', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (15),'MixLoopVolume': (80),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':230,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
mix({'Module' : 'POS32', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':4,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (15),'MixLoopVolume': (80),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})
def blockF(): 
    b_pcr_run_methods(method = '4-25')
    b_pcr_stop_heating()
f = parallel_block(blockF) #PCRB停止

a_pcr_run_methods(method = '4-25')
a_pcr_stop_heating()#PCRA停止
dely(90)    

mvkit('POS27','POS19')  #一计时5’05”
dely(85)
mvkit('POS32','POS24')  #二计时5’05”

report(phase = 'PCR后纯化', step = '第一板乙醇洗涤开始')

load_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'Tips':96}) #①去除废液  1’  一上架计时2’15”
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (90), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS4', 'Well':'1A','SafePointOfZ':15})

for x in range(2):  #①加乙醇洗涤  4′20
    load_tips({'Module' : 'POS%d'%(8-x), 'Well':'1A','Tips':96}) 
    aspirate({'Module' : 'POS26', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (150), 'PreAirVolume': (5), 'PostAirVolume': (5),'AspirateRateOfP':100,'DelySeconds':0.5})
    empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':3,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (0),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (0),'MixLoopAspirateRate':200,'MixLoopDispenseRate':200
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':0,"SecondRouteRate": 38.0})
    aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (165), 'PreAirVolume': (5), 'AspirateRateOfP':10,'DelySeconds':0.5})
    empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':6+4*x,'DispenseRateOfP':50,'DelySeconds':0.5})
    unload_tips({'Module' : 'POS%d'%(8-x),'Col' : 1, 'Row' : 1,'SafePointOfZ':15})	

report(phase = 'PCR后纯化', step = '第二板乙醇洗涤开始')

load_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'Tips':96}) #②去除废液  1‘  二上架6’30”
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (90), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':12,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS5', 'Well':'1A','SafePointOfZ':15})

for x in range(2):  #②加乙醇洗涤  4′20
    load_tips({'Module' : 'POS%d'%(3-x), 'Well':'1A','Tips':96}) 
    aspirate({'Module' : 'POS26', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (150), 'PreAirVolume': (5), 'PostAirVolume': (5),'AspirateRateOfP':100,'DelySeconds':0.5})
    empty({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':3,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (0),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (0),'MixLoopAspirateRate':200,'MixLoopDispenseRate':200
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':0,"SecondRouteRate": 38.0})
    aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (165), 'PreAirVolume': (5), 'AspirateRateOfP':10,'DelySeconds':0.5})
    empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':19+4*x,'DispenseRateOfP':50,'DelySeconds':0.5})
    unload_tips({'Module' : 'POS%d'%(3-x),'Col' : 1, 'Row' : 1,'SafePointOfZ':15})	

report(phase = 'PCR后纯化', step = '第一板洗脱回溶开始')

load_tips({'Module' : 'POS6', 'Col' : 1, 'Row' : 1,'Tips':96}) #①洗脱磁珠   55″
aspirate({'Module' : 'POS31', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (32), 'PreAirVolume': (5),'PostAirVolume': (2),'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS6', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS19','POS20')#抓手 #20″

shake_on(1200,1)
dely(120)
shake_off()
mvkit('POS20','POS27') 

report(phase = 'PCR后纯化', step = '第二板洗脱回溶开始')

load_tips({'Module' : 'POS1', 'Col' : 1, 'Row' : 1,'Tips':96}) #②洗脱磁珠   55″
aspirate({'Module' : 'POS31', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (32), 'PreAirVolume': (5),'PostAirVolume': (2),'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS1', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS24','POS20')#抓手 20″

shake_on(1200,1)
dely(120)
shake_off()
dely(50)

report(phase = 'PCR后纯化', step = '第一板吸取洗脱DNA')

mvkit('POS27','POS19')    #一计时5’05”
dely(150)

load_tips({'Module' : 'POS6', 'Col' : 1, 'Row' : 1,'Tips':96})  #吸取洗脱DNA①    55″   一上架计时2’50”
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (32), 'PreAirVolume': (5),'AspirateRateOfP':10,'DelySeconds':0.5})
dispense({'Module' : 'POS38', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':0.3,'DispenseVolume': (32),'DispenseRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS38', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':10,'DelySeconds':0.5})
unload_tips({'Module' : 'POS6', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = 'PCR后纯化', step = '第二板吸取洗脱DNA')

mvkit('POS20','POS24')    #二计时5’05”
dely(150)

load_tips({'Module' : 'POS1', 'Col' : 1, 'Row' : 1,'Tips':96})  #吸取洗脱DNA②   55″
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (32), 'PreAirVolume': (5),'AspirateRateOfP':10,'DelySeconds':0.5})
dispense({'Module' : 'POS39', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':0.3,'DispenseVolume': (32),'DispenseRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS39', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':10,'DelySeconds':0.5})
unload_tips({'Module' : 'POS1', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})
f.Wait()
home()







