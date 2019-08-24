## Manifesto

A simple tool to generate a Greybus manifest blob from a Python
ConfigParser-style input file.

Provided under BSD license. See *LICENSE* for details.

### Creating a Manifest Blob

For creating a manifest blob(.mnfb) from a manifest file(.mnfs) :
```
 manifesto -o /path/to/output.mnfb  /path/to/input.mnfs
```
## INSCLICK/RMCLICK

A python CLI for easy loading/unloading of MikroElektronika Click Boards through Greybus Manifests

## Install

For installing the utilities, generating the manifest blobs and adding the insclick/rmclick CLI to path, run the installation script:

```
sudo sh install.sh
```
## Loading Clicks

```
sudo insclick rtc6 (clickname) p1 (portname :p1 ,p2 ,p3 ,p4)

```
Here the argument `portname` corresponds to the slot in which the click is connected , the PocketBeagle Mikrobus position 1 and Beaglebone Mikrobus Cape Position 1 corresponds to p1, the PocketBeagle Mikrobus position 2 and Beaglebone Mikrobus Cape Position 2 corresponds to p2, p3 and p4 corresponds to the slots 3 and 4 in the Beaglebone Mikrobus Cape The CLI also supports g1 and g2 slots which corresponds to the I2C and UART grove ports on the Seedstudio Beaglebone Green. 
The argument `clickname` corresponds to the click name , for example `rtc6` `weather` etc.

## Unloading the Clicks

The rmclick utility/command can be used to remove/free the Greybus Interface and Unload the Click, the rmclick usage is:

```
sudo rmclick oledc (clickname) p1 (portname :p1 ,p2 ,p3 ,p4)
```
## Adding Support for new Click Boards
 
Adding support for new click board normally requires the addition of the click data under clicks.json and creating a new manifest(only for simple SPI based clicks), some example entries for SPI and I2C based clicks are explained below :

### Adding Support for Simple I2C Click

Adding support for simple I2C clicks which has no interrupts or other platform data requirements requires only the addition of the corresponding entry under `clicks.json` . An example entry for the RTC 6 Click based on the MCP79410 I2C RTC is shown below: 

```
"rtc6": {
        "type": "i2c",
        "class": "ordinary",
        "driver": "mcp7941x",
        "address": "0x6f",
        "info": [
            "RTC 6 Click",
            "Use Command : sudo hwclock -r --rtc /dev/rtc1 to display the RTC Date and Time",
            "use cat /sys/class/rtc/rtc1/date  to get the RTC Date",
            "use cat /sys/class/rtc/rtc1/time  to get the RTC Time",
            "use cat /sys/class/rtc/rtc1/since_epoch  to get the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT)"
        ]
    }
```
Here the key for the entry is the name of the click `rtc6` , this name will be available with the insclick/rmclick commands.The other entries are:

 * `type` : corresponds to the type of bus the click uses (currently SPI/I2C)
 * `class` : corresponds to whether the click requires additional platform data or not , in this case class->ordinary , the available options are : oridnary/platform/display 
 * `driver` : corresponds to the name of linux driver available for the click device
 * `address` : corresponds to the I2C address of the device
  * `info` : this section contains the helping information for the user to get started with the Click Board , the helper string array can have any length and each array element will be displayed in new line when invoking the insclick command
  
### Adding Support for Simple SPI Click

Adding support for simple SPI clicks which has no interrupts or other platform data requirements requires only the addition of the corresponding entry under `clicks.json` and creation of a greybus manifest file for the device. An example entry for the MicroSD Click is shown below: 

```
"microSD": {
        "type": "spi",
        "class": "ordinary",
        "info": [
            "microSD Click",
            "usage information"
        ]
    },
```
Here the key for the entry is the name of the click `microSD` , this name will be available with the insclick/rmclick commands.The other entries are:

 * `type` : corresponds to the type of bus the click uses (currently SPI/I2C)
 * `class` : corresponds to whether the click requires additional platform data or not , in this case class->ordinary , the available options are : oridnary/platform/display 
 * `info` : this section contains the helping information for the user to get started with the Click Board , the helper string array can have any length and each array element will be displayed in new line when invoking the insclick command
 
 The example manifest for a microSD click is as shown below
 
 ```
 ;
; Simple SPI Interface Manifest
;
; Copyright 2015 Google Inc.
; Copyright 2015 Linaro Ltd.
;
; Provided under the three clause BSD license found in the LICENSE file.
;

[manifest-header]
version-major = 0
version-minor = 1

[interface-descriptor]
vendor-string-id = 1
product-string-id = 2

; Interface vendor string (id can't be 0)
[string-descriptor 1]
string = MikroElektronika
; Driver Name string (id can't be 0)
[string-descriptor 2]
string = mmc_spi

; Control cport and bundle are optional.
; - Control cport's id must be 0 and its bundle number must be 0.
; - No other bundle or control cport may use these values.
; - Class and protocol of bundle and cport must be marked as 0x00.
;
;Control protocol on CPort 0
[cport-descriptor 0]
bundle = 0
protocol = 0x00

;Control protocol Bundle 0
[bundle-descriptor 0]
class = 0

; SPI protocol on CPort 1
[cport-descriptor 1]
bundle = 1
protocol = 0x0b

; Bundle 1
[bundle-descriptor 1]
class = 0x0a
 
 ```
For adding support for new SPI clicks without additional platform data , a new manifest needs to be made from the above template where the `string-decriptor 2` property should match the device driver corresponding to the clickboard (here mmc_spi corresponds to the driver for the microSD click), the newly created manifests should be saved under the manifests/ directory where the name of the manifest file should be same as the click name


### Adding Support for SPI based Display Click

