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
        spi_com = SPI_COM() 
	def steer_posture_init(self):
		self.spi_com.steer_1(self.steer_val_1)		
		self.spi_com.steer_2(self.steer_val_2)		
		self.spi_com.steer_3(self.steer_val_3)		
		self.spi_com.steer_4(self.steer_val_4)		
		self.spi_com.steer_5(self.steer_val_5)		
		self.spi_com.steer_6(self.steer_val_6)	
	def steer_set_val_1(self,val,time):
		if val < self.steer_val_1:
			l = range(self.steer_val_1,val,-10)
			l.append(val)
		else:
			l = range(self.steer_val_1,10)
			l.append(val)
		for i in l:
			self.spi_com.steer_1(i)
			time.sleep(time)	
			 
