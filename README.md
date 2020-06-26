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

Flash the testing image with the mikrobus driver available at [https://rcn-ee.net/rootfs/bb.org/testing/2020-06-24/buster-iot-mikrobus/bone-debian-10.4-iot-mikrobus-armhf-2020-06-24-4gb.img.xz](https://rcn-ee.net/rootfs/bb.org/testing/2020-06-24/buster-iot-mikrobus/bone-debian-10.4-iot-mikrobus-armhf-2020-06-24-4gb.img.xz) using [Etcher](https://www.balena.io/etcher/), then to load the mikrobus driver: 
```
sudo modprobe mikrobus
```
Then pass the configuration array to attach the mikrobus port(s) with the mikrobus driver(need to be done as root), if trying out on a PocketBeagle with Techlab Cape then only the mikroBUS port 1 need to be attached, if not using a Techlab Cape see [PocketBeagle Wiki](https://github.com/beagleboard/pocketbeagle/wiki/System-Reference-Manual#72-mikrobus-socket-connections) to find out the mikroBUS ports position:
```
sudo su
printf "%b" '\x01\x00\x00\x59\x32\x17' > /sys/bus/mikrobus/add_port	(mikrobus port 1) --> Techlab Cape mikrobus Port
printf "%b" '\x02\x01\x00\x2d\x6e\x1a' > /sys/bus/mikrobus/add_port 	(mikrobus port 2)
```
Then clone the manifesto repository and checkout the mikrobusv2 branch and create all the manifest binaries:
```
git clone https://github.com/vaishnav98/manifesto.git
cd manifesto
git checkout mikrobusv2
./install.sh (will take about a minute)
```
The click can now be plugged in to the mikrobus port and the manifest binary can be passed to the mikrobus driver to load the click device driver(s), the manifests under manifests/ directory is marked as NOT-TESTED for clicks that are yet to be tested,rest of the manifests will have their latest commit message  == the testing logs and click usage, for exampe see the [RTC 6 Click Manifest Source](https://github.com/vaishnav98/manifesto/blob/mikrobusv2/manifests/RTC-6-CLICK.mnfs) :
```
root@beaglebone:/home/debian/manifesto# cat manifests/RTC-6-CLICK-NOT-TESTED.mnfb >  /sys/class/mikrobus-port/mikrobus-0/new_device
root@beaglebone:/home/debian/manifesto# dmesg
[ 5074.789367] mikrobus_manifest: Device 1 , number of properties=0 , number of gpio resources=0
[ 5074.789384] mikrobus_manifest:  RTC 6 Click manifest parsed with 1 device(s)
[ 5074.789394] mikrobus:  registering device : mcp7941x
[ 5074.800576] rtc-ds1307 1-006f: registered as rtc1
root@beaglebone:/home/debian/manifesto# cat /sys/class/rtc/rtc1/
date           dev            device/        hctosys        max_user_freq  name           power/         since_epoch    subsystem/     time           uevent
root@beaglebone:/home/debian/manifesto# cat /sys/class/rtc/rtc1/time
12:03:19
root@beaglebone:/home/debian/manifesto# cat /sys/class/rtc/rtc1/date
2020-06-23
root@beaglebone:/home/debian/manifesto# echo 0 >  /sys/class/mikrobus-port/mikrobus-0/delete_device
root@beaglebone:/home/debian/manifesto# dmesg
[ 5074.789367] mikrobus_manifest: Device 1 , number of properties=0 , number of gpio resources=0
[ 5074.789384] mikrobus_manifest:  RTC 6 Click manifest parsed with 1 device(s)
[ 5074.789394] mikrobus:  registering device : mcp7941x
[ 5074.800576] rtc-ds1307 1-006f: registered as rtc1
[ 5106.657836] mikrobus:  removing device : mcp7941x
```
### Loading Clicks (Debug Interface run as root)

```
cat manifests/CLICK_NAME.mnfb >  /sys/class/mikrobus-port/mikrobus-0/new_device
cat manifests/WEATHER-CLICK.mnfb >  /sys/class/mikrobus-port/mikrobus-0/new_device
```
### Unloading the Clicks (Debug Interface run as root)

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
