## Manifesto

A simple tool to generate a mikroBUS manifest blob from a Python
ConfigParser-style input file.

Provided under BSD license. See *LICENSE* for details.

### Creating a Manifest Blob

For creating a manifest blob(.mnfb) from a manifest file(.mnfs) :
```
 manifesto -i /path/to/input.mnfs -o /path/to/output.mnfb
```

### Writing a Manifest Blob to EEPROM

For writing a manifest blob(.mnfb) created from a manifest file(.mnfs) to an EEPROM (the EEPROM probe is specific to the type of EEPROM) :
```
echo 24c32 0x57 > /sys/bus/i2c/devices/i2c-1/new_device
./manifesto -i manifests/mpu9dof.mnfs -o /sys/bus/nvmem/devices/1-00570/nvmem
echo 0x57 > /sys/bus/i2c/devices/i2c-1/delete_device
```

## Install

For generating the manifest blobs from all the manifest sources in the manifest/ directory , run the installation script:

```
sh install.sh
```
## Loading Clicks (Debug Interface run as root)

```
cat manifests/mpu9dof.mnfb >  /sys/class/mikrobus-port/mikrobus-0/new_device
```
## Unloading the Clicks (Debug Interface run as root)

```
echo 0 >  /sys/class/mikrobus-port/mikrobus-0/delete_device
```

## Adding Support for new Click Boards
 
Adding support for new click board normally just requires the addition of the new manifest source, the fields in a mikrobus manifest are explained as below:
```
;
; Click Board Manifest Source for
; ETH Click
; https://www.mikroe.com/eth-click
;

# -----------------------------------------------------------
#            Manifest Header
# -----------------------------------------------------------
[manifest-header]
version-major = 0
version-minor = 1
click-string-id = 1
reset-gpio-state = 2
int-gpio-state = 1

# -----------------------------------------------------------
#            Manifest String Descriptors
# -----------------------------------------------------------
; click string (id can't be 0)
[string-descriptor 1]
string = eth

; driver string
[string-descriptor 2]
string = enc28j60

# -----------------------------------------------------------
#            Manifest Device Descriptor Section
# -----------------------------------------------------------
; device descriptor
[device-descriptor 1]
driver-string-id = 2
protocol = 1
mode=0
max-speed-hz=16000000
irq = 1
irq-type = 2
```
* lines starting with ```;``` or ```#``` are considered as comments
* ```manifest-header``` : contains the details about the number of devices in the click , the click name string and the mikrobus gpio states required for the click board to work properly, the gpios whose state will be handled by the device driver , these are the possible states under the gpio state(Here in this example the reset line of the device is pulled low):
```
	MIKROBUS_GPIO_UNUSED = 0x00,
	MIKROBUS_GPIO_INPUT = 0x01,
	MIKROBUS_GPIO_OUTPUT_HIGH = 0x02,
	MIKROBUS_GPIO_OUTPUT_LOW = 0x03,
 ```
* ```device-descriptor``` : There can be multiple devices(sensors/actuators/display ..etc) inside a click device, this descriptor describe the device properties and the details required to instantiate the device on the corresponding bus(SPI/I2C/UART).
* ```driver-string-id``` : the device driver name for the device
* ```num-properties``` : number of custom properties required by the driver (provided to driver through Unified Property API)
* ```num-gpio-resource``` : number of named gpios required by the driver (provided to driver through GPIO Lookup Tables)
* ```mode``` : SPI Device Mode
* ```protocol``` : type of bus the device works on , can have the following values :
```
	MIKROBUS_PROTOCOL_SPI = 0x01,
	MIKROBUS_PROTOCOL_I2C = 0x02,
	MIKROBUS_PROTOCOL_UART = 0x03,
	MIKROBUS_PROTOCOL_SPI_GPIOCS = 0x04,
	MIKROBUS_PROTOCOL_I2C_MUX = 0x05
```
* ```reg``` : address / Chip select number for the device
* ```cs-gpio``` : CS GPIO used by the device, can have the values under the mikrobus GPIOs
* ```irq``` : IRQ GPIO used by the device, can have the values under the mikrobus GPIOs :
```
	MIKROBUS_GPIO_INVALID = 0x00, (feature unused)
	MIKROBUS_GPIO_INT = 0x01,
	MIKROBUS_GPIO_RST = 0x02,
	MIKROBUS_GPIO_PWM = 0x03,
```
* ```irq_type``` : Type of IRQ used by the device, same values as described in [linux/irq.h](https://elixir.bootlin.com/linux/v4.4/source/include/linux/irq.h#L80)

