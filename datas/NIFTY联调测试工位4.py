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
# pos_type_map = {"POS1":["useless",None,None],"POS2":["useless",None,None],"POS3":["GETP01",None,None],"POS4":["GETP01",None,None],"POS5":["useless",None,None],
                # "POS6":["useless",None,None],"POS7":[None,None,None],"POS8":["GETP01",None,None],"POS9":["GETP01",None,None],"POS10":[None,None,None],
                # "POS11":[None,None,None],"POS12":[None,None,None],"POS13":[None,None,None],"POS14":[None,None,None],"POS15":["BGTE01",None,None],
                # "POS16":["useless",None,None],"POS17":["BRMW01",None,None],"POS18":[None,None,None],"POS19":[None,None,None],"POS20":[None,None,"shake"],
                # "POS21":["useless",None,None],"POS22":["BRMW01",None,None],"POS23":[None,None,None],"POS24":[None,None,None],"POS25":["DNDW01",None,None],
                # "POS26":["BGET01",None,None],"POS27":["BGBD05",None,None],"POS28":[None,None,None],"POS29":[None,None,None],"POS30":["useless",None,None],
                # "POS31":["BGET01",None,None],"POS32":["BGBD05",None,None],"POS33":[None,None,None],"POS34":[None,None,None],"POS35":[None,None,"trash"],
                # "POS36":[None,None,None],"POS37":[None,None,None],"POS38":["BRMW01",None,None],"POS39":["BRMW01",None,None],"POS40":[None,None,None]}
# binding_map(pos_type_map) 


"""
不要修改HEAD
第一次调试修改时间-20180910，全程1h30'
"""
#20181022 更正PCR反应前加胶垫顺序。原来为先关门再加胶垫，现改为先加胶垫后关门。优化两台PCR的并行逻辑。 by 王岩琦
#20181024 将18与23号板位最底层改为PCRMGILIDHOLD by 王岩琦
#20190103 最后吸取洗脱DNA改为一吸两喷，以避免最终板底部出现气泡，使得QC前不用再离心 by 王岩琦
#2019.7.26 联调测试脚本 by 赵桂丽

home()

report(phase = 'PCR反应', step = 'PCR A反应开始')

# a_pcr_open_door()
b_pcr_open_door()


# def blockA(): 
    # a_pcr_close_door()
    # a_pcr_run_methods(method = 'START')
   
# a = parallel_block(blockA) #PCRA已经开始...正在执行

report(phase = 'PCR反应', step = 'PCR B反应开始')

def PCRB(): 
    b_pcr_close_door()
    b_pcr_run_methods(method = 'START')
   
b = parallel_block(PCRB) #PCRB已经开始...正在执行

# a.Wait()

report(phase = 'PCR后纯化', step = '第一板磁珠结合开始')

# a_pcr_open_door()


load_tips({'Module' : 'POS8', 'Col' : 1, 'Row' : 1,'Tips':96}) #①样品+beads   2′
aspirate({'Module' : 'POS17', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.2,'AspirateVolume': (60), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS27', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS8', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

b.Wait()

report(phase = 'PCR后纯化', step = '第二板磁珠结合开始')

b_pcr_open_door()


load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96}) #②样品+beads   2′
aspirate({'Module' : 'POS22', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.2,'AspirateVolume': (60), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS32', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

# def blockE(): 
    # a_pcr_stop_heating()
# e = parallel_block(blockE) #PCRA停止

def blockF(): 
    b_pcr_stop_heating()
f = parallel_block(blockF) #PCRB停止


mvkit('POS27','POS19')  #一计时5’05”
mvkit('POS32','POS24')  #二计时5’05”

report(phase = 'PCR后纯化', step = '第一板乙醇洗涤开始')

load_tips({'Module' : 'POS8', 'Col' : 1, 'Row' : 1,'Tips':96}) #①去除废液  1’  一上架计时2’15”
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (90), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS8', 'Well':'1A','SafePointOfZ':15})

report(phase = 'PCR后纯化', step = '第二板乙醇洗涤开始')

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96}) #②去除废液  1‘  二上架6’30”
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (90), 'PreAirVolume': (5), 'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS25', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':12,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS9', 'Well':'1A','SafePointOfZ':15})

report(phase = 'PCR后纯化', step = '第一板洗脱回溶开始')


mvkit('POS19','POS20')#抓手 #20″

shake_on(1200,1)
dely(5)
shake_off()
mvkit('POS20','POS27') 

report(phase = 'PCR后纯化', step = '第二板洗脱回溶开始')


mvkit('POS24','POS20')#抓手 20″

shake_on(1200,1)
dely(5)
shake_off()


report(phase = 'PCR后纯化', step = '第一板吸取洗脱DNA')

mvkit('POS27','POS19')    #一计时5’05”

load_tips({'Module' : 'POS3', 'Col' : 1, 'Row' : 1,'Tips':96})  #吸取洗脱DNA①    55″   一上架计时2’50”
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (32), 'PreAirVolume': (5),'AspirateRateOfP':10,'DelySeconds':0.5})
dispense({'Module' : 'POS38', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':0.3,'DispenseVolume': (32),'DispenseRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS38', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':10,'DelySeconds':0.5})
unload_tips({'Module' : 'POS3', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = 'PCR后纯化', step = '第二板吸取洗脱DNA')

mvkit('POS20','POS24')    #二计时5’05”
mvkit('POS19','POS27')  #一计时5’05”
mvkit('POS24','POS32')

jc("POS17")#丢掉中间板①
jc("POS22")#丢掉中间板②


# e.Wait()
f.Wait()

home()







