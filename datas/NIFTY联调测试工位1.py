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
# pos_type_map = {"POS1":["useless",None,None],"POS2":["GETP01",None,None],"POS3":["useless",None,None],"POS4":["GETP01",None,None],"POS5":["useless",None,None],
                # "POS6":["useless",None,None],"POS7":["GETP01",None,None],"POS8":["useless",None,None],"POS9":["GETP01",None,None],"POS10":["useless",None,None],
                # "POS11":["BGLE01",None,None],"POS12":["BGSP15",None,None],"POS13":["BGLE01",None,None],"POS14":["BGSP15",None,None],"POS15":[None,None,None],
                # "POS16":[None,None,None],"POS17":[None,None,None],"POS18":["BGBD01",None,None],"POS19":[None,None,None],"POS20":[None,None,"shake"],
                # "POS21":[None,None,None],"POS22":[None,None,None],"POS23":["BGBD01",None,None],"POS24":[None,None,None],"POS25":["BGTE01",None,None],
                # "POS26":["BGW101",None,None],"POS27":["BGW101",None,None],"POS28":["BGW201",None,None],"POS29":["BGW201",None,None],"POS30":[None,None,None],
                # "POS31":[None,None,None],"POS32":[None,None,None],"POS33":[None,None,None],"POS34":[None,None,None],"POS35":[None,None,"trash"],
                # "POS36":[None,None,None],"POS37":[None,None,None],"POS38":[None,None,None],"POS39":[None,None,None],"POS40":[None,None,None]}
# binding_map(pos_type_map) 

"""
不要修改HEAD
第一次调试修改时间-20180910，全程1h46'
"""

home()

report(phase = '提取', step = '第一板MLE裂解开始')


report(phase = '提取', step = '第二板MLE裂解开始')

mvkit('POS18','POS19') #①转移磁力架，吸附磁珠   20"+10"

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96})   #②中间混匀血浆第四次    2'35"
mix({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':16,'MixOffsetOfZAfterLoop':15,'PreAirVolume': (10),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':10,"SecondRouteRate": 38.0})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS23','POS24') #②转移磁力架，吸附磁珠   20"+10"

report(phase = '提取', step = '第一板MLE去废液')

load_tips({'Module' : 'POS7', 'Col' :1, 'Row' : 1,'Tips':96})  #转移①废液（MLE）  3'
unload_tips({'Module' : 'POS7', 'Well':'1A','SafePointOfZ':15})

report(phase = '提取', step = '第一板MW1洗涤')

mvkit('POS19','POS20') #①转移振荡器(加MW1) 20"+10"

report(phase = '提取', step = '第二板MLE去废液')


mvkit('POS20','POS19')#①转移磁力架，吸附磁珠(MW1)  

report(phase = '提取', step = '第二板MW1洗涤')

mvkit('POS24','POS20') #②转移振荡器(加MW1)

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96}) #洗涤MW1②  3'20"
aspirate({'Module' : 'POS27', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS20','POS24')#②转移磁力架，吸附磁珠(MW1)

report(phase = '提取', step = '第一板MW2第一次洗涤')

mvkit('POS19','POS20')#①转移振荡器(加MW2-1)

report(phase = '提取', step = '第二板MW1去废液')
   
mvkit('POS20','POS19')#①转移磁力架，吸附磁珠(MW2-1)  

report(phase = '提取', step = '第二板MW2第一次洗涤')

mvkit('POS24','POS20')#②转移振荡器(加MW2-1)

load_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'Tips':96}) #洗涤MW2②-1       3'20"
aspirate({'Module' : 'POS29', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS9', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

report(phase = '提取', step = '第一板MW2第一次去废液')

mvkit('POS20','POS24')#②转移磁力架，吸附磁珠(MW2-1)

report(phase = '提取', step = '第一板MW2第二次洗涤')

mvkit('POS19','POS20')#①转移振荡器(加MW2-2)

report(phase = '提取', step = '第二板MW2第一次去废液')

mvkit('POS20','POS19')#①转移磁力架，吸附磁珠(MW2-2)

mvkit('POS24','POS20')#②转移振荡器(加MW2-1)

report(phase = '提取', step = '第一板MW2第二次去废液')

mvkit('POS20','POS24')#②转移磁力架，吸附磁珠(MW2-2)


report(phase = '提取', step = '第一板洗脱回溶开始')

load_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'Tips':96}) #①TE洗脱磁珠  1'
aspirate({'Module' : 'POS25', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (30), 'PreAirVolume': (5),'PostAirVolume':0,'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS19','POS20')#①转移振荡器(TE)

report(phase = '提取', step = '第二板洗脱回溶开始')


mvkit('POS20','POS18')#①准备转移下一工位磁力架(TE)

mvkit('POS24','POS20')#②转移振荡器(TE)

#清理台面开始
jc("POS12")
jc("POS14")

mvkit('POS20','POS23')#②准备转移下一工位磁力架(TE)

home()
