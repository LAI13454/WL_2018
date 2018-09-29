#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from spi_com import SPI_COM
from oled_display import OLED
from run import RUN
import threading
import time

spi_com = SPI_COM()
oled = OLED()
run = RUN()
oled_thread = threading.Thread(target=oled.display)
oled_thread.start()
spi_com.motor_left(300)
spi_com.motor_right(300)
time.sleep(3)
while True:
    gray_data = spi_com.gray()
    dif = run.gray_dif(gray_data)
    turn_out = run.turn_pid(dif)
    print(turn_out)
    spi_com.steer_turn(turn_out)
    time.sleep(0.002)
