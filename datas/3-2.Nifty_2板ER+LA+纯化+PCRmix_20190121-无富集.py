# -*- coding: utf-8 -*-
"""
***Spx head example***
wangjian5@genomics.cn
jjseen@163.com
"""
#region pos and kit type mapping table
#three write methods:empty-None; pcr-"pcr"; kit-"kit" ;cannot grasp/loose-"useless"  shake-([,"shake"])
pos_type_map = {"POS1":["TipGEBAF250A",None,None],"POS2":["TipGEBAF250A",None,None],"POS3":["TipGEBAF250A",None,None],"POS4":["TipGEBAF250A",None,None],"POS5":["TipGEBAF250A",None,None],
                "POS6":["TipGEBAF250A",None,None],"POS7":["TipGEBAF250A",None,None],"POS8":["TipGEBAF250A",None,None],"POS9":["TipGEBAF250A",None,None],"POS10":["TipGEBAF250A",None,None],
                "POS11":["TipGEBAF250A",None,None],"POS12":["TipGEBAF250A",None,None],"POS13":[None,None,None],"POS14":[None,None,None],"POS15":[None,None,None],
                "POS16":["useless",None,None],"POS17":["PCRBioRadHSP9601",None,None],"POS18":["PCRMGILIDHOLD","PCRMGILID",None],"POS19":["DeepwellPlateDT7350504",None,None],"POS20":[None,None,"shake"],
                "POS21":["useless",None,None],"POS22":["PCRBioRadHSP9601",None,None],"POS23":["PCRMGILIDHOLD","PCRMGILID",None],"POS24":["DeepwellPlateDT7350504",None,None],"POS25":["DeepwellPlateDT7350504",None,None],
                "POS26":["PCRBioRadHSP9601",None,None],"POS27":["DeepwellPlateDT7350504",None,None],"POS28":["DeepwellPlateDT7350504",None,None],"POS29":[None,None,None],"POS30":["useless",None,None],
                "POS31":["PCRBioRadHSP9601",None,None],"POS32":["DeepwellPlateDT7350504",None,None],"POS33":["DeepwellPlateDT7350504",None,None],"POS34":[None,None,None],"POS35":[None,None,"trash"],
                "POS36":["PCRMST96DM",None,None],"POS37":["PCRMST96DM",None,None],"POS38":["PCRMST96DM",None,None],"POS39":["PCRMST96DM",None,None],"POS40":["PCRMST96DM",None,None]}

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
20180912   用SPC计时  全程1h53'
"""
#20181016 更正加lid步骤，更改head中map至三维 by 王岩琦
#20181017 增补末修与连接反应后去掉lid的步骤 by 王岩琦
#20181024 将18与23号板位最底层改为PCRMGILIDHOLD。加入温控模块c,d。样品板丢弃位置改为29，34号位。 by 王岩琦
#20190103 小试、中试、试生产中优化多处操作，降低气泡率、减少漏吸 by 王岩琦
#20190109 最后四个温控终止改为并行，并在分装完PCR mix后就开始终止，节省12分钟。
#20190121 温控并行流程ghij的wait指令移至连接反应开始。但温控的开始指令ghij仍为末端时候启动。可以节省时间。

home()

report(phase = '末端修复', step = 'PCR与温控实验前准备')

def blockA(): 
    a_pcr_close_door()
    a_pcr_open_door()
    a_pcr_run_methods(method = 'START')
    a_pcr_run_methods(method = '25-4')
a = parallel_block(blockA) #PCRA已经开始...正在执行

def blockG(): 
    temp_a(4)
g = parallel_block(blockG) #温控A已经开始...正在执行

def blockH(): 
    temp_b(4)
h = parallel_block(blockH) #温控B已经开始...正在执行
def blockI(): 
    temp_c(4)
i = parallel_block(blockI) #温控C已经开始...正在执行

def blockJ(): 
    temp_d(4)
j = parallel_block(blockJ) #温控D已经开始...正在执行
b_pcr_close_door()
b_pcr_open_door()
b_pcr_run_methods(method = 'START')
b_pcr_run_methods(method = '25-4')

a.Wait()


report(phase = '末端修复', step = 'PCR A末端反应开始')

load_tips({'Module':'POS1','Col':1,'Row':1,'Tips':96})#①混匀样本和末修mix  1'50"
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.45,'AspirateVolume': (40), 'PreAirVolume': (5),'PostAirVolume': (0),'AspirateRateOfP':8,'DelySeconds':0.5})
empty({'Module' : 'POS17', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':4,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS17', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.7,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (10),'MixLoopVolume': (40),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS1', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS18','POS17')#PCRA加lid

def blockC(): 
    a_pcr_close_door()
    a_pcr_run_methods(method = 'Nifty_ER')
c = parallel_block(blockC) #PCRA已经开始末修反应...正在执行

report(phase = '末端修复', step = 'PCR B末端反应开始')

load_tips({'Module':'POS2','Col':1,'Row':1,'Tips':96})#②混匀样本和末修mix    1'50"
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.45,'AspirateVolume': (40), 'PreAirVolume': (5),'PostAirVolume': (0),'AspirateRateOfP':8,'DelySeconds':0.5})
empty({'Module' : 'POS22', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':4,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS22', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.7,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (10),'MixLoopVolume': (40),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS23','POS22')#PCRB加lid

def blockB(): 
    b_pcr_close_door()
    b_pcr_run_methods(method = 'Nifty_ER')
b = parallel_block(blockB) #PCRB已经开始末修反应...正在执行

c.Wait()
a_pcr_open_door()

mvkit('POS17','POS18')#末修后PCRA去lid

report(phase = '接头连接', step = 'PCR A加连接mix和barcode')

g.Wait()
h.Wait()
i.Wait()
j.Wait()

load_tips({'Module':'POS3','Col':1,'Row':1,'Tips':96})#配连接mix+①加入mix    2'30"
aspirate({'Module' : 'POS36', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (55.8), 'PreAirVolume': (5),'PostAirVolume': (0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS37', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':4,'DispenseRateOfP':20,'DelySeconds':0.5,"TipTouchHeight":4,"TipTouchOffsetOfX": 1})
mix({'Module' : 'POS37', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':5,'PreAirVolume': (10),'MixLoopVolume': (50),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':60,'MixLoopDispenseRate':60
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
aspirate({'Module' : 'POS37', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.27,'AspirateVolume': (25), 'PreAirVolume': (5),'PostAirVolume': (0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS17', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS3', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})


load_tips({'Module':'POS4','Col':1,'Row':1,'Tips':96})  #①加接头+①混匀样本和mix  2'
aspirate({'Module' : 'POS40', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (5), 'PreAirVolume': (10),'PostAirVolume': (3),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS17', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':7,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS17', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':8,'MixOffsetOfZAfterLoop':7,'PreAirVolume': (10),'MixLoopVolume': (60),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '接头连接', step = 'PCR A连接反应开始')

mvkit('POS18','POS17')#连接前PCRA加lid
def blockD(): 
    a_pcr_close_door()
    a_pcr_run_methods(method = 'Nifty_Ad Ligation')
d = parallel_block(blockD) #PCRA已经开始连接反应...正在执行


b.Wait()

report(phase = '接头连接', step = 'PCR B加连接mix和barcode')

b_pcr_open_door()
mvkit('POS22','POS23')#末修后PCRB去lid
load_tips({'Module':'POS5','Col':1,'Row':1,'Tips':96})  #②加接头+②加入连接mix+②混匀样本和mix    2'30"
aspirate({'Module' : 'POS40', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (5), 'PreAirVolume': (10),'PostAirVolume': (3),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS22', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':20,'DelySeconds':0.5})
aspirate({'Module' : 'POS37', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.27,'AspirateVolume': (25), 'PreAirVolume': (5),'PostAirVolume': (0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS22', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':7,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS22', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':8,'MixOffsetOfZAfterLoop':7,'PreAirVolume': (10),'MixLoopVolume': (60),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '接头连接', step = 'PCR B连接反应开始')

mvkit('POS23','POS22')#连接前PCRB加lid
def blockE(): 
    b_pcr_close_door()
    b_pcr_run_methods(method = 'Nifty_Ad Ligation')
e = parallel_block(blockE) #PCRB已经开始连接反应...正在执行

def blockG2(): 
    temp_sleep_a()
g2 = parallel_block(blockG2) #温控A终止...正在执行

def blockH2(): 
    temp_sleep_b()
h2 = parallel_block(blockH2) #温控B终止...正在执行

d.Wait()
a_pcr_open_door()#PCRA连接结束，开盖准备转至beads

report(phase = 'PCR前纯化', step = '第一板磁珠结合开始')

mvkit('POS17','POS18')#连接后PCRA去lid
load_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'Tips':96}) #样品①+beads   2′08"
aspirate({'Module' : 'POS17', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.2,'AspirateVolume': (90), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS28', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
#底部吹打磁珠
mix({'Module' : 'POS28', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (15),'MixLoopVolume': (100),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':230,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
mix({'Module' : 'POS28', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':4,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (15),'MixLoopVolume': (100),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})
e.Wait()

report(phase = 'PCR前纯化', step = '第二板磁珠结合开始')

b_pcr_open_door()#PCRB连接结束，开盖准备转至beads
mvkit('POS22','POS23')#连接后PCRB去lid
load_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'Tips':96}) #样品②+beads   2′08"
aspirate({'Module' : 'POS22', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.2,'AspirateVolume': (90), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS33', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
#底部吹打磁珠
mix({'Module' : 'POS33', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (15),'MixLoopVolume': (100),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':230,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
mix({'Module' : 'POS33', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':4,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (15),'MixLoopVolume': (100),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})
def blockF(): 
    b_pcr_run_methods(method = '4-25')
    b_pcr_stop_heating()
f = parallel_block(blockF) #PCRB停止

a_pcr_run_methods(method = '4-25')
a_pcr_stop_heating()#PCRA停止


dely(50) 
mvkit('POS19','POS29')
mvkit('POS28','POS19')  #一5min计时
dely(60)
mvkit('POS24','POS34')
mvkit('POS33','POS24')  #二5min计时

report(phase = 'PCR前纯化', step = '第一板乙醇洗涤开始')

load_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'Tips':96}) #①去除废液  55 ″     一上架3'
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (110), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS4', 'Well':'1A','SafePointOfZ':15}) 


for x in range(2):  #①加乙醇洗涤  4′20″
    load_tips({'Module' : 'POS%d'%(6+x), 'Well':'1A','Tips':96}) 
    aspirate({'Module' : 'POS27', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (150), 'PreAirVolume': (5), 'PostAirVolume': (5),'AspirateRateOfP':100,'DelySeconds':0.5})
    empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':3,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (0),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (0),'MixLoopAspirateRate':200,'MixLoopDispenseRate':200
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':0,"SecondRouteRate": 38.0})
    aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (165), 'PreAirVolume': (5), 'AspirateRateOfP':10,'DelySeconds':0.5})
    empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':7+4*x,'DispenseRateOfP':50,'DelySeconds':0.5})
    unload_tips({'Module' : 'POS%d'%(6+x),'Col' : 1, 'Row' : 1,'SafePointOfZ':15})	

report(phase = 'PCR前纯化', step = '第二板乙醇洗涤开始')

load_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'Tips':96}) #②去除废液  55″
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (110), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':15,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS5', 'Well':'1A','SafePointOfZ':15})

for x in range(2):  #②加乙醇洗涤  4′20″
    load_tips({'Module' : 'POS%d'%(8+x), 'Well':'1A','Tips':96}) 
    aspirate({'Module' : 'POS27', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (150), 'PreAirVolume': (5), 'PostAirVolume': (5),'AspirateRateOfP':100,'DelySeconds':0.5})
    empty({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':3,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':0.5,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (0),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (0),'MixLoopAspirateRate':200,'MixLoopDispenseRate':200
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':0,"SecondRouteRate": 38.0})
    aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (165), 'PreAirVolume': (5), 'AspirateRateOfP':10,'DelySeconds':0.5})
    empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':19+4*x,'DispenseRateOfP':50,'DelySeconds':0.5})
    unload_tips({'Module' : 'POS%d'%(8+x),'Col' : 1, 'Row' : 1,'SafePointOfZ':15})	

report(phase = 'PCR前纯化', step = '第一板洗脱回溶开始')

load_tips({'Module' : 'POS10', 'Col' : 1, 'Row' : 1,'Tips':96}) #①洗脱磁珠   50″
aspirate({'Module' : 'POS32', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (23), 'PreAirVolume': (5),'PostAirVolume': (2),'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS10', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS19','POS20')#转移振荡器(TE)

shake_on(1200,1)
dely(120)
shake_off()
mvkit('POS20','POS28') #20″+10″

report(phase = 'PCR前纯化', step = '第二板洗脱回溶开始')

load_tips({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'Tips':96}) #②洗脱磁珠   50″  二计时5’
aspirate({'Module' : 'POS32', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (23), 'PreAirVolume': (5),'PostAirVolume': (2),'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS24','POS20')#②转移振荡器(TE)

shake_on(1200,1)
dely(120)
shake_off()
dely(50)
mvkit('POS28','POS19') #一计时5’

request_pcr_mix()

report(phase = 'PCR前纯化', step = '配制PCR mix并分装')

load_tips({'Module':'POS12','Col':1,'Row':1,'Tips':96})#配PCRmix+分装mix  2′50"
aspirate({'Module' : 'POS38', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (55), 'PreAirVolume': (5),'PostAirVolume': (0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS39', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5,"TipTouchHeight":3,"TipTouchOffsetOfX": 1})
mix({'Module' : 'POS39', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.8,'MixOffsetOfZInLoop':6,'MixOffsetOfZAfterLoop':5,'PreAirVolume': (10),'MixLoopVolume': (50),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
aspirate({'Module' : 'POS39', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (29), 'PreAirVolume': (5),'PostAirVolume': (0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS26', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':4,'DispenseRateOfP':20,'DelySeconds':0.5})
aspirate({'Module' : 'POS39', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (29), 'PreAirVolume': (5),'PostAirVolume': (0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS31', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':4,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS12', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})



def blockI2(): 
    temp_sleep_c()
i2 = parallel_block(blockI2) #温控C终止...正在执行

def blockJ2(): 
    temp_sleep_d()
j2 = parallel_block(blockJ2) #温控D终止...正在执行

report(phase = 'PCR前纯化', step = '第一板吸取洗脱DNA')

load_tips({'Module' : 'POS10', 'Col' : 1, 'Row' : 1,'Tips':96})  #①吸取洗脱DNA    2’
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (28), 'PreAirVolume': (2),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS26', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':10,'DelySeconds':0.5})
mix({'Module' : 'POS26', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (10),'MixLoopVolume': (40),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS10', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = 'PCR前纯化', step = '第二板吸取洗脱DNA')

mvkit('POS20','POS24')
dely(180)

load_tips({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'Tips':96})  #②吸取洗脱DNA    2'
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (28), 'PreAirVolume': (2),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS31', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':10,'DelySeconds':0.5})
mix({'Module' : 'POS31', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (10),'MixLoopVolume': (40),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

g2.Wait()
h2.Wait()
i2.Wait()
j2.Wait()

home()
