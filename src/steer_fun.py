from spi_com import SPI_COM
import json
import time
class STEER_FUN:
    def __init__(self):
        self.spi_com = SPI_COM()
        f = open("config.json",encoding='utf-8')
        setting = json.load(f)
        self.steer_val_1 = setting["Steer_DEF"]["1"]
        self.steer_val_2 = setting["Steer_DEF"]["2"]
        self.steer_val_3 = setting["Steer_DEF"]["3"]
        self.steer_val_4 = setting["Steer_DEF"]["4"]
        self.steer_val_5 = setting["Steer_DEF"]["5"]
        self.steer_val_6 = setting["Steer_DEF"]["6"]
        self.steer_speed = setting["Steer_DEF"]["Speed"] 
    def steer_posture_init(self):
        self.spi_com.steer_1(self.steer_val_1)		
        self.spi_com.steer_2(self.steer_val_2)		
        self.spi_com.steer_3(self.steer_val_3)		
        self.spi_com.steer_4(self.steer_val_4)		
        self.spi_com.steer_5(self.steer_val_5)		
        self.spi_com.steer_6(self.steer_val_6)	
    def steer_set_val_1(self,val,time_val):
        if val < self.steer_val_1:
            l = list(range(self.steer_val_1,val,-10))
            l.append(val)
        else:
            l = list(range(self.steer_val_1,val,10))
            l.append(val)
        for i in l:
            self.spi_com.steer_1(i)
            time.sleep(time_val * self.steer_speed)
        self.steer_val_1 = val
    def steer_set_val_2(self,val,time_val):
        if val < self.steer_val_2:
            l = list(range(self.steer_val_2,val,-10))
            l.append(val)
        else:
            l = list(range(self.steer_val_2,val,10))
            l.append(val)
        for i in l:
            self.spi_com.steer_2(i)
            time.sleep(time_val * self.steer_speed)
        self.steer_val_2 = val 
    def steer_set_val_3(self,val,time_val):
        if val < self.steer_val_1:
            l = list(range(self.steer_val_3,val,-10))
            l.append(val)
        else:
            l = list(range(self.steer_val_3,val,10))
            l.append(val)
        for i in l:
            self.spi_com.steer_3(i)
            time.sleep(time_val * self.steer_speed)
        self.steer_val_3 = val
    def steer_set_val_4(self,val,time_val):
        if val < self.steer_val_4:
            l = list(range(self.steer_val_4,val,-10))
            l.append(val)
        else:
            l = list(range(self.steer_val_4,val,10))
            l.append(val)
        for i in l:
            self.spi_com.steer_4(i)
            time.sleep(time_val * self.steer_speed)
        self.steer_val_4 = val
    def steer_set_val_5(self,val,time_val):
        if val < self.steer_val_5:
            l = list(range(self.steer_val_5,val,-10))
            l.append(val)
        else:
            l = list(range(self.steer_val_5,val,10))
            l.append(val)
        for i in l:
            self.spi_com.steer_5(i)
            time.sleep(time_val * self.steer_speed)
        self.steer_val_5 = val
    def steer_set_val_6(self,val,time_val):
        if val < self.steer_val_6:
            l = list(range(self.steer_val_6,val,-10))
            l.append(val)
        else:
            l = list(range(self.steer_val_6,val,10))
            l.append(val)
        for i in l:
            self.spi_com.steer_6(i)
            time.sleep(time_val * self.steer_speed)
        self.steer_val_6 = val
    def steer_get_val_1(self):
        return self.steer_val_1
    def steer_get_val_2(self):
        return self.steer_val_2
    def steer_get_val_3(self):
        return self.steer_val_3
    def steer_get_val_4(self):
        return self.steer_val_4
    def steer_get_val_5(self):
        return self.steer_val_5
    def steer_get_val_6(self):
        return self.steer_val_6 
