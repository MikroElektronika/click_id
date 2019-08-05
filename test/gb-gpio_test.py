#!/usr/bin/python

import os

GBSTARTGPIO = 506 #needs to be generalized

mikrobusPBPins = [89,23,50,45,26,110]
mikrobusBBPins = [60,48,50,49,116,51,26,65,22,46,27,23]

def getPlatformPins():
    with open('/proc/device-tree/model','r') as f:
       model=f.readline()
       if(model.find("PocketBeagle")!=-1):
          print("Performing Greybus GPIO Test on PocketBeagle")
          return mikrobusPBPins
       else :           
           print("Performing Greybus GPIO Test on Beaglebone Black")
           return mikrobusBBPins

def testSingleGPIO(gpio_n,mikroBUSPins):
    mikroBUSgpio= mikroBUSPins[gpio_n-GBSTARTGPIO] #mikrobus GPIO ID
   
    gpio_gb="/sys/class/gpio/gpio" + str(gpio_n)
    gpio_mb="/sys/class/gpio/gpio" + str(mikroBUSgpio)

    with open(gpio_gb+"/direction", "w") as gpiodir: #test 1 : set input direction
        gpiodir.write("in")
    with open(gpio_mb+"/direction", "r") as gpiodir:
        assert gpiodir.readline().find("in")!=-1,"GPIO Input Direction Set Failed ("+str(gpio_n)+","+str(mikroBUSgpio)+")"

    with open(gpio_gb+"/direction", "w") as gpiodir: #test 2 : set output direction
        gpiodir.write("out")
    with open(gpio_mb+"/direction", "r") as gpiodir:
        assert gpiodir.readline().find("out")!=-1,"GPIO Input Direction Set Failed ("+str(gpio_n)+","+str(mikroBUSgpio)+")"

    with open(gpio_gb+"/value", "w") as gpiodir: #test 3 : write high
        gpiodir.write("1")
    with open(gpio_mb+"/value", "r") as gpiodir:
        assert int(gpiodir.readline())==1,"GPIO Value Set Failed ("+str(gpio_n)+","+str(mikroBUSgpio)+")"
    
    with open(gpio_gb+"/value", "w") as gpiodir: #test 3 : write low
        gpiodir.write("0")
    with open(gpio_mb+"/value", "r") as gpiodir:
        assert int(gpiodir.readline())==0,"GPIO Value Set Failed ("+str(gpio_n)+","+str(mikroBUSgpio)+")"

def testMikrobusGPIO(mikroBUSPins):
    for i in range(len(mikroBUSPins)):
        print("Testing Greybus GPIO: "+ str(GBSTARTGPIO+i))
        testSingleGPIO(GBSTARTGPIO+i,mikroBUSPins)

if __name__ == '__main__':
    print("**********MikroBUS GPIO Test********** \n")
    mikroBUSPins=getPlatformPins()
    #hack to find greybus startgpio 
    if(not os.path.exists("/sys/class/gpio/gpiochip"+str(GBSTARTGPIO))):
        for filename in os.listdir("/sys/class/gpio/"):
            if(filename.find("gpiochip")!=-1 and int(filename.replace("gpiochip",''))>300):
                GBSTARTGPIO= int(filename.replace("gpiochip",''))
                
    for i in range(len(mikroBUSPins)):
        with open("/sys/class/gpio/export", "w") as gpiodir:
            if(not os.path.exists("/sys/class/gpio/gpio"+str(GBSTARTGPIO+i))):
                gpiodir.write(str(GBSTARTGPIO+i))
    testMikrobusGPIO(mikroBUSPins)
    print("\n**********All GPIOS Passed All Checks**********")
