import sys
from spi_com import SPI_COM
spi_com = SPI_COM()
if len(sys.argv) == 3:
    if sys.argv[1] == '1':
        spi_com.motor_left(int(sys.argv[2]))
    if sys.argv[1] == '2':
        spi_com.motor_right(int(sys.argv[2]))
