#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from spi_com import SPI_COM
from oled_display import OLED
from run import RUN
from steer_fun import STEER_FUN
import threading
import time
import json

gray_data = []          #灰度数据
gray_data_two = []
catch_goods_place_flag = False
speed_l = 200
for i in range(12):
    gray_data.append(0)
def run_fun():
    global gray_data
    global gray_data_two
    global catch_goods_place_flag
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
        if ((time.time()-time_last) >= 0.02) and (catch_goods_place_flag == False):
            time_last = time.time()
            dif = run.gray_dif(gray_data)
            turn_out = run.turn_pid(dif)
            #print("OUT:",turn_out)
            spi_com.motor_left(int(speed_set+turn_out*speed_ratio))
            spi_com.motor_right(int(speed_set-turn_out*speed_ratio))
            spi_com.steer_turn(turn_out)
        elif catch_goods_place_flag == True:
            #spi_com.motor_left(0)
            #spi_com.motor_right(0)
            pass

spi_com = SPI_COM()
oled = OLED()
run = RUN()
steer_fun = STEER_FUN()
steer_fun.steer_posture_init()
oled_thread = threading.Thread(target=oled.display)
oled_thread.start()
#run_thread = threading.Thread(target=run_fun)
#run_thread.start()
spi_com.motor_left(300)
spi_com.motor_right(300)
time.sleep(2)
run_thread = threading.Thread(target=run_fun)
run_thread.start()
time.sleep(3)
place_start_count = 0
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

