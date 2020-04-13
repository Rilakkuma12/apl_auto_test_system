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
# pos_type_map = {"POS1":["useless",None,None],"POS2":["useless",None,None],"POS3":["useless",None,None],"POS4":["GETP02",None,None],"POS5":["GETP02",None,None],
                # "POS6":["useless",None,None],"POS7":["GETP01",None,None],"POS8":["GETP01",None,None],"POS9":["GETP01",None,None],"POS10":["GETP01",None,None],
                # "POS11":[None,None,None],"POS12":[None,None,None],"POS13":["BGBD02",None,None],"POS14":["BGBD02",None,None],"POS15":[None,None,None],
                # "POS16":[None,None,None],"POS17":["BGMX01",None,None],"POS18":[None,None,None],"POS19":["BGBD02",None,None],"POS20":[None,None,"shake"],
                # "POS21":[None,None,None],"POS22":["BGMX01",None,None],"POS23":[None,None,None],"POS24":["BGBD02",None,None],"POS25":["BGTE02",None,None],
                # "POS26":[None,None,None],"POS27":[None,None,None],"POS28":["BGBD03",None,None],"POS29":["BGBD03",None,None],"POS30":[None,None,None],
                # "POS31":[None,None,None],"POS32":[None,None,None],"POS33":["BGET01",None,None],"POS34":["BGET01",None,None],"POS35":[None,None,"trash"],
                # "POS36":[None,None,None],"POS37":[None,None,None],"POS38":[None,None,None],"POS39":[None,None,None],"POS40":[None,None,None]}
# binding_map(pos_type_map) 

"""
不要修改HEAD
第一次调试修改时间-20180910，全程58'
"""
#20181019 将第2板丢弃位置改为35号，更新mapping至三维 by 王岩琦
home()

# def blockC1(): 
    # c1_home()
# c1 = parallel_block(blockC1) #温控1复位

# def blockC2(): 
    # c2_home()
# c2 = parallel_block(blockC2) #温控2复位

def blockA(): 
    a_pcr_close_door()
    a_pcr_open_door()

a = parallel_block(blockA) #PCRA预热开始...正在执行

def blockB(): 
    b_pcr_close_door()
    b_pcr_open_door()

b = parallel_block(blockB) #PCRB预热开始...正在执行

def blockC(): 
    temp_a(4)
c = parallel_block(blockC) #温控A已经开始...正在执行（末端buffer备用板位）

def blockD(): 
    temp_b(4)
d = parallel_block(blockD) #温控B已经开始...正在执行（末端酶备用板位）


report(phase = '片段筛选', step = '片筛前，等待提取磁珠洗脱')

report(phase = '片段筛选', step = '第二板第一次结合磁珠')
load_tips({'Module' : 'POS10', 'Col' : 1, 'Row' : 1,'Tips':96}) #②转移样品+beads1   1′45
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.1,'AspirateVolume': (35), 'PreAirVolume': (3),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':2})
empty({'Module' : 'POS14', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':1,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS10', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '片段筛选', step = '第一次磁珠结合等待，同时丢掉样品板')

mvkit('POS19','POS12')  #移开样品板①
mvkit('POS24','POS27')  #移开样品板②

report(phase = '片段筛选', step = '第一板第一次磁珠上架')
mvkit('POS13','POS19')  #20″ ①beads1上架，一计时6’10“

report(phase = '片段筛选', step = '第二板第一次磁珠上架')
mvkit('POS14','POS24')  #20″ ②beads1上架，二计时6’20“

mvkit('POS19','POS38')  #①beads1移开，作废液板
mvkit('POS24','POS39')  #②beads1移开，作废液板

report(phase = '片段筛选', step = '第一板第二次磁珠上架')
mvkit('POS28','POS19')  #20″ ①beads2上架
report(phase = '片段筛选', step = '第二板第二次磁珠上架')
mvkit('POS29','POS24')#二计时8’②beads2上架

report(phase = '片段筛选', step = '第一板去除beads2废液')
load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96}) #①去除废液  40″
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (100), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS38', 'Col' : 1, 'Row' : 1,'Bo  ttomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':2})

report(phase = '片段筛选', step = '第一板乙醇洗涤')

unload_tips({'Module' : 'POS7','Col' : 1, 'Row' : 1,'SafePointOfZ':15})  

report(phase = '片段筛选', step = '第二板去除beads2废液')
load_tips({'Module' : 'POS8', 'Col' : 1, 'Row' : 1,'Tips':96}) #②去除废液  40″
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (100), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS39', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})

report(phase = '片段筛选', step = '第二板乙醇洗涤')

unload_tips({'Module' : 'POS8','Col' : 1, 'Row' : 1,'SafePointOfZ':15}) 

report(phase = '片段筛选', step = '第一板加TE')

load_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'Tips':96}) #①TE洗脱磁珠   40″
aspirate({'Module' : 'POS25', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (42), 'PreAirVolume': (3),'PostAirVolume': (0),'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS19','POS20')#①转移振荡器(TE)

report(phase = '片段筛选', step = '第二板加TE，第一板震荡')

load_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'Tips':96}) #②TE洗脱磁珠   40″  二上架计时3’
aspirate({'Module' : 'POS25', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (42), 'PreAirVolume': (3),'PostAirVolume': (0),'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '片段筛选', step = '第一板静置，第二板震荡')

mvkit('POS20','POS13')#①TE上架前洗脱静置
mvkit('POS24','POS20')#②转移振荡器(TE)
mvkit('POS13','POS19')#①第一板上架

a.Wait()
report(phase = '末端修复', step = '第一板吸取洗脱DNA加入末修mix')

report(phase = '末端修复', step = 'PCR A末端反应开始')


report(phase = '末端修复', step = '第二板上架')
mvkit('POS20','POS24')#②第二板上架
b.Wait()
load_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'Tips':96})  #②吸取洗脱DNA    1分15秒
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.1,'AspirateVolume': (45), 'PreAirVolume': (5),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS22', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':1,'DispenseRateOfP':10,'DelySeconds':0.5})
mix({'Module' : 'POS22', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':5,'PreAirVolume': (10),'MixLoopVolume': (40),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 50.0})
unload_tips({'Module' : 'POS5', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '末端修复', step = 'PCR B末端反应开始')

report(phase = '末端修复', step = 'PCR A末端反应结束')

#a_pcr_open_door()

report(phase = '末端修复', step = 'PCR B末端反应结束')

#b_pcr_open_door()

c.Wait()
d.Wait()

temp_sleep_a()
temp_sleep_b()

jc("POS12")
jc("POS27")

home()

