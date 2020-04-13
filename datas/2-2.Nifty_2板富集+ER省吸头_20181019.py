# -*- coding: utf-8 -*-
"""
***Spx head example***
wangjian5@genomics.cn
jjseen@163.com
"""
#region pos and kit type mapping table
#three write methods:empty-None; pcr-"pcr"; kit-"kit" ;cannot grasp/loose-"useless"  shake-([,"shake"])
pos_type_map = {"POS1":["useless",None,None],"POS2":["useless",None,None],"POS3":["useless",None,None],"POS4":["useless",None,None],"POS5":["useless",None,None],
                "POS6":["useless",None,None],"POS7":["useless",None,None],"POS8":["useless",None,None],"POS9":["useless",None,None],"POS10":["useless",None,None],
                "POS11":[None,None,None],"POS12":["useless",None,None],"POS13":["DeepwellPlateDT7350504",None,None],"POS14":["DeepwellPlateDT7350504",None,None],"POS15":[None,None,None],
                "POS16":[None,None,None],"POS17":[None,None,None],"POS18":["PCRMGILIDHOLD","PCRMGILID",None],"POS19":["DeepwellPlateDT7350504",None,None],"POS20":[None,None,"shake"],
                "POS21":[None,None,None],"POS22":[None,None,None],"POS23":["PCRMGILIDHOLD","PCRMGILID",None],"POS24":["DeepwellPlateDT7350504",None,None],"POS25":["DeepwellPlateDT7350504",None,None],
                "POS26":[None,None,None],"POS27":[None,None,None],"POS28":["DeepwellPlateDT7350504",None,None],"POS29":["DeepwellPlateDT7350504",None,None],"POS30":[None,None,None],
                "POS31":[None,None,None],"POS32":[None,None,None],"POS33":["PCRMST96DM",None,None],"POS34":["PCRMST96DM",None,None],"POS35":[None,None,"trash"],
                "POS36":["PCRBioRadHSP9601",None,None],"POS37":["PCRBioRadHSP9601",None,None],"POS38":[None,None,None],"POS39":[None,None,None],"POS40":[None,None,None]}

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
第一次调试修改时间-20180910，全程58'
"""
#20181019 将第2板丢弃位置改为35号，更新mapping至三维 by 王岩琦
home()


def blockA(): 
    a_pcr_close_door()
    a_pcr_open_door()
    a_pcr_run_methods(method = 'START')
    a_pcr_run_methods(method = '25-4')
a = parallel_block(blockA) #PCRA预热开始...正在执行

def blockB(): 
    b_pcr_close_door()
    b_pcr_open_door()
    b_pcr_run_methods(method = 'START')
    b_pcr_run_methods(method = '25-4')
b = parallel_block(blockB) #PCRB预热开始...正在执行

# def blockC(): 
    # temp_a(4)
# c = parallel_block(blockC) #温控A已经开始...正在执行（末端buffer备用板位）

# def blockD(): 
    # temp_b(4)
# d = parallel_block(blockD) #温控B已经开始...正在执行（末端酶备用板位）

report(phase = '片段筛选', step = '片筛前，等待提取磁珠洗脱')

dely(180)#富集前等待提取磁珠

report(phase = '片段筛选', step = '第一板第一次结合磁珠')
load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96}) #①转移样品+beads1   1′45
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.1,'AspirateVolume': (35), 'PreAirVolume': (3),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':2})
empty({'Module' : 'POS13', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':1,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS13', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':3,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (5),'MixLoopVolume': (60),'DispenseVolumeAfterSubmixLoop': (5),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 50.0})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '片段筛选', step = '第二板第一次结合磁珠')
load_tips({'Module' : 'POS10', 'Col' : 1, 'Row' : 1,'Tips':96}) #②转移样品+beads1   1′45
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.1,'AspirateVolume': (35), 'PreAirVolume': (3),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':2})
empty({'Module' : 'POS14', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':1,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS14', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':3,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (5),'MixLoopVolume': (60),'DispenseVolumeAfterSubmixLoop': (5),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 50.0})
unload_tips({'Module' : 'POS10', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})


report(phase = '片段筛选', step = '第一次磁珠结合等待，同时丢掉样品板')
def blockE(): 
    dely(180) 
e = parallel_block(blockE) #①&②第一次磁珠结合上架前共300秒

jc("POS19")#丢掉样品板①
jc("POS24")#丢掉样品板②

e.wait

report(phase = '片段筛选', step = '第一板第一次磁珠上架')
mvkit('POS13','POS19')  #20″ ①beads1上架，一计时6’10“
dely(70)  

report(phase = '片段筛选', step = '第二板第一次磁珠上架')
mvkit('POS14','POS24')  #20″ ②beads1上架，二计时6’20“
dely(210)

report(phase = '片段筛选', step = '第一板第二次结合磁珠')
load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96}) #①吸取上清液和Beads2混合  2′    一上架计时5’
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.1,'AspirateVolume': (73), 'PreAirVolume': (3),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':2})
empty({'Module' : 'POS28', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':1,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS28', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':3,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (5),'MixLoopVolume': (100),'DispenseVolumeAfterSubmixLoop': (5),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 50.0})
unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '片段筛选', step = '第二板第二次结合磁珠')
load_tips({'Module' : 'POS8', 'Col' : 1, 'Row' : 1,'Tips':96}) #②吸取上清液和Beads2混合  2′   二上架计时5’20
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.1,'AspirateVolume': (73), 'PreAirVolume': (3),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':2})
empty({'Module' : 'POS29', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':1,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS29', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':3,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (5),'MixLoopVolume': (100),'DispenseVolumeAfterSubmixLoop': (5),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 50.0})
unload_tips({'Module' : 'POS8', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})


mvkit('POS19','POS38')  #①beads1移开，作废液板
mvkit('POS24','POS39')  #②beads1移开，作废液板

dely(410)

report(phase = '片段筛选', step = '第一板第二次磁珠上架')
mvkit('POS28','POS19')  #20″ ①beads2上架
dely(90)

report(phase = '片段筛选', step = '第二板第二次磁珠上架')
mvkit('POS29','POS24')#二计时8’②beads2上架
dely(180)


report(phase = '片段筛选', step = '第一板去除beads2废液')
load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96}) #①去除废液  40″
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (100), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS38', 'Col' : 1, 'Row' : 1,'Bo  ttomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':2})

report(phase = '片段筛选', step = '第一板乙醇洗涤')

for x in range(2):  #①加乙醇洗涤 3′30
    aspirate({'Module' : 'POS33', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (150), 'PreAirVolume': (5), 'PostAirVolume': (5),'AspirateRateOfP':100,'DelySeconds':0.5})
    empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':3,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (0),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (0),'MixLoopAspirateRate':200,'MixLoopDispenseRate':200
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':0,"SecondRouteRate": 50.0})
    aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (165), 'PreAirVolume': (5), 'AspirateRateOfP':10,'DelySeconds':2})
    empty({'Module' : 'POS38', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})

unload_tips({'Module' : 'POS7','Col' : 1, 'Row' : 1,'SafePointOfZ':15})  

jc("POS38")#丢掉beads1①

report(phase = '片段筛选', step = '第二板去除beads2废液')
load_tips({'Module' : 'POS8', 'Col' : 1, 'Row' : 1,'Tips':96}) #②去除废液  40″
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (100), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS39', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})

report(phase = '片段筛选', step = '第二板乙醇洗涤')
	
for x in range(2):  #②加乙醇洗涤 3′30
    aspirate({'Module' : 'POS34', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (150), 'PreAirVolume': (5), 'PostAirVolume': (5),'AspirateRateOfP':100,'DelySeconds':0.5})
    empty({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':3,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (0),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (0),'MixLoopAspirateRate':200,'MixLoopDispenseRate':200
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':0,"SecondRouteRate": 50.0})
    aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (165), 'PreAirVolume': (5), 'AspirateRateOfP':10,'DelySeconds':2})
    empty({'Module' : 'POS39', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})

unload_tips({'Module' : 'POS8','Col' : 1, 'Row' : 1,'SafePointOfZ':15}) 

report(phase = '片段筛选', step = '第一板加TE')

load_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'Tips':96}) #①TE洗脱磁珠   40″
aspirate({'Module' : 'POS25', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (42), 'PreAirVolume': (3),'PostAirVolume': (0),'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS19','POS20')#①转移振荡器(TE)

def blockF(): 
    shake_on(1500,1)
    dely(180)
    shake_off()
f = parallel_block(blockG) #①TE洗脱震荡开始

report(phase = '片段筛选', step = '第二板加TE，第一板震荡')

load_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'Tips':96}) #②TE洗脱磁珠   40″  二上架计时3’
aspirate({'Module' : 'POS25', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (42), 'PreAirVolume': (3),'PostAirVolume': (0),'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

f.Wait() #等候①TE洗脱震荡完毕


report(phase = '片段筛选', step = '第一板静置，第二板震荡')

mvkit('POS20','POS13')#①TE上架前洗脱静置
mvkit('POS24','POS20')#②转移振荡器(TE)
shake_on(1500,1)
dely(60)
mvkit('POS13','POS19')#①第一板上架
dely(120)
shake_off()#②第二板开始静置
dely(60)

a.Wait()
report(phase = '末端修复', step = '第一板吸取洗脱DNA加入末修mix')

load_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'Tips':96})  #①吸取洗脱DNA加入末修mix     1'45 
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.1,'AspirateVolume': (45), 'PreAirVolume': (5),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS17', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':1,'DispenseRateOfP':10,'DelySeconds':0.5})
mix({'Module' : 'POS17', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':5,'PreAirVolume': (10),'MixLoopVolume': (40),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 50.0})
unload_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '末端修复', step = 'PCR A末端反应开始')

mvkit('POS18','POS17')#PCRA加lid
def blockG(): 
    a_pcr_close_door()
    a_pcr_run_methods(method = 'Nifty_ER')
g = parallel_block(blockC) #PCRA已经开始末修反应...正在执行


report(phase = '末端修复', step = '第二板上架')
mvkit('POS20','POS24')#②第二板上架
dely(180)#第二板上架3分钟

load_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'Tips':96})  #②吸取洗脱DNA    1分15秒
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.1,'AspirateVolume': (45), 'PreAirVolume': (5),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS22', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':1,'DispenseRateOfP':10,'DelySeconds':0.5})
mix({'Module' : 'POS22', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':5,'PreAirVolume': (10),'MixLoopVolume': (40),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 50.0})
unload_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})


report(phase = '末端修复', step = 'PCR B末端反应开始')

mvkit('POS23','POS22')#PCRB加lid

def blockH(): 
    b_pcr_close_door()
    b_pcr_run_methods(method = 'Nifty_ER')
h = parallel_block(blockB) #PCRB已经开始末修反应...正在执行

jc("POS39")#丢掉beads1②
jc("POS19")#丢掉beads2①
jc("POS24")#丢掉beads2②
jc("POS33")#丢掉乙醇①
jc("POS34")#丢掉乙醇②
jc("POS25")#丢掉TE

g.Wait()
report(phase = '末端修复', step = 'PCR A末端反应结束')

#a_pcr_open_door()
#mvkit('POS17','POS18')#末修后PCRA去lid

h.Wait()
report(phase = '末端修复', step = 'PCR B末端反应结束')

#b_pcr_open_door()
#mvkit('POS22','POS23')#末修后PCRB去lid

home()
