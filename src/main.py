#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from spi_com import SPI_COM
from oled_display import OLED
from run import RUN
import threading
import time
import json

gray_data = []          #灰度数据
catch_goods_place_flag = False
for i in range(12):
    gray_data.append(0)
def run_fun():
    global gray_data
    global catch_goods_place_flag
    time_last = 0
    f = open("config.json",encoding='utf-8')
    setting = json.load(f)
    speed_set = setting["Speed"]["Set"]
    speed_ratio = setting["Speed"]["Ratio"]
    print(speed_set)
    
    while True:
        gray_data = spi_com.gray()
        if ((time.time()-time_last) >= 0.02) and (catch_goods_place_flag == False):
            time_last = time.time()
            dif = run.gray_dif(gray_data)
            turn_out = run.turn_pid(dif)
            #print("OUT:",turn_out)
            spi_com.motor_left(int(speed_set+turn_out*speed_ratio))
            spi_com.motor_right(int(speed_set-turn_out*speed_ratio))
            spi_com.steer_turn(turn_out)
        else:
            pass

spi_com = SPI_COM()
oled = OLED()
run = RUN()
oled_thread = threading.Thread(target=oled.display)
oled_thread.start()
run_thread = threading.Thread(target=run_fun)
run_thread.start()
spi_com.motor_left(300)
spi_com.motor_right(300)
time.sleep(3)
while True:
    #print(gray_data)
    if(gray_data[7] and gray_data[9] and gray_data[11]):
        #run_thread.stop()
        catch_goods_place_flag = True
        spi_com.motor_right(800)
        spi_com.motor_left(-800)
        spi_com.steer_turn(-500)
        time.sleep(3)
        spi_com.motor(0)
        print("转向标志")
    else:
        pass
    time.sleep(0.02)

