#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from spi_com import SPI_COM
from oled_display import OLED
from run import RUN
from steer_fun import STEER_FUN
import threading
import time
import json
import serial

gray_data = []          #灰度数据
gray_data_two = []
normal_walk_flag = False #正常行走标志,为真车子使用PID寻线，否则采用流程控制中的方法
normal_walk_speed_flag = False   #为假时，正常寻线，为真时，关闭舵机转向，速度改为慢档
camera_data = None
goods_data = ["ZJGXDS06","ZJGXDS08","ZJGXDS09"]


speed_l = 200
for i in range(12):
    gray_data.append(0)
def run_fun():
    global gray_data
    global gray_data_two
    global normal_walk_flag
    global normal_walk_speed_flag
    global speed_l
    time_last = 0
    f = open("config.json",encoding='utf-8')
    setting = json.load(f)
    speed_set = setting["Speed"]["Set"]
    speed_ratio = setting["Speed"]["Ratio"]
    speed_l = setting["Speed"]["Speed_L"]
    print(speed_set)
    
    while True:
        gray_data = spi_com.gray()
        gray_data_two = spi_com.gray_two()
        if (((time.time()-time_last) >= 0.02) and (normal_walk_flag == True)):    #正常行走控制语句
            time_last = time.time()
            dif = run.gray_dif(gray_data)
            turn_out = run.turn_pid(dif)
            #print("OUT:",turn_out)
            if normal_walk_speed_flag == False:   #高速挡
                spi_com.motor_left(int(speed_set+turn_out*speed_ratio))
                spi_com.motor_right(int(speed_set-turn_out*speed_ratio))
                spi_com.steer_turn(turn_out)
            else:                                 #低速挡
                spi_com.motor_left(int(speed_l+turn_out*speed_ratio*0.5))
                spi_com.motor_right(int(speed_l-turn_out*speed_ratio*0.5))

def camera_use():
    global camera_data
    ser = serial.Serial("/dev/ttyAMA0",115200)
    while True:
        try:
            data = ser.readline()
        except SerialException:
            pass
        data = str(data, encoding = "utf8") 
        #print(data)
        if len(data) > 5:
            camera_data = data[0:8]
            print(camera_data)
        else:
            camera_data = None


spi_com = SPI_COM()
oled = OLED()
run = RUN()
steer_fun = STEER_FUN()
steer_fun.steer_posture_init()
oled_thread = threading.Thread(target=oled.display)
oled_thread.start()
#run_thread = threading.Thread(target=run_fun)
#run_thread.start()
spi_com.motor_left(0)       #开机电机速度清零
spi_com.motor_right(0)
spi_com.steer_turn(0)       #开机舵机回正
run_thread = threading.Thread(target=run_fun)
run_thread.start()
camera_thread = threading.Thread(target=camera_use)
camera_thread.start()
place_start_count = 0

