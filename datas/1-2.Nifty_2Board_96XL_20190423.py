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
                "POS11":["DeepwellPlateDT7350504",None,None],"POS12":["DeepwellPlateDT7350504",None,None],"POS13":["DeepwellPlateDT7350504",None,None],"POS14":["DeepwellPlateDT7350504",None,None],"POS15":[None,None,None],
                "POS16":[None,None,None],"POS17":[None,None,None],"POS18":["DeepwellPlateDT7350504",None,None],"POS19":[None,None,None],"POS20":[None,None,"shake"],
                "POS21":[None,None,None],"POS22":[None,None,None],"POS23":["DeepwellPlateDT7350504",None,None],"POS24":[None,None,None],"POS25":["DeepwellPlateDT7350504",None,None],
                "POS26":["DeepwellPlateDT7350504",None,None],"POS27":["DeepwellPlateDT7350504",None,None],"POS28":["DeepwellPlateDT7350504",None,None],"POS29":["DeepwellPlateDT7350504",None,None],"POS30":[None,None,None],
                "POS31":[None,None,None],"POS32":[None,None,None],"POS33":[None,None,None],"POS34":[None,None,None],"POS35":[None,None,"trash"],
                "POS36":[None,None,None],"POS37":[None,None,None],"POS38":[None,None,None],"POS39":[None,None,None],"POS40":[None,None,None]}

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
第一次调试修改时间-20180910，全程1h46'
"""

home()
report(phase = '提取', step = '第一板MLE裂解开始')


load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96})   #吸取血浆①    3分
for i in range(2):      
    aspirate({'Module' : 'POS12', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':1.2-i,'AspirateVolume': (100), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':20,'DelySeconds':0.5})
    empty({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':3+2*i,'MixOffsetOfZAfterLoop':3+2*i,'PreAirVolume': (15),'MixLoopVolume': (99),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
    ,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})
   
for i in range(2):     #吸取MLE①    3分钟
    aspirate({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':1.4-i,'AspirateVolume': (140), 'PreAirVolume': (7),'PostAirVolume': (3), 'AspirateRateOfP':50,'DelySeconds':0.5})
    empty({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':5})
    mix({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':6+2*i,'MixOffsetOfZAfterLoop':6+2*i,'PreAirVolume': (15),'MixLoopVolume': (140),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})
	

mix({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':16,'MixOffsetOfZAfterLoop':15,'PreAirVolume': (10),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})#①中间混匀血浆第一次   2'
unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '提取', step = '第二板MLE裂解开始')

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96})   #吸取血浆②    3分
for i in range(2):      
    aspirate({'Module' : 'POS14', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':1.2-i,'AspirateVolume': (100), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':20,'DelySeconds':0.5})
    empty({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':3+2*i,'MixOffsetOfZAfterLoop':3+2*i,'PreAirVolume': (15),'MixLoopVolume': (99),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
    ,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})
   
for i in range(2):     #吸取MLE②    3分钟
    aspirate({'Module' : 'POS13', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':1.4-i,'AspirateVolume': (140), 'PreAirVolume': (7),'PostAirVolume': (3), 'AspirateRateOfP':50,'DelySeconds':0.5})
    empty({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':5})
    mix({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':6+2*i,'MixOffsetOfZAfterLoop':6+2*i,'PreAirVolume': (15),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})
	

mix({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':16,'MixOffsetOfZAfterLoop':15,'PreAirVolume': (10),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})#②中间混匀血浆第一次  2'
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96})   #①中间混匀血浆第二次  2'35"
mix({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':16,'MixOffsetOfZAfterLoop':15,'PreAirVolume': (10),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})


load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96})   #②中间混匀血浆第二次 2'35"
mix({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':16,'MixOffsetOfZAfterLoop':15,'PreAirVolume': (10),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96})   #①中间混匀血浆第三次 2'35"
mix({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':16,'MixOffsetOfZAfterLoop':15,'PreAirVolume': (10),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96})   #②中间混匀血浆第三次  2'35"
mix({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':16,'MixOffsetOfZAfterLoop':15,'PreAirVolume': (10),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96})   #①中间混匀血浆第四次  2'35"
mix({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':16,'MixOffsetOfZAfterLoop':15,'PreAirVolume': (10),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':10,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS18','POS19') #①转移磁力架，吸附磁珠   20"+10"

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96})   #②中间混匀血浆第四次    2'35"
mix({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':16,'MixOffsetOfZAfterLoop':15,'PreAirVolume': (10),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':10,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

dely(400)

mvkit('POS23','POS24') #②转移磁力架，吸附磁珠   20"+10"

report(phase = '提取', step = '第一板MLE去废液')

load_tips({'Module' : 'POS7', 'Col' :1, 'Row' : 1,'Tips':96})  #转移①废液（MLE）  3'
for i in range(4):
    aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3.5-i,'AspirateVolume': (120), 'PreAirVolume': (7),'PostAirVolume': (3), 'AspirateRateOfP':20,'DelySeconds':0.5})
    empty({'Module' : 'POS12', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3+i,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS7', 'Well':'1A','SafePointOfZ':15})

report(phase = '提取', step = '第一板MW1洗涤')

mvkit('POS19','POS20') #①转移振荡器(加MW1) 20"+10"

load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96}) #洗涤MW1①   3'20"
aspirate({'Module' : 'POS26', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
shake_on(1200,1)
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':15,'BottomOffsetOfZ':0.8,'MixOffsetOfZInLoop':0.8,'MixOffsetOfZAfterLoop':2,'PreAirVolume': (15),'MixLoopVolume': (120),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':150,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
shake_off()
aspirate({'Module' : 'POS26', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (15),'MixLoopVolume': (148),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

dely(90)

report(phase = '提取', step = '第二板MLE去废液')

load_tips({'Module' : 'POS9', 'Col' :1, 'Row' : 1,'Tips':96})  #转移②废液(MLE)  3'
for i in range(4):
    aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3.5-i,'AspirateVolume': (120), 'PreAirVolume': (7),'PostAirVolume': (3), 'AspirateRateOfP':20,'DelySeconds':0.5})
    empty({'Module' : 'POS14', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3+i,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS9', 'Well':'1A','SafePointOfZ':15})

mvkit('POS20','POS19')#①转移磁力架，吸附磁珠(MW1)  

report(phase = '提取', step = '第二板MW1洗涤')

mvkit('POS24','POS20') #②转移振荡器(加MW1)

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96}) #洗涤MW1②  3'20"
aspirate({'Module' : 'POS27', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
shake_on(1200,1)
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':15,'BottomOffsetOfZ':0.8,'MixOffsetOfZInLoop':0.8,'MixOffsetOfZAfterLoop':2,'PreAirVolume': (15),'MixLoopVolume': (120),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':150,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
shake_off()
aspirate({'Module' : 'POS27', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (15),'MixLoopVolume': (148),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

dely(150)

report(phase = '提取', step = '第一板MW1去废液')

load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96})   #去除MW1废液①    1'45"
for i in range(2):
    aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5), 'AspirateRateOfP':20,'DelySeconds':2})
    empty({'Module' : 'POS12', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':15,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS7', 'Well':'1A','SafePointOfZ':15})

mvkit('POS20','POS24')#②转移磁力架，吸附磁珠(MW1)

report(phase = '提取', step = '第一板MW2第一次洗涤')


mvkit('POS19','POS20')#①转移振荡器(加MW2-1)

load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96}) #洗涤MW2①-1 3'20"
aspirate({'Module' : 'POS28', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
shake_on(1200,1)
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':15,'BottomOffsetOfZ':0.8,'MixOffsetOfZInLoop':0.8,'MixOffsetOfZAfterLoop':2,'PreAirVolume': (15),'MixLoopVolume': (120),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':150,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
shake_off()
aspirate({'Module' : 'POS28', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':8,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (15),'MixLoopVolume': (148),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '提取', step = '第二板MW1去废液')


load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96})   #去除MW1废液②   1'45"
for i in range(2):
    aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5), 'AspirateRateOfP':20,'DelySeconds':2})
    empty({'Module' : 'POS14', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':15,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS9', 'Well':'1A','SafePointOfZ':15})
   
mvkit('POS20','POS19')#①转移磁力架，吸附磁珠(MW2-1)  

report(phase = '提取', step = '第二板MW2第一次洗涤')

mvkit('POS24','POS20')#②转移振荡器(加MW2-1)
load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96}) #洗涤MW2②-1       3'20"
aspirate({'Module' : 'POS29', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
shake_on(1200,1)
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':15,'BottomOffsetOfZ':0.8,'MixOffsetOfZInLoop':0.8,'MixOffsetOfZAfterLoop':2,'PreAirVolume': (15),'MixLoopVolume': (120),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':150,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
shake_off()
aspirate({'Module' : 'POS29', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':8,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (15),'MixLoopVolume': (148),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '提取', step = '第一板MW2第一次去废液')

load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96})   #①去除MW2-1废液  1'45"
for x in range(2):
    aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (160), 'PreAirVolume': (5), 'AspirateRateOfP':20,'DelySeconds':0.5})
    empty({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS7', 'Well':'1A','SafePointOfZ':15})

mvkit('POS20','POS24')#②转移磁力架，吸附磁珠(MW2-1)

report(phase = '提取', step = '第一板MW2第二次洗涤')

mvkit('POS19','POS20')#①转移振荡器(加MW2-2)

load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96}) #①洗涤MW2-2  3'20"
aspirate({'Module' : 'POS28', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
shake_on(1200,1)#shaker
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':15,'BottomOffsetOfZ':0.8,'MixOffsetOfZInLoop':0.8,'MixOffsetOfZAfterLoop':2,'PreAirVolume': (15),'MixLoopVolume': (120),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':150,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
shake_off()#shaker off
aspirate({'Module' : 'POS28', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':8,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (15),'MixLoopVolume': (148),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '提取', step = '第二板MW2第一次去废液')

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96})   #②去除MW2-1废液   1'45"
for x in range(2):
    aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (160), 'PreAirVolume': (5), 'AspirateRateOfP':20,'DelySeconds':0.5})
    empty({'Module' : 'POS13', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS9', 'Well':'1A','SafePointOfZ':15})

mvkit('POS20','POS19')#①转移磁力架，吸附磁珠(MW2-2)

mvkit('POS24','POS20')#②转移振荡器(加MW2-1)

report(phase = '提取', step = '第二板MW2第二次洗涤')

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96}) #洗涤MW2②-2
aspirate({'Module' : 'POS29', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
shake_on(1200,1)
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':15,'BottomOffsetOfZ':0.8,'MixOffsetOfZInLoop':0.8,'MixOffsetOfZAfterLoop':2,'PreAirVolume': (15),'MixLoopVolume': (120),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
shake_off()
aspirate({'Module' : 'POS29', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':8,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':5,'MixOffsetOfZAfterLoop':4,'PreAirVolume': (15),'MixLoopVolume': (148),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '提取', step = '第一板MW2第二次去废液')

load_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'Tips':96})   #①去除MW2-2废液
for x in range(2):
    aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (150), 'PreAirVolume': (5), 'AspirateRateOfP':15,'DelySeconds':0.5})
    empty({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (100), 'PreAirVolume': (5), 'AspirateRateOfP':15,'DelySeconds':0.5})
empty({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS7', 'Well':'1A','SafePointOfZ':15})

mvkit('POS20','POS24')#②转移磁力架，吸附磁珠(MW2-2)

def blockC(): 
    dely(180)
    
c = parallel_block(blockC)#①等待磁珠吸附后洗脱

jc("POS7")#丢掉M*吸头盒①
jc("POS11")#丢掉MLE废液板①
jc("POS12")#丢掉血浆废液板①

c.Wait()#①等待磁珠吸附后洗脱

report(phase = '提取', step = '第一板洗脱回溶开始')

load_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'Tips':96}) #①TE洗脱磁珠  1'
aspirate({'Module' : 'POS25', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (30), 'PreAirVolume': (5),'PostAirVolume':0,'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS19','POS20')#①转移振荡器(TE)


def blockA(): 
    shake_on(1200,1)
    dely(120)
    shake_off()
    dely(120)
    shake_on(1200,1)
    dely(40)
    shake_off()
    dely(40)
a = parallel_block(blockA)#①洗脱shaker

report(phase = '提取', step = '第二板MW2第二次去废液')

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96})   #②去除MW2-2废液  1'45"
for x in range(2):
    aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (150), 'PreAirVolume': (5), 'AspirateRateOfP':15,'DelySeconds':0.5})
    empty({'Module' : 'POS13', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})
aspirate({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (100), 'PreAirVolume': (5), 'AspirateRateOfP':15,'DelySeconds':0.5})
empty({'Module' : 'POS13', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS9', 'Well':'1A','SafePointOfZ':15})

report(phase = '提取', step = '第二板洗脱回溶开始')

def blockD(): 
    dely(120)
    
d = parallel_block(blockD)#②等待磁珠吸附后洗脱

jc("POS9")#丢掉M*吸头盒②
jc("POS13")#丢掉MLE废液板②
jc("POS14")#丢掉血浆废液板②

d.Wait()#①等待磁珠吸附后洗脱

load_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'Tips':96}) #②TE洗脱磁珠  1'
aspirate({'Module' : 'POS25', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (30), 'PreAirVolume': (5),'PostAirVolume':0,'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS24', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS4', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

a.Wait()

mvkit('POS20','POS18')#①准备转移下一工位磁力架(TE)

mvkit('POS24','POS20')#②转移振荡器(TE)


def blockB(): 
    shake_on(1200,1)
    dely(120)
    shake_off()
    dely(120)
    shake_on(1200,1)
    dely(40)
    shake_off()
    dely(40)
b = parallel_block(blockB)#②洗脱shaker

#清理台面开始

jc("POS2")#丢掉TE吸头盒①
jc("POS4")#丢掉TE吸头盒②
jc("POS25")#丢掉TE板
jc("POS26")#丢掉MW1废液板①
jc("POS27")#丢掉MW1废液板②
jc("POS28")#丢掉MW2废液板①
jc("POS29")#丢掉MW2废液板②


b.Wait()

mvkit('POS20','POS23')#②准备转移下一工位磁力架(TE)
home()
