#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from spi_com import SPI_COM
from oled_display import OLED
import threading

spi_com = SPI_COM()
oled = OLED()
oled_thread = threading.Thread(target=oled.display)
oled_thread.start()
while True:
    pass
