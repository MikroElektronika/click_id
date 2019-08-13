# Manifesto

A simple tool to generate a Greybus manifest blob from a Python
ConfigParser-style input file.

Provided under BSD license. See *LICENSE* for details.

# INSCLICK/RMCLICK

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
sudo rmclick oledc (clickname)
```

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