while True:
    walk_path_count = 0     #行走点位计数，知道自己走到哪一步，流程控制
    while True:             #当走到终点时退出循环
        if walk_path_count == 0:  #开机固定一段时间往前走,结束流程控制转为正常寻线模式
            print("STEP:"+str(walk_path_count))
            normal_walk_speed_flag = False
            normal_walk_flag = False
            spi_com.motor_left(speed_l)
            spi_com.motor_right(speed_l)
            spi_com.steer_turn(0)
            time.sleep(3)
            normal_walk_flag = True
            walk_path_count = walk_path_count + 1
        elif walk_path_count == 1:    #取物台中间两个黑线，用右侧传感器检测到，停车，进入下一步
            print("STEP:"+str(walk_path_count))
            while(not((gray_data_two[1] and gray_data_two[2]) and (gray_data_two[9] and gray_data_two[10]) and (not(gray_data_two[4] or gray_data_two[6] or gray_data_two[5])))):
                pass
            normal_walk_flag = False
            spi_com.motor_left(0)
            spi_com.motor_right(0)
            spi_com.steer_turn(0)
            time.sleep(0.5)
            walk_path_count = walk_path_count + 1
        elif walk_path_count == 2:   #倒退到取右边第一个物料点
            print("STEP:"+str(walk_path_count))
            spi_com.motor_left(int(-speed_l))
            spi_com.motor_right(int(-speed_l))
            spi_com.steer_turn(0)
            count = 0    #当右边传感器检测到第0个点为黑线时并且整条只有一个黑点时，停车
            while(not((gray_data_two[0] == 1) and count == 1)):
                count = 0
                for i in gray_data_two:
                    if(i == 1):
                        count = count + 1
            spi_com.motor_left(0)
            spi_com.motor_right(0)
            spi_com.steer_turn(0)
            walk_path_count = walk_path_count + 1
        elif walk_path_count == 3:  #夹取第一个物料
            print("STEP:"+str(walk_path_count))
            steer_fun.steer_set_val_5(900,10)
            steer_fun.steer_set_val_4(-200,10)
            steer_fun.steer_set_val_3(-700,30)
            steer_fun.steer_set_val_2(450,10)
            steer_fun.steer_set_val_1(0,10)
            while camera_data == None:
                pass
            m_data = camera_data
            for i in goods_data:
                print(i,m_data)
                if i == m_data:
                    steer_fun.steer_set_val_1(30,10)
                    steer_fun.steer_set_val_2(500,10)
                    steer_fun.steer_set_val_3(-800,10)
                    steer_fun.steer_set_val_4(-900,10)
                    steer_fun.steer_set_val_5(900,10)
                    steer_fun.steer_set_val_6(100,10)
                    print("夹取物料中")
                    #while True:
                    #    pass
                else:
                    pass
                    #walk_path_count = walk_path_count + 1
                
            time.sleep(3)
            walk_path_count = walk_path_count + 1
        elif walk_path_count == 4:   #放置第一个物料
            print("STEP:"+str(walk_path_count))
            steer_fun.steer_set_val_3(-200,50)
            steer_fun.steer_set_val_1(250,50)
            steer_fun.steer_set_val_4(350,50)
            steer_fun.steer_set_val_2(0,50)
            steer_fun.steer_set_val_3(300,50)
            steer_fun.steer_set_val_2(0,50)
            steer_fun.steer_set_val_4(1000,50)
            steer_fun.steer_set_val_3(250,30)
            steer_fun.steer_set_val_5(900,60)
            steer_fun.steer_set_val_6(900,5)
            time.sleep(4)
            walk_path_count = walk_path_count + 1
        elif walk_path_count == 5:   #到达第二个物料位
            print("STEP:"+str(walk_path_count))
            normal_walk_speed_flag = True  #调慢档开寻线
            normal_walk_flag = True
            while(not((gray_data_two[6] == 1) and (gray_data_two[7] == 1))):
                pass
            normal_walk_flag = False
            spi_com.motor_left(0)
            spi_com.motor_right(0)
            spi_com.steer_turn(0)
            walk_path_count = walk_path_count + 1
        elif walk_path_count == 6:
            print("STEP:"+str(walk_path_count))
            while True:
                pass
        
            
       
    
while True:
    #print(gray_data)
    if gray_data[6] and gray_data[9] and gray_data[11] and (not (gray_data[1] or gray_data[3])):
        place_start_count = place_start_count + 1 
        print("拿物料右标志")
    else:
        place_start_count = 0
    if place_start_count == 3:
        place_start_flag = True
        print("拿物料右标志触发")
    else:
        place_start_flag = False
    if (gray_data_two[0] == 1) and (place_start_flag == True):
    #if (gray_data_two[0] == 1):
        #run_thread.stop()
        catch_goods_place_flag = True
        print("转向标志")
    else:
        pass
    if catch_goods_place_flag == True:
        spi_com.motor_left(0)
        spi_com.motor_right(0)
        time.sleep(1)
        print("A")
        count = 0
        while(not((gray_data_two[0] == 1) and count == 1)):
            count = 0
            for i in gray_data_two:
                if(i == 1):
                    count = count + 1
            #print("Count:"+str(count)+"G:")
            #print(gray_data_two)
            spi_com.motor_left(int(-speed_l))
            spi_com.motor_right(int(-speed_l))
        spi_com.motor_left(0)
        spi_com.motor_right(0)
        steer_fun.steer_set_val_2(550,10)
        steer_fun.steer_set_val_4(-350,10)
        steer_fun.steer_set_val_1(-120,10)
        steer_fun.steer_set_val_3(-1000,10)
        while True:
            pass
    time.sleep(0.02)

