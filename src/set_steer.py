import sys
from spi_com import SPI_COM
spi_com = SPI_COM()
if len(sys.argv) == 3:
    if sys.argv[1] == '1':
        spi_com.steer_1(int(sys.argv[2]))
    if sys.argv[1] == '2':
        spi_com.steer_2(int(sys.argv[2]))
    if sys.argv[1] == '3':
        spi_com.steer_3(int(sys.argv[2]))  
    if sys.argv[1] == '4':
        spi_com.steer_4(int(sys.argv[2]))
    if sys.argv[1] == '5':
        spi_com.steer_5(int(sys.argv[2]))
    if sys.argv[1] == '6':
        spi_com.steer_6(int(sys.argv[2]))
    if sys.argv[1] == '7':
        spi_com.steer_7(int(sys.argv[2]))
    if sys.argv[1] == '8':
        spi_com.steer_8(int(sys.argv[2]))

