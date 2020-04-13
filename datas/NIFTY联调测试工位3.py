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

# *************离线添加头部（离线请添加以下指令覆盖映射表）***********
# pos_type_map = {"POS1":["useless",None,None],"POS2":["GETP01",None,None],"POS3":["GETP01",None,None],"POS4":["GETP01",None,None],"POS5":["useless",None,None],
                # "POS6":["useless",None,None],"POS7":["GETP01",None,None],"POS8":["GETP01",None,None],"POS9":["GETP01",None,None],"POS10":["useless",None,None],
                # "POS11":[None,None,None],"POS12":[None,None,None],"POS13":[None,None,None],"POS14":[None,None,None],"POS15":["BGTE03",None,None],
                # "POS16":[None,None,None],"POS17":["BGMX01",None,None],"POS18":[None,None,None],"POS19":[None,None,None],"POS20":[None,None,"shake"],
                # "POS21":[None,None,None],"POS22":["BGMX01",None,None],"POS23":[None,None,None],"POS24":[None,None,None],"POS25":["DNDW01",None,None],
                # "POS26":["BRMW01",None,None],"POS27":["BGET01",None,None],"POS28":["BGBD04",None,None],"POS29":[None,None,None],"POS30":[None,None,None],
                # "POS31":["BRMW01",None,None],"POS32":["BGET01",None,None],"POS33":["BGBD04",None,None],"POS34":[None,None,None],"POS35":[None,None,"trash"],
                # "POS36":["BGBF02",None,None],"POS37":["BGEZ02",None,None],"POS38":["BGBF03",None,None],"POS39":["BGPM01",None,None],"POS40":["BGBC01",None,None]}
# binding_map(pos_type_map) 

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

report(phase = '接头连接', step = 'PCR与温控实验前准备')

home()

#def blockC1(): 
#    c1_home()
#c1 = parallel_block(blockC1) #温控1复位

#def blockC2(): 
#    c2_home()
#c2 = parallel_block(blockC2) #温控2复位

#def blockC3(): 
#    c3_home()
#c3 = parallel_block(blockC3) #温控3复位

#def blockC4(): 
#    c4_home()
#c4 = parallel_block(blockC4) #温控4复位

#c1.Wait()
#c2.Wait()
#c3.Wait()
#c4.Wait()

def blockA(): 
    a_pcr_close_door()
    a_pcr_open_door()
    a_pcr_run_methods(method = 'START')
    a_pcr_run_methods(method = '25-4')
a = parallel_block(blockA) #PCRA预热已经开始...正在执行

def blockB(): 
    b_pcr_close_door()
    b_pcr_open_door()
    b_pcr_run_methods(method = 'START')
    b_pcr_run_methods(method = '25-4')
b = parallel_block(blockB) #PCRB预热已经开始...正在执行

def blockK1(): 
    temp_a(4)
k1 = parallel_block(blockK1) #温控A已经开始...正在执行

def blockK2(): 
    temp_b(4)
k2 = parallel_block(blockK2) #温控B已经开始...正在执行

def blockK3(): 
    temp_c(4)
k3 = parallel_block(blockK3) #温控C已经开始...正在执行

def blockK4(): 
    temp_d(4)
k4 = parallel_block(blockK4) #温控D已经开始...正在执行

#c1_in()
#c2_in()
#c3_in()
#c4_in()

a.Wait()
b.Wait()
k1.Wait()
k2.Wait()
k3.Wait()
k4.Wait()

report(phase = '接头连接', step = 'PCR A加连接mix和barcode')


load_tips({'Module':'POS8','Col':1,'Row':1,'Tips':96})  #①加接头+①混匀样本和mix  2'
aspirate({'Module' : 'POS40', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (5), 'PreAirVolume': (10),'PostAirVolume': (3),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS17', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':7,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS17', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':8,'MixOffsetOfZAfterLoop':7,'PreAirVolume': (10),'MixLoopVolume': (60),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS8', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '接头连接', step = 'PCR A连接反应开始')

b.Wait()

report(phase = '接头连接', step = 'PCR B连接反应开始')

#c1_out()
#c2_out()

a_pcr_open_door()#PCRA连接结束，开盖准备转至beads

report(phase = 'PCR前纯化', step = '第一板磁珠结合开始')

report(phase = 'PCR前纯化', step = '第二板磁珠结合开始')

b_pcr_open_door()#PCRB连接结束，开盖准备转至beads

def blockE(): 
    a_pcr_run_methods(method = '4-25')
    a_pcr_stop_heating()
e = parallel_block(blockE) #PCRA停止

def blockF(): 
    b_pcr_run_methods(method = '4-25')
    b_pcr_stop_heating()
f = parallel_block(blockF) #PCRB停止

mvkit('POS28','POS19')  #一5min计时
mvkit('POS33','POS24')  #二5min计时

report(phase = 'PCR前纯化', step = '第一板乙醇洗涤开始')

load_tips({'Module' : 'POS8', 'Col' : 1, 'Row' : 1,'Tips':96}) #①去除废液  55 ″     一上架3'
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (110), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS8', 'Well':'1A','SafePointOfZ':15}) 

report(phase = 'PCR前纯化', step = '第一板洗脱回溶开始')

mvkit('POS19','POS20')#转移振荡器(TE)

mvkit('POS20','POS28') #洗脱震荡后静置①

report(phase = 'PCR前纯化', step = '第二板洗脱回溶开始')

load_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'Tips':96}) #②洗脱磁珠   50″  二计时5’
aspirate({'Module' : 'POS15', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (23), 'PreAirVolume': (5),'PostAirVolume': (2),'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS24','POS20')#②转移振荡器(TE)

mvkit('POS28','POS19')#TE洗脱静置后上架①

report(phase = 'PCR前纯化', step = '配制PCR mix并分装')

load_tips({'Module':'POS7','Col':1,'Row':1,'Tips':96})#配PCRmix+分装mix  2′50"
aspirate({'Module' : 'POS38', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (55), 'PreAirVolume': (5),'PostAirVolume': (0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS39', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5,"TipTouchHeight":3,"TipTouchOffsetOfX": 1})
mix({'Module' : 'POS39', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.8,'MixOffsetOfZInLoop':6,'MixOffsetOfZAfterLoop':5,'PreAirVolume': (10),'MixLoopVolume': (50),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

def blockK5(): 
    temp_sleep_a()
k5 = parallel_block(blockK5) #温控A终止...正在执行

def blockK6(): 
    temp_sleep_b()
k6 = parallel_block(blockK6) #温控B终止...正在执行

def blockK7(): 
    temp_sleep_c()
k7 = parallel_block(blockK7) #温控C终止...正在执行

def blockK8(): 
    temp_sleep_d()
k8 = parallel_block(blockK8) #温控D终止...正在执行

report(phase = 'PCR前纯化', step = '第一板吸取洗脱DNA')

load_tips({'Module' : 'POS3', 'Col' : 1, 'Row' : 1,'Tips':96})  #①吸取洗脱DNA    2’
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (28), 'PreAirVolume': (2),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS26', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':10,'DelySeconds':0.5})
mix({'Module' : 'POS26', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (10),'MixLoopVolume': (40),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS3', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = 'PCR前纯化', step = '第二板吸取洗脱DNA')

mvkit('POS20','POS24')#TE洗脱静置后上架②
#c3_out()
#c4_out()

e.Wait()
f.Wait()

k5.Wait()
k6.Wait()
k7.Wait()
k8.Wait()

jc("POS17")
jc("POS22")

home()
