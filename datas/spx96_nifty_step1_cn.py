# -*- coding: utf-8 -*-
"""
***Spx head example***
wangjian5@genomics.cn
jjseen@163.com
"""
#region pos and kit type mapping table
#three write methods:empty-None; pcr-"pcr"; kit-"kit" ;cannot grasp/loose-"useless"  shake-([,"shake"])
pos_type_map = {"POS1":"useless","POS2":"useless","POS3":"useless","POS4":"useless","POS5":"useless","POS6":"useless","POS7":"useless","POS8":"useless","POS9":"useless","POS10":"useless",
                "POS11":"PCRBioRadHSP9601","POS12":"PCRBioRadHSP9601","POS13":"DeepwellPlateDT7350504","POS14":"DeepwellPlateDT7350504","POS15":"PCRBioRadHSP9601","POS16":None,
                "POS17":"DeepwellPlateDT7350504","POS18":"DeepwellPlateDT7350504","POS19":None,"POS20":["DeepwellPlateDT7350504","shake"],"POS21":"DeepwellPlateDT7350504",
                "POS22":"DeepwellPlateDT7350504","POS23":"DeepwellPlateDT7350504","POS24":"useless"}

#region HEAD
spx96 = globals().get("Spx96")

#simplest way 
from head import *
#init
init(spx96) #most important
binding_map(pos_type_map)

shake.binding(spx96)


"""
不要修改HEAD
"""


#20180503修改脚本 屏蔽PCR空跑脚本无bug。by赵鑫2：44：00


report(phase = '提取', step = '（1/4）裂解')

pcr_close_door()

load_tips({'Module' : 'POS5', 'Well':'1A','Tips':8})  #单列分配提取磁珠
# mix({'Module' : 'POS21', 'Well':'1A','SubMixLoopCounts':15,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':6,'MixOffsetOfZAfterLoop':6,'PreAirVolume': (20),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (20),'MixLoopAspirateRate':250,'MixLoopDispenseRate':250,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':2,"SecondRouteRate": 80.0,'Tips':8})
# for x in range(12):   
    # mix({'Module' : 'POS21', 'Well':'1A','SubMixLoopCounts':2,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':6-0.5*x,'MixOffsetOfZAfterLoop':6-0.5*x,'PreAirVolume': (10),'MixLoopVolume': (150-11*x),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':200,'MixLoopDispenseRate':100,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':2,"SecondRouteRate": 80.0,'Tips':8})
    # aspirate({'Module' : 'POS21', 'Well':'1A','BottomOffsetOfZ':3.6-x*0.3,'AspirateVolume': (14), 'PreAirVolume': (10),'PostAirVolume':2, 'AspirateRateOfP':50,'DelySeconds':0.5,'Tips':8})
    # empty({'Module' : 'POS20', 'Col' : 1+x, 'Row' : 1,'BottomOffsetOfZ':1,'DispenseRateOfP':20,'DelySeconds':0.5,'Tips':8})
unload_tips({'Module' : 'POS24', 'Well':'1A'})