Adding support for SPI based display clicks requires only the additon of a corresponding entry under `clicks.json`, currently the display clicks supported by the [fbtft](https://github.com/beagleboard/linux/tree/4.14/drivers/staging/fbtft) driver is supported through this method. An example entry for the OLED Click based on the SSD1306 driver is shown below: 

```
"oledb": {
        "type": "spi",
        "class": "display",
        "driver": "fb_ssd1306",
        "width": "96",
        "height": "39",
        "speed": "6000000",
        "buswidth": "8",
        "fps": "40",
        "info": [
            "OLEDB Click",
            "blinking cursor will be diplayed on the screen if setup was successful",
            "use  sudo fbi -T 1 -a NameofImage to display an image",
            "use sudo screen /dev/tty1 to enter a conole on the OLED Screen",
            "echo text | sudo tee /dev/vcs1 (or /dev/tty1) to display some text on the display"
        ]
    }
```
Here the key for the entry is the name of the click `oledb` , this name will be available with the insclick/rmclick commands.The other entries are:

 * `type` : corresponds to the type of bus the click uses (currently SPI/I2C)
 * `class` : corresponds to the class of the click, in this case class->display , the available options are : oridnary/platform/display 
 * `driver` : corresponds to the name of linux driver available for the click device
 * `width` : width of the display
 * `height` : height of the display
 * `speed` : SPI Bus Speed (Hz)
 * `buswdith` : number of bits width
 * `fps` : Frame Per Second
 * `info` : this section contains the helping information for the user to get started with the Click 
 
 ### Adding Support for I2C based Generic Click with Platform Data

Adding support for I2C based clicks with additional platform data requires only the additon of a corresponding entry under `clicks.json`, currently the clicks with interrupt requirements is supported through this method, for adding support for clicks with additonal platform_data, the [mikrobus_i2c driver](https://github.com/vaishnav98/mikrobus_device/blob/master/mikrobus_i2c_device.c) needs to be modified. An example entry for the MPU9DOF Click based on the MPU9150 driver is shown below: 

```
 "mpu9dof": {
        "type": "i2c",
        "class": "platform",
        "driver": "mpu9150",
        "address": "0x68",
        "info": [
            "MPU9DOF Click",
            "Use Command : cat /sys/bus/iio/devices/iio\\:device1/in_accel_x_raw to display the x-direction raw acceleration",
            "use cat /sys/bus/iio/devices/iio\\:device1/in_accel_y_raw to display the y-direction raw acceleration",
            "use cat /sys/bus/iio/devices/iio\\:device1/in_accel_z_raw to display the z-direction raw acceleration",
            "use cat /sys/bus/iio/devices/iio\\:device1/in_anglvel_x_raw to display the x-direction raw angular velocity",
            "use cat /sys/bus/iio/devices/iio\\:device1/in_anglvel_y_raw to display the y-direction raw angular velocity",
            "use cat /sys/bus/iio/devices/iio\\:device1/in_anglvel_z_raw to display the z-direction raw angular velocity",
            "use cat /sys/bus/iio/devices/iio\\:device1/in_temp_raw to display the raw tmeperature reading"
        ]
    }
```
Here the key for the entry is the name of the click `mpu9dof` , this name will be available with the insclick/rmclick commands.The other entries are:

 * `type` : corresponds to the type of bus the click uses (currently SPI/I2C)
 * `class` : corresponds to the class of the click, in this case class->platform as additonal platform data is required , the available options are : oridnary/platform/display 
 * `driver` : corresponds to the name of linux driver available for the click device
 * `address` : corresponds to the I2C address of the device
 * `info` : this section contains the helping information for the user to get started with the Click 

 ### Adding Support for SPI based Generic Click with Platform Data

Adding support for SPI based clicks with additional platform data requires only the additon of a corresponding entry under `clicks.json`, currently the clicks with interrupt requirements is supported through this method, for adding support for clicks with additonal platform_data, the [mikrobus_spi driver](https://github.com/vaishnav98/mikrobus_device/blob/master/mikrobus_spi_device.c) needs to be modified. An example entry for the ETH Click based on the enc28j60 driver is shown below: 

```
    "eth": {
        "type": "spi",
        "class": "platform",
        "driver": "enc28j60",
        "speed": "16000000",
        "info": [
            "ETH Click",
            "usage information"
        ]
    }
```
Here the key for the entry is the name of the click `eth` , this name will be available with the insclick/rmclick commands.The other entries are:

 * `type` : corresponds to the type of bus the click uses (currently SPI/I2C)
 * `class` : corresponds to the class of the click, in this case class->platform as additonal platform data is required , the available options are : oridnary/platform/display 
 * `driver` : corresponds to the name of linux driver available for the click device
 * `speed` : corresponds to the SPI Bus Speed (Hz)
 * `info` : this section contains the helping information for the user to get started with the Click 

## Mikrobus Tests

The test directory contains some simple python based tests to verify the peripheral creation by gbsim and verify the correct transfers between virtual interfaces in greybus and actual physical interfaces  (for example : greybus gpio <-> physical mikrobus gpio)

### Test Mikrobus GPIO

```
sudo startgbsim
cp manifests/gpio.mnfb /tmp/gbsim/hotplug-modules/
sudo python gb-gpio_test.py
```

### Test Mikrobus GPIO IRQ

```
sudo startgbsim
cp manifests/gpio.mnfb /tmp/gbsim/hotplug-modules/
sudo python gb-gpioirq_test.py
```

### Test Mikrobus SPI

```
sudo startgbsim
cp manifests/oled.mnfb /tmp/gbsim/hotplug-modules/
sudo python gb-spi_test.py
```

### Test Mikrobus I2C

```
sudo startgbsim
cp manifests/i2c1.mnfb /tmp/gbsim/hotplug-modules/
sudo python gb-i2c_test.py
```
