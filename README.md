## Manifesto

A simple tool to generate a mikroBUS manifest blob from a Python
ConfigParser-style input file.

Provided under BSD license. See *LICENSE* for details.

### Creating a Manifest Blob

For creating a manifest blob(.mnfb) from a manifest file(.mnfs) :
```
 manifesto -i /path/to/input.mnfs -o /path/to/output.mnfb
```

## Install

For generating the manifest blobs from all the manifest sources in the manifest/ directory , run the installation script:

```
sh install.sh
```

## Reproducing the Results using PocketBeagle 

Flash the testing image with the mikrobus driver available at [https://rcn-ee.net/rootfs/bb.org/testing/2020-08-15/buster-iot-mikrobus/](https://rcn-ee.net/rootfs/bb.org/testing/2020-08-15/buster-iot-mikrobus/) using [Etcher](https://www.balena.io/etcher/), then to load the mikrobus driver: 

Then edit the uEnv.txt to load the overlays for the mikrobus port-0 and port-1 on the pocketbeagle
```
sudo nano /boot/uEnv.txt
(Edit the below lines)
#uboot_overlay_addr0=/lib/firmware/<file0>.dtbo
#uboot_overlay_addr1=/lib/firmware/<file1>.dtbo
(to)
uboot_overlay_addr0=/lib/firmware/PB-MIKROBUS-0.dtbo
uboot_overlay_addr1=/lib/firmware/PB-MIKROBUS-1.dtbo
```

Then clone the manifesto repository and checkout the mikrobusv3 branch and create all the manifest binaries:
```
git clone https://github.com/vaishnav98/manifesto.git
cd manifesto
git checkout mikrobusv3
./install.sh (will take about a minute)
```
The click can now be plugged in to the mikrobus port and the manifest binary can be passed to the mikrobus driver to load the click device driver(s), the manifests under manifests/ directory are TESTED and the test script provided can be used for testing different click.

### Test Script Usage

```
debian@beaglebone:~/manifesto$ ./test
board name> MPU-              (Press Tab to Auto complete from list of supported clicks)
MPU-9DOF-CLICK  MPU-IMU-CLICK   
board name> MPU-9DOF-CLICK
port> mikrobus-               (Press Tab to Auto complete from list of attached mikrobus port)
mikrobus-0  mikrobus-1  
port> mikrobus-0
testing MPU-9DOF-CLICK on mikrobus-0 

[ 2805.111767] mikrobus_manifest:mikrobus_manifest_parse:  MPU 9DOF Click manifest parsed with 1 devices
[ 2805.111813] mikrobus:mikrobus_port_pinctrl_select: setting pinctrl pwm_default
[ 2805.111824] mikrobus:mikrobus_port_pinctrl_select: setting pinctrl uart_default
[ 2805.111836] mikrobus:mikrobus_port_pinctrl_select: setting pinctrl i2c_default
[ 2805.111848] mikrobus:mikrobus_port_pinctrl_select: setting pinctrl spi_default
[ 2805.111873] mikrobus mikrobus-0: registering device : mpu9150
[ 2805.169305] inv-mpu6050-i2c 1-0068: mounting matrix not found: using identity...
[ 2805.169346] inv-mpu6050-i2c 1-0068: supply vdd not found, using dummy regulator
[ 2805.169445] inv-mpu6050-i2c 1-0068: supply vddio not found, using dummy regulator
[ 2805.280525] inv-mpu6050-i2c 1-0068: whoami mismatch got 0x71 (MPU9250)expected 0x68 (MPU9150)
IN_ACCEL_Z_CALIBBIAS /sys/bus/iio/devices/iio:device1/in_accel_z_calibbias : -2045
IN_ANGLVEL_Z_RAW /sys/bus/iio/devices/iio:device1/in_anglvel_z_raw : -13
IN_ANGLVEL_Y_CALIBBIAS /sys/bus/iio/devices/iio:device1/in_anglvel_y_calibbias : 0
IN_ACCEL_Y_RAW /sys/bus/iio/devices/iio:device1/in_accel_y_raw : -200
IN_MAGN_Z_SCALE /sys/bus/iio/devices/iio:device1/in_magn_z_scale : 0.003574
IN_ANGLVEL_SCALE /sys/bus/iio/devices/iio:device1/in_anglvel_scale : 0.001064724
IN_ACCEL_MOUNT_MATRIX /sys/bus/iio/devices/iio:device1/in_accel_mount_matrix : 1, 0, 0; 0, 1, 0; 0, 0, 1
IN_MAGN_Z_RAW /sys/bus/iio/devices/iio:device1/in_magn_z_raw : -8
IN_ACCEL_X_CALIBBIAS /sys/bus/iio/devices/iio:device1/in_accel_x_calibbias : 8684
IN_TEMP_SCALE /sys/bus/iio/devices/iio:device1/in_temp_scale : 2.941176
IN_ACCEL_Z_RAW /sys/bus/iio/devices/iio:device1/in_accel_z_raw : 17212
IN_MAGN_X_SCALE /sys/bus/iio/devices/iio:device1/in_magn_x_scale : 0.003574
IN_ACCEL_SCALE /sys/bus/iio/devices/iio:device1/in_accel_scale : 0.000598
IN_ANGLVEL_Z_CALIBBIAS /sys/bus/iio/devices/iio:device1/in_anglvel_z_calibbias : 0
IN_ANGLVEL_SCALE_AVAILABLE /sys/bus/iio/devices/iio:device1/in_anglvel_scale_available : 0.000133090 0.000266181 0.000532362 0.001064724
IN_ACCEL_SCALE_AVAILABLE /sys/bus/iio/devices/iio:device1/in_accel_scale_available : 0.000598 0.001196 0.002392 0.004785
IN_ANGLVEL_X_RAW /sys/bus/iio/devices/iio:device1/in_anglvel_x_raw : 78
IN_TEMP_OFFSET /sys/bus/iio/devices/iio:device1/in_temp_offset : 12420
IN_ACCEL_Y_CALIBBIAS /sys/bus/iio/devices/iio:device1/in_accel_y_calibbias : 3831
IN_ANGLVEL_X_CALIBBIAS /sys/bus/iio/devices/iio:device1/in_anglvel_x_calibbias : 0
IN_MAGN_X_RAW /sys/bus/iio/devices/iio:device1/in_magn_x_raw : -17
IN_MAGN_Y_SCALE /sys/bus/iio/devices/iio:device1/in_magn_y_scale : 0.003574
IN_ANGLVEL_MOUNT_MATRIX /sys/bus/iio/devices/iio:device1/in_anglvel_mount_matrix : 1, 0, 0; 0, 1, 0; 0, 0, 1
IN_ACCEL_MATRIX /sys/bus/iio/devices/iio:device1/in_accel_matrix : 0, 0, 0; 0, 0, 0; 0, 0, 0
IN_ANGLVEL_Y_RAW /sys/bus/iio/devices/iio:device1/in_anglvel_y_raw : -65
IN_ACCEL_X_RAW /sys/bus/iio/devices/iio:device1/in_accel_x_raw : 320
IN_MAGN_MOUNT_MATRIX /sys/bus/iio/devices/iio:device1/in_magn_mount_matrix : 0, 1, 0; 1, 0, 0; 0, 0, -1
IN_GYRO_MATRIX /sys/bus/iio/devices/iio:device1/in_gyro_matrix : 0, 0, 0; 0, 0, 0; 0, 0, 0
IN_TEMP_RAW /sys/bus/iio/devices/iio:device1/in_temp_raw : 1493
IN_MAGN_Y_RAW /sys/bus/iio/devices/iio:device1/in_magn_y_raw : -33
remove board[y/n]> y
[ 2818.790861] mikrobus mikrobus-0: removing device mpu9150
debian@beaglebone:~/manifesto$ 
```

### Loading Add-on Board (Debug Interface run as root)

```
cat manifests/BOARD_NAME.mnfb >  /sys/class/mikrobus-port/mikrobus-0/new_device
cat manifests/WEATHER-CLICK.mnfb >  /sys/class/mikrobus-port/mikrobus-0/new_device
```
### Unloading the Add-on Board (Debug Interface run as root)

```
echo 0 >  /sys/class/mikrobus-port/mikrobus-0/delete_device
```

### Writing a Manifest Blob to EEPROM

For writing a manifest blob(.mnfb) created from a manifest file(.mnfs) to an EEPROM (the EEPROM probe is specific to the type of EEPROM) :
```
echo 24c32 0x57 > /sys/bus/i2c/devices/i2c-1/new_device
./manifesto -i manifests/mpu9dof.mnfs -o /sys/bus/nvmem/devices/1-00570/nvmem
echo 0x57 > /sys/bus/i2c/devices/i2c-1/delete_device
```

### Writing a Manifest Blob to  Click ID EEPROM

If a valid manifest binary is not found in the Click ID EEPROM, the device is exposed as a NVMEM device and the manifest can be written to the EEPROM in the following manner.
```
$ ./manifesto -i manifests/RTC-6-CLICK.mnfs -o /sys/bus/nvmem/devices/mikrobus-port0/nvmem
$ hexdump /sys/bus/nvmem/devices/mikrobus-port0/nvmem                             (reading back written manifest)
0000000 0074 0100 0008 0001 0201 0000 0018 0002
0000010 0110 694d 726b 456f 656c 746b 6f72 696e
0000020 616b 0000 0014 0002 020b 5452 2043 2036
0000030 6c43 6369 006b 0000 0010 0005 0104 0707
0000040 0606 0505 0505 0102 0008 0004 0001 0301
0000050 0014 0007 0301 6f03 0000 0000 0000 0000
0000060 0000 0000 0010 0002 0308 636d 3770 3439
0000070 7831 0000 0000 0000 0000 0000 0000 0000
0000080 ffff ffff ffff ffff ffff ffff ffff ffff
*
```

### Writing Manifests for new Add-On Boards

For writing manifests for new add-on boards using an interactive interface head over to https://vaishnav98.github.io/manifesto/

### Status of Supported Add-on Boards

To see the status of Supported add-on boards, view [this CSV sheet](click_info.csv)

### Hardware Modifications

Some of the Existing Clicks require minor hardware modifications to work with the kernel driver correctly. This section maintains the list of the clicks which require hardware modifications:

* GNSS ZOE Click : Swap COMM SEL Jumpers Default Position to select UART.
* GNSS Clicks: All GNSS Clicks are Supported through the gnss linux subsytems, so their COMM SEL Default position needs to be in the UART Position
* 6 LoWPAN T Click : The driver requires fifo, fifop, sfd, cca, vreg and reset gpio of which vreg, reset and fifo gpios are routed to the mikroBUS headers correctly but the 
other GPIOs are not accessible, GPIO 2,3,4 from CC2520 needs to be routed to the mikroBUS headers(GPIO reference 1MHZ Clock is not necessary).
* 6 LoWPAN C Click : The driver requires fifo, fifop, sfd, cca, vreg and reset gpio of which vreg, reset and fifo gpios are routed to the mikroBUS headers correctly but the 
other GPIOs are not accessible, GPIO 2,3,4 from CC2520 needs to be routed to the mikroBUS headers(GPIO reference 1MHZ Clock is not necessary).

### Kconfig
This list contains a few dependent Kconfig settings that needs to be applied(if you are testing all of the supported) apart from the Click Driver Kconfig.

```
CONFIG_MODULES=y
CONFIG_SYSFS=y
CONFIG_I2C=y
CONFIG_SPI=y
CONFIG_GPIOLIB=y
CONFIG_PWM=y
CONFIG_IIO=m
CONFIG_MIKROBUS=m
CONFIG_STAGING=y
CONFIG_FB=y
CONFIG_FB_TFT=m
CONFIG_NET=y
CONFIG_NETDEVICES=y
CONFIG_ETHERNET=y
CONFIG_NET_VENDOR_MICROCHIP=y
CONFIG_MMC=m
CONFIG_RTC_CLASS=y
CONFIG_NFC=m
CONFIG_NFC_DIGITAL=m
```

