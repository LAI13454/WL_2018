#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from spi_com import SPI_COM
from oled_display import OLED
from run import RUN
import threading
import time
import json

def run_fun():
    time_last = 0
    f = open("config.json",encoding='utf-8')
    setting = json.load(f)
    speed_set = setting["Speed"]["Set"]
    speed_ratio = setting["Speed"]["Ratio"]
    print(speed_set)

    while True:
        if (time.time()-time_last) >= 0.02:
            time_last = time.time()
            gray_data = spi_com.gray()
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
    pass

