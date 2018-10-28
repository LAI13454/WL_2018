import spidev
class SPI_COM:
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.max_speed_hz = 50000 
    def motor_left(self,val):
        #print(val)
        self.spi.xfer([0xaa,0x01,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
        #print(val)
    def motor_right(self,val):
        self.spi.xfer([0xaa,0x02,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
    def motor(self,val):
        self.motor_left(val)
        self.motor_right(val)
    def steer_1(self,val):
        self.spi.xfer([0xaa,0x11,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
    def steer_2(self,val):
        self.spi.xfer([0xaa,0x12,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
    def steer_turn_1(self,val):
        self.spi.xfer([0xaa,0x13,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
    def steer_3(self,val):
        self.spi.xfer([0xaa,0x14,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
    def steer_4(self,val):
        self.spi.xfer([0xaa,0x15,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
    def steer_5(self,val):
        self.spi.xfer([0xaa,0x16,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
    def steer_6(self,val):
        self.spi.xfer([0xaa,0x17,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
    def steer_turn_2(self,val):
        self.spi.xfer([0xaa,0x18,(val>>8)&0xff,val&0xff,0x00,0x00,0x55])
    def steer_turn(self,val):
        val = val - 60
        if val <= 0:
            #Left Turn
            if val <= -650:
                self.steer_turn_1(-650) #left
            else:
                self.steer_turn_1(val)
            if val <= -650:
                self.steer_turn_2(-650) #right
            else:
                self.steer_turn_2(val)
        else:
            #Right Turn
            if val > 550:
                self.steer_turn_1(550)
            else:
                self.steer_turn_1(val)
            if val > 550:
                self.steer_turn_2(550)
            else:
                self.steer_turn_2(val)

    def gray(self):
        val = []
        num = self.spi.xfer([0xaa,0x21,0x00,0x00,0xff,0xff,0x55])
        temp = ((num[4]<<8)|num[5])&0x0fff
        for i in range(12):
            if temp & (0x01<<i):
                val.append(1)
            else:
                val.append(0)
        #val.reverse()
        return val
    def gray_two(self):
        val = []
        num = self.spi.xfer([0xaa,0x22,0x00,0x00,0xff,0xff,0x55])
        temp = ((num[4]<<8)|num[5])&0x0fff
        for i in range(12):
            if temp & (0x01<<i):
                val.append(1)
            else:
                val.append(0)
        val.reverse()
        return val

