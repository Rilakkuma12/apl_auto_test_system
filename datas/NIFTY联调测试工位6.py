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
# pos_type_map = {"POS1":["useless",None,None],"POS2":["BRMW01",None,None],"POS3":["PCRMGILIDHOLD","PCRMGILID",None],"POS4":["GETP01",None,None],
                # "POS5":[None,None,None],"POS6":[None,None,None],"POS7":["DNDW01",None,None],"POS8":[None,None,"trash"],
                # "POS9":["BGMX02",None,None],"POS10":[None,None,None],"POS11":["BRMW01",None,None],"POS12":[None,None,None]}            
# binding_map(pos_type_map) 

"""
不要修改HEAD
"""
##2019.7.9-by 赵桂丽
#胶垫抓取
#需要根据不同样本量确定不同试剂在POS13的孔位置以及总用体积，每孔分装，减少单吸头换板的步骤，splint buffer和酶混合，混合酶1、2分装，计算损耗
#####吸头用不完怎么处理 下料。pos13试剂分装的孔的位置，每个试剂单独一列，按每孔样本分装。是否加入穿刺的封膜的动作？？和贴壁穿刺加宽孔的动作？？？
##2019.7.12-by 赵桂丽
##修改板位，换成12个模块的板位
#####需要添加的东西：不需要转移最终DNB样本，可以一直用在POS2PCR仪位置的PCR板，分两列隔开，是否可以在LIMS上标注DNB产物？
#######需要实现：是否pooling的输入样本深孔板放在POS10的温控上？需要保存pooling样本，需要下料封膜回冰箱，而不是直接扔掉#########


home()
# c1_home()
# c2_home()

# c1_in()
# c2_in()

# img('Splint+makeDNB.jpg')

def PCR_time(value): ##同一步骤根据不同情况可选择不同的PCR反应温度和时间
    if(value == 15):
        pcr_run_methods(method = '30-15min')
    elif(value == 20):
        pcr_run_methods(method = '30-20min')
    elif(value == 25):
        pcr_run_methods(method = '30-25min')
    else:
        raise ValueError('value must be 15 or 20 or 25')

# paramters = require({'SampleNum':'','RCA_PCR_time':''})

SampleNum=8##此脚本中固定样本数量为8
RCA_PCR_time=20##此脚本中选择30度20min的固定时间

attempts = 0
success = False

#######是否运行？？？
# while attempts < 3 and not success:
    # try :
        # SampleNum = int(paramters['SampleNum'])
        # RCA_PCR_time = int(paramters['RCA_PCR_time'])
        # if SampleNum < 1 or SampleNum > 7:
            # raise ValueError('SampleNum Need in range [1,7]')
        # if RCA_PCR_time != 15 and RCA_PCR_time != 20 and RCA_PCR_time != 25: 
            # raise ValueError('Value must be 15 or 20 or 25')	
        # success = True 
    # except Exception as e:
        # dialog('Input value  can\'t be accept')
        # attempts += 1
        # if attempts==3:
            # sys.exit(0) 
        # paramters = require({'SampleNum':'','RCA_PCR_time':''})
        

    
def blockA():
    temp_a(4)
    
# def blockB(): 
    # pcr_open_door()
    # pcr_run_methods(method = 'START') 
   	
a = parallel_block(blockA) #并行开启温控
# b = parallel_block(blockB) #PCR已经开始...正在执行 



