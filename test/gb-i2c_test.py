import os

GBI2CDEV="3"

if __name__ == '__main__':
    print("**********MikroBUS I2C Test**********\n")
    #hack to find greybus i2c bus 
    if(not os.path.exists("/sys/class/i2c-adapter/i2c-"+GBI2CDEV)):
        for filename in os.listdir("/sys/class/i2c-adapter/"):
            if(filename.find("i2c")!=-1 and int(filename.replace("i2c-",''))>=3):
                GBI2CDEV=filename.replace("i2c-",'')
    print("checking for i2cdev at: "+"/dev/i2c-"+GBI2CDEV)
    if(os.path.exists("/dev/i2c-"+GBI2CDEV)):
        print("\n**********MikroBUS I2C Check Passed**********")
    else:
        print("\n**********MikroBUS I2C Check Failed**********")
