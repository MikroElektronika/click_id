import os

GBSPIDEV="3"

if __name__ == '__main__':
    print("**********MikroBUS SPI Test**********\n")
    #hack to find greybus spi bus 
    if(not os.path.exists("/sys/class/spi_master/spi"+GBSPIDEV)):
        for filename in os.listdir("/sys/class/spi_master/"):
            if(filename.find("spi")!=-1 and int(filename.replace("spi",''))>=3):
                GBSPIDEV=filename.replace("spi",'')
    print("checking for spidev at: "+"/dev/spidev"+GBSPIDEV+".1")
    if(os.path.exists("/dev/spidev"+GBSPIDEV+".1")):
        print("\n**********MikroBUS SPI Check Passed**********")
    else:
        print("\n**********MikroBUS SPI Check Failed**********")