##吸取样本，单个吸头还是按照样本数量定吸头数量的逻辑
load_tips({'Module' : 'POS4', 'Col' : 12, 'Row' : 9-SampleNum,'Tips':SampleNum}) 
aspirate({'Module' : 'POS7', 'Col' :1, 'Row' : 1, 'AspirateVolume':(48),'BottomOffsetOfZ':0.3,'PreAirVolume':(5),'PostAirVolume':(0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS2', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS4', 'Col' : 12, 'Row' : 9-SampleNum,'Tips':SampleNum})

a.Wait()
# b.Wait()	

# mvkit('POS3','POS2')#连接前PCR加lid
# pcr_close_door()
# pcr_run_methods(method = 'single95-5min')  #单链分离95°5min，4°2min
# pcr_open_door() 
# mvkit('POS2','POS3')#连接后PCR去lid

#####pos13试剂按照样本数量分装，一个孔对应一个样本，省去单吸头分试剂，加入穿刺的封膜的动作
   
load_tips({'Module' : 'POS4', 'Col' : 11, 'Row' : 9-SampleNum,'Tips':SampleNum})  #MIX加入PCR产物样本（保证反应时间相同） 环化，总体积60ul
aspirate({'Module':'POS9', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':0.3,'AspirateVolume':(12.1), 'PreAirVolume':(5),'PostAirVolume':(0), 'AspirateRateOfP':20,'DelySeconds':2})
empty({'Module' : 'POS2', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':4,'DispenseRateOfP':20,'DelySeconds':0.5})
unload_tips({'Module' : 'POS4', 'Col' : 11, 'Row' : 9-SampleNum,'Tips':SampleNum})

# pcr_stop_heating()
# mvkit('POS3','POS2')#连接前PCR加lid
# pcr_close_door()
# pcr_run_methods(method = '37-30min')
# pcr_open_door()
# mvkit('POS2','POS3')#连接后PCR去lid

report(phase = '制备DNB', step = '加入制备缓冲液（1/4）')


load_tips({'Module' : 'POS4', 'Col' : 10, 'Row' : 9-SampleNum,'Tips':SampleNum}) ###只吸取20ul样本，直接在POS13试剂板吸取试剂加到样本，共40ul
aspirate({'Module':'POS9', 'Col' :2, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume':(20), 'PreAirVolume':(5),'PostAirVolume':(0), 'AspirateRateOfP':20,'DelySeconds':2})
empty({'Module' : 'POS2', 'Col' :2, 'Row' : 1,'BottomOffsetOfZ':3,'DispenseRateOfP':10,'DelySeconds':2})
unload_tips({'Module' : 'POS4', 'Col' : 10, 'Row' : 9-SampleNum,'Tips':SampleNum})

# mvkit('POS3','POS2')#连接前PCR加lid
# pcr_close_door()
# pcr_run_methods(method = 'DNB')###此反应时不加入DNB聚合酶，先反应3min
# pcr_open_door()
# mvkit('POS2','POS3')#连接后PCR去lid

report(phase = '制备DNB', step = '加入DNB聚合酶（2/4）')



load_tips({'Module':'POS4','Col' : 9, 'Row' : 9-SampleNum,'Tips':SampleNum})  #吸取聚合酶1到聚合酶2中混合，再吸取44ul加到样本中，共84ul
aspirate({'Module' : 'POS9', 'Col' : 4, 'Row' : 1,'BottomOffsetOfZ':0.5,'AspirateVolume':(44), 'PreAirVolume':(10),'PostAirVolume':(0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' :'POS2', 'Col' : 2, 'Row' : 1,'BottomOffsetOfZ':6,'DispenseRateOfP':10,'DelySeconds':0.5})
unload_tips({'Module':'POS4','Col' : 9, 'Row' : 9-SampleNum,'Tips':SampleNum})


report(phase = '制备DNB', step = '制备纳米球（3/4）')

# mvkit('POS3','POS2')#连接前PCR加lid
# pcr_close_door()
# PCR_time(RCA_PCR_time)
# pcr_open_door()
# mvkit('POS2','POS3')#连接后PCR去lid

report(phase = '制备DNB', step = '停止反应（4/4）')


temp_sleep_a()



load_tips({'Module' : 'POS4', 'Col' : 7,'Row' : 9-SampleNum,'Tips':SampleNum}) 
aspirate({'Module' : 'POS2', 'Col' : 2, 'Row' : 1, 'AspirateVolume':(102),'BottomOffsetOfZ':0.5, 'PreAirVolume':(10),'PostAirVolume':(0),'AspirateRateOfP':10,'DelySeconds':0.5})
empty({'Module' : 'POS11', 'Col' :1, 'Row' : 1,'BottomOffsetOfZ':5,'DispenseRateOfP':10,'DelySeconds':0.5})
unload_tips({'Module' : 'POS4', 'Col' : 7,'Row' : 9-SampleNum,'Tips':SampleNum})
    

	
####剩下的吸头是下料
# c1_out()
# c2_out()


jc("POS2")


# pcr_stop_heating()
home()