load_tips({'Module':'POS5', 'Well':'2A','Tips':8})   #单列分配蛋白酶K
for x in range(12): 
    aspirate({'Module':'POS21','Well':'2A','BottomOffsetOfZ':0.3,'AspirateVolume': (10), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':10,'DelySeconds':0.5,'Tips':8})
    empty({'Module' : 'POS20', 'Col' : 1+x, 'Row' : 1,'BottomOffsetOfZ':0.5,'DispenseRateOfP':20,'DelySeconds':0.5,'Tips':8})
unload_tips({'Module' : 'POS24', 'Well':'1A'})  


load_tips({'Module' : 'POS1', 'Col' : 1, 'Row' : 1,'Tips':96})   #吸取血浆    
for i in range(2):      
    aspirate({'Module' : 'POS23', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (100), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
    empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':3+2*i,'MixOffsetOfZAfterLoop':3+2*i,'PreAirVolume': (15),'MixLoopVolume': (80),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
    ,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 80.0})
   
for i in range(2):     #吸取MLE   
    aspirate({'Module' : 'POS14', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (140), 'PreAirVolume': (7),'PostAirVolume': (3), 'AspirateRateOfP':50,'DelySeconds':0.5})
    empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':5})
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':15,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':8,'MixOffsetOfZAfterLoop':8,'PreAirVolume': (15),'MixLoopVolume': (130),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':5,"SecondRouteRate": 80.0})
unload_tips({'Module' : 'POS1', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

for i in range(4):    #15分钟
    dely(60)	
    load_tips({'Module' : 'POS1', 'Col' : 1, 'Row' : 1,'Tips':96})       #中间混匀血浆
    mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':30,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':12,'MixOffsetOfZAfterLoop':10,'PreAirVolume': (10),'MixLoopVolume': (130),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
        ,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 80.0})
    unload_tips({'Module' : 'POS1', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})


mvkit('POS20','POS19') 
dely(400)


load_tips({'Module' : 'POS1', 'Col' :1, 'Row' : 1,'Tips':96})  #转移废液系  2分钟
for i in range(4):
    aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3.5-i,'AspirateVolume': (120), 'PreAirVolume': (7),'PostAirVolume': (3), 'AspirateRateOfP':20,'DelySeconds':0.5})
    empty({'Module' : 'POS14', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3+i,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS1', 'Well':'1A','SafePointOfZ':15})

mvkit('POS19','POS20') 

report(phase = '提取', step = '（2/4）MW1洗涤')

load_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'Tips':96}) #洗涤MW1   3分
aspirate({'Module' : 'POS18', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (150), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
shake_on(1000,1)#shaker
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':15,'BottomOffsetOfZ':1.5,'MixOffsetOfZInLoop':2,'MixOffsetOfZAfterLoop':2,'PreAirVolume': (15),'MixLoopVolume': (100),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':150,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
shake_off()#shaker off
aspirate({'Module' : 'POS18', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (150), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':7,'MixOffsetOfZAfterLoop':5,'PreAirVolume': (15),'MixLoopVolume': (148),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
unload_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS20','POS19')#抓手  
dely(120)


load_tips({'Module' : 'POS2', 'Col' : 1, 'Row' : 1,'Tips':96})   #去除MW1   1分
for i in range(2):
    aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (160), 'PreAirVolume': (5), 'AspirateRateOfP':20,'DelySeconds':2})
    empty({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})
unload_tips({'Module' : 'POS2', 'Well':'1A','SafePointOfZ':15})

report(phase = '提取', step = '（3/4）MW2洗涤')

def blockC(): 
    pcr_run_methods(method = 'START')
    pcr_run_methods(method = '25-4')
c = parallel_block(blockC) #PCR已经开始...正在执行
 
for i in range(2):     #17分钟
    mvkit('POS19','POS20')#抓手
    load_tips({'Module' : 'POS%d'%(3+i), 'Col' : 1, 'Row' : 1,'Tips':96}) #洗涤MW2
    aspirate({'Module' : 'POS17', 'Well':'1A','BottomOffsetOfZ':1,'AspirateVolume': (150), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
    empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
    shake_on(1200,1)#shaker#shaker
    mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':20,'BottomOffsetOfZ':1.5,'MixOffsetOfZInLoop':2,'MixOffsetOfZAfterLoop':2,'PreAirVolume': (15),'MixLoopVolume': (100),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':150,'MixLoopDispenseRate':150
    ,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
    shake_off()#shaker off#shaker off
    aspirate({'Module' : 'POS17', 'Well':'1A','BottomOffsetOfZ':1,'AspirateVolume': (150), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5})
    empty({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
    mix({'Module' : 'POS20', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':7,'MixOffsetOfZAfterLoop':5,'PreAirVolume': (15),'MixLoopVolume': (148),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':200,'MixLoopDispenseRate':150
     ,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
    unload_tips({'Module' : 'POS%d'%(3+i), 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})
   
    mvkit('POS20','POS19')#抓手  
    dely(120)
    load_tips({'Module' : 'POS%d'%(3+i), 'Col' : 1, 'Row' : 1,'Tips':96})   #去除MW2
    for x in range(2):
        aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0,'AspirateVolume': (160), 'PreAirVolume': (5), 'AspirateRateOfP':20,'DelySeconds':0.5})
        empty({'Module' : 'POS18', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':50,'DelySeconds':0.5})
    unload_tips({'Module' : 'POS%d'%(3+i), 'Well':'1A','SafePointOfZ':15})
	

dely(180)

report(phase = '提取', step = '（4/4）DNA洗脱')



load_tips({'Module' : 'POS6', 'Col' : 1, 'Row' : 1,'Tips':96}) #洗脱磁珠  1′
aspirate({'Module' : 'POS22', 'Well':'1A','BottomOffsetOfZ':0.5,'AspirateVolume': (40), 'PreAirVolume': (5),'PostAirVolume':0,'AspirateRateOfP':50,'DelySeconds':0.5})
empty({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS6', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

mvkit('POS19','POS20')#抓手
shake_on(1200,1)#shaker

report(phase = '末端修复', step = '（1/3）配置反应液')

load_tips({'Module':'POS5','Well':'3A','Tips':8})#配置mix1   4分
aspirate({'Module':'POS21','Well':'3A','BottomOffsetOfZ':0.3,'AspirateVolume': (131.6), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':50,'DelySeconds':0.5,'Tips':8})
empty({'Module' : 'POS21', 'Well':'4A','BottomOffsetOfZ':1,'DispenseRateOfP':20,'DelySeconds':0.5,'Tips':8})
mix({'Module' : 'POS21', 'Well':'4A','SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':3,'MixOffsetOfZAfterLoop':3,'PreAirVolume': (10),'MixLoopVolume': (120),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':5,"SecondRouteRate": 80.0,'Tips':8})
unload_tips({'Module' : 'POS24', 'Well':'1A'})

shake_off()

c.Wait()

pcr_open_door()

def blockA(): 
    dely(150)
    shake_on(1200,1)
    dely(60)
    shake_off()
	
a = parallel_block(blockA) #PCR已经开始...正在执行

load_tips({'Module':'POS5',  'Well':'4A','Tips':8})   #分配mix1
for x in range(12): 
    aspirate({'Module':'POS21','Well':'4A','BottomOffsetOfZ':0.3,'AspirateVolume': (10), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':10,'DelySeconds':0.5,'Tips':8})
    empty({'Module' : 'POS11', 'Col' : 1+x, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':20,'DelySeconds':0.5,'Tips':8})
unload_tips({'Module' : 'POS24', 'Well':'1A'})   

report(phase = '末端修复', step = '（2/3）混匀反应体系')

a.Wait()

mvkit('POS20','POS19')#抓手


dely(180)

dialog('请加入阴阳对照品')

load_tips({'Module' : 'POS6', 'Col' : 1, 'Row' : 1,'Tips':96}) #吸取洗脱DNA   
aspirate({'Module' : 'POS19', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (40), 'PreAirVolume': (5),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS11', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':50,'DelySeconds':0.5})
mix({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':6,'MixOffsetOfZAfterLoop':6,'PreAirVolume': (10),'MixLoopVolume': (40),'DispenseVolumeAfterSubmixLoop': (10),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2})
unload_tips({'Module' : 'POS6', 'Well':'1A','SafePointOfZ':15})
 
report(phase = '末端修复', step = '（3/3）进行酶反应')

pcr_close_door()
pcr_run_methods(method = 'Nifty_ER') #末端修复反应    

report(phase = '接头连接', step = '（1/3）配置反应液')

load_tips({'Module':'POS5', 'Well':'5A','Tips':8})   #配置mix2  3′
for i in range(3):
    aspirate({'Module':'POS21', 'Well':'5A','BottomOffsetOfZ':2.3-i,'AspirateVolume': (112), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':20,'DelySeconds':5,'Tips':8})
    empty({'Module': 'POS21', 'Well':'6A','BottomOffsetOfZ':1+i,'DispenseRateOfP':10,'DelySeconds':5,'Tips':8})
mix({'Module' : 'POS21', 'Well':'6A','SubMixLoopCounts':15,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':7,'MixOffsetOfZAfterLoop':7,'PreAirVolume': (15),'MixLoopVolume': (140),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':100,'MixLoopDispenseRate':50
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':10,"SecondRouteRate": 80.0,'Tips':8})
unload_tips({'Module' : 'POS24', 'Well':'1A'}) 	

load_tips({'Module':'POS5','Well':'6A','Tips':8})   #分配mix2  5′
for x in range(12): 
    aspirate({'Module':'POS21', 'Well':'6A','BottomOffsetOfZ':5.8-0.5*x,'AspirateVolume': (25), 'PreAirVolume': (5),'PostAirVolume': (2), 'AspirateRateOfP':20,'DelySeconds':2,'Tips':8})
    empty({'Module' : 'POS15', 'Col' : 1+x, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':10,'DelySeconds':0.5,'Tips':8})
unload_tips({'Module' : 'POS24', 'Well':'1A'})

pcr_open_door()

report(phase = '接头连接', step = '（2/3）混匀反应体系')

# load_tips({'Module':'POS7','Col':1,'Row':1,'Tips':96})  #混合BC、连接mix和样品   2′
# aspirate({'Module' : 'POS12', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (5), 'PreAirVolume': (5),'PostAirVolume': (2),'AspirateRateOfP':20,'DelySeconds':0.5})
# empty({'Module' : 'POS11', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':10,'DelySeconds':1})
# aspirate({'Module' : 'POS15', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (27), 'PreAirVolume': (10),'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
# empty({'Module' : 'POS11', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':6,'DispenseRateOfP':20,'DelySeconds':0.5})
# mix({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':7,'MixOffsetOfZAfterLoop':7,'PreAirVolume': (15),'MixLoopVolume': (60),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
# ,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 80.0})
# unload_tips({'Module' : 'POS7', 'Col' : 1, 'Row' : 1,'SafePointOfZ':15})

load_tips({'Module':'POS7','Col':7,'Row':1,'Tips':96})  #混合BC、连接mix和样品   2′
aspirate({'Module' : 'POS12', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (5), 'PreAirVolume': (5),'PostAirVolume': (2),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS11', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':10,'DelySeconds':1})
aspirate({'Module' : 'POS15', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (27), 'PreAirVolume': (10),'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS11', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':6,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS11', 'Col' : 1, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':7,'MixOffsetOfZAfterLoop':7,'PreAirVolume': (15),'MixLoopVolume': (60),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 80.0})
unload_tips({'Module' : 'POS24', 'Well':'1A'})

load_tips({'Module':'POS7','Col':1,'Row':1,'Tips':96})  #混合BC、连接mix和样品   2′
aspirate({'Module' : 'POS12', 'Col' : 1, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume': (5), 'PreAirVolume': (5),'PostAirVolume': (2),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS11', 'Col' :7, 'Row' : 1,'BottomOffsetOfZ':2,'DispenseRateOfP':10,'DelySeconds':1})
aspirate({'Module' : 'POS15', 'Col' : 7, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume': (27), 'PreAirVolume': (10),'PostAirVolume': (0),'AspirateRateOfP':20,'DelySeconds':0.5})
empty({'Module' : 'POS11', 'Col' :7, 'Row' : 1,'BottomOffsetOfZ':6,'DispenseRateOfP':20,'DelySeconds':0.5})
mix({'Module' : 'POS11', 'Col' : 7, 'Row' : 1,'SubMixLoopCounts':10,'BottomOffsetOfZ':1,'MixOffsetOfZInLoop':7,'MixOffsetOfZAfterLoop':7,'PreAirVolume': (15),'MixLoopVolume': (60),'DispenseVolumeAfterSubmixLoop': (15),'MixLoopAspirateRate':100,'MixLoopDispenseRate':100
,'DispenseRateAfterSubmixLoop':20,'SubMixLoopCompletedDely':2,"SecondRouteRate": 80.0})
unload_tips({'Module' : 'POS24', 'Well':'1A'})  

report(phase = '接头连接', step = '（3/3）进行酶反应')

def blockD():      
    pcr_close_door()
    pcr_run_methods(method = 'Nifty_Ad Ligation')
d = parallel_block(blockD) #PCR已经开始...正在执行

mvkit('POS13','POS20')
mvkit('POS19','POS13')

load_tips({'Module' : 'POS5', 'Well':'7A','Tips':8})    #单通道分配纯化磁珠
mix({'Module': 'POS21', 'Well':'9A','SubMixLoopCounts':10,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':1,'MixOffsetOfZAfterLoop':10,'PreAirVolume': (20),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (20),'MixLoopAspirateRate':250,'MixLoopDispenseRate':250
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':5,"SecondRouteRate": 80.0,'Tips':8})
mix({'Module': 'POS21', 'Well':'9A','SubMixLoopCounts':25,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':10,'MixOffsetOfZAfterLoop':10,'PreAirVolume': (20),'MixLoopVolume': (150),'DispenseVolumeAfterSubmixLoop': (20),'MixLoopAspirateRate':250,'MixLoopDispenseRate':250
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':5,"SecondRouteRate": 80.0,'Tips':8})
for x in range(4):   
    mix({'Module': 'POS21', 'Well':'9A','SubMixLoopCounts':5,'BottomOffsetOfZ':0.5,'MixOffsetOfZInLoop':10-3*x,'MixOffsetOfZAfterLoop':10-3*x,'PreAirVolume': (20),'MixLoopVolume': (100),'DispenseVolumeAfterSubmixLoop': (20),'MixLoopAspirateRate':200,'MixLoopDispenseRate':200
    ,'DispenseRateAfterSubmixLoop':10,'SubMixLoopCompletedDely':5,"SecondRouteRate": 80.0,'Tips':8})
    aspirate({'Module' :'POS21', 'Well':'9A','BottomOffsetOfZ':0.5,'AspirateVolume': (130), 'PreAirVolume': (5),'PostAirVolume': (0), 'AspirateRateOfP':50,'DelySeconds':0.5,'Tips':8})
    dispense({'Module' : 'POS21', 'Well':'9A','BottomOffsetOfZ':10-3*x,'DispenseVolume': (5),'DispenseRateOfP':20,'DelySeconds':0.5,'Tips':8})
    for i in range(3):	 
        dispense({'Module' : 'POS20', 'Col' : 1+i+3*x, 'Row' : 1,'BottomOffsetOfZ':0.5,'DispenseVolume': (40),'DispenseRateOfP':20,'DelySeconds':0.5,'Tips':8})
    empty({'Module' : 'POS21', 'Well':'9A','BottomOffsetOfZ':10-3*x,'DispenseRateOfP':20,'DelySeconds':0.5,'Tips':8})
unload_tips({'Module' : 'POS24', 'Well':'1A'})

home()

d.Wait()


