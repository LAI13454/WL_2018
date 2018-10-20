from spi_com import SPI_COM
import time
spi_com = SPI_COM()
while True:
    print(spi_com.gray_two(),end='\r')
    time.sleep(0.5)
