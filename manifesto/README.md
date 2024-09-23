## Manifesto

A simple tool to generate a mikroBUS manifest blob from a Python
ConfigParser-style input file.

Provided under BSD license. See *LICENSE* for details.

### Creating a Manifest Blob

# usage: manifesto [-h] [-I {mnfs,mnfb}] [-o OUT] [-O {mnfs,mnfb}] [-s] infile

For creating a manifest blob(.mnfb) from a manifest file(.mnfs) :
```
manifesto -I mnfs -O mnfb -o /path/to/output.mnfb /path/to/input.mnfs
```

Usage:

Clone the repository and create all the manifest binaries:
```
git clone https://github.com/MikroElektronika/click_id.git
cd manifesto
make all
sudo make install
```
The click can now be plugged in to the mikrobus port and the manifest binary can be passed to the mikrobus driver to load the click device driver(s)

### Writing a Manifest Blob to EEPROM

For writing a manifest blob(.mnfb) created from a manifest file(.mnfs) to an click :
```
dd if=/lib/firmware/mikrobus/your_manifest.mnfb of=/sys/bus/w1/devices/w1_bus_master1-<unique ID>/mikrobus_manifest
```

