#!/usr/bin/python

import os

GBSTARTGPIO = 506 #needs to be generalized

mikrobusPBPins = [89,23,50,45,26,110]
mikrobusBBPins = [60,48,50,49,116,51,26,65,22,46,27,23]

def getPlatformPins():
    with open('/proc/device-tree/model','r') as f:
       model=f.readline()
       if(model.find("PocketBeagle")!=-1):
          print("Performing Greybus GPIO IRQ Test on PocketBeagle")
          return mikrobusPBPins
       else :           
           print("Performing Greybus GPIO IRQ Test on Beaglebone Black")
           return mikrobusBBPins

def testSingleGPIO(gpio_n,mikroBUSPins):
    mikroBUSgpio= mikroBUSPins[gpio_n-GBSTARTGPIO] #mikrobus GPIO ID
   
    gpio_gb="/sys/class/gpio/gpio" + str(gpio_n)
    gpio_mb="/sys/class/gpio/gpio" + str(mikroBUSgpio)

    with open(gpio_gb+"/direction", "w") as gpiodir: #set input direction
        gpiodir.write("in")

    with open(gpio_gb+"/edge", "w") as gpiodir: #test 1 : set falling edge
        gpiodir.write("falling")
    with open(gpio_mb+"/edge", "r") as gpiodir:
        assert gpiodir.readline().find("falling")!=-1,"GPIO Input Edge Set Failed ("+str(gpio_n)+","+str(mikroBUSgpio)+")"

    with open(gpio_gb+"/edge", "w") as gpiodir: #test 2 : set rising edge
        gpiodir.write("rising")
    with open(gpio_mb+"/edge", "r") as gpiodir:
        assert gpiodir.readline().find("rising")!=-1,"GPIO Input Edge Set Failed ("+str(gpio_n)+","+str(mikroBUSgpio)+")"

    with open(gpio_gb+"/edge", "w") as gpiodir: #test 3 : set both edge
        gpiodir.write("both")
    with open(gpio_mb+"/edge", "r") as gpiodir:
        assert gpiodir.readline().find("both")!=-1,"GPIO Input Edge Set Failed ("+str(gpio_n)+","+str(mikroBUSgpio)+")"
    
    with open(gpio_gb+"/edge", "w") as gpiodir: #Disable all the interrupts set
        gpiodir.write("none")
    with open(gpio_mb+"/edge", "w") as gpiodir:
        gpiodir.write("none")

def testMikrobusGPIO(mikroBUSPins):
    for i in range(len(mikroBUSPins)):
        print("Testing Greybus GPIO IRQ : "+ str(GBSTARTGPIO+i))
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
