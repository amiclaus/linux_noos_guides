### Host Environment Variables:
#### ARM
`export ARCH=arm`  
`export CROSS_COMPILE=arm-linux-gnueabihf-`  

One line example:  
`export CROSS_COMPILE=arm-linux-gnueabihf- ARCH=arm`  

#### ARM64
`export ARCH=arm64`  
`export CROSS_COMPILE=aarch64-linux-gnu-`  

Optional: `export KCFLAGS="$KCFLAGS -Wmaybe-uninitialized"`

### Kernel configuration:
`make adi_bcm2709_defconfig`  
or   
`make adi_bcm2711_defconfig` (for rpi4)  
or  
`make adi_bcmrpi_defconfig` (for rpi zero, zero W)  
or  
`make zynq_xcomm_adv7511_defconfig` (for Zynq)  
or  
`make adi_zynqmp_defconfig ` (for ZynqMP)  

### Building the Kernel:
`make -j4`  
or  
`make -j4 zImage modules dtbs` (for rpi)  
or  
`make -j4 UIMAGE_LOADADDR=0x8000 uImage` (for Zynq)  
or  
`make -j4 Image UIMAGE_LOADADDR=0x8000` (for ZynqMP)  

### Install modules:
`sudo make modules_install`  
or  
with path to rootfs: `sudo make INSTALL_MOD_PATH=/media/amiclaus/rootfs/ modules_install`

### Copy the outputs
`sudo cp arch/arm/boot/dts/*.dtb /media/amiclaus/BOOT/`  
`sudo cp arch/arm/boot/dts/overlays/*.dtb* /media/amiclaus/BOOT/overlays/`  
`sudo cp arch/arm/boot/dts/overlays/README /media/amiclaus/BOOT/overlays/`  
`sudo cp arch/arm/boot/zImage /media/amiclaus/BOOT/$KERNEL.img`  

Replace `$KERNEL.img` with `kernel7.img` for Pi 2/3, `kernel7l.img` for Pi 4, `kernel.img` for Pi Zero/Pi Zero 2.

with scp:
`scp arch/arm/boot/zImage root@192.168.1.122:/boot/kernel7.img` 
`scp arch/arm/boot/dts/overlays/rpi-admv1014.dtbo  root@10.48.65.139:/boot/overlays`

### Rpi mount:
`ifconfig`  
`mount /dev/mmcblk0p1 /media/boot/`  
`ls -l /media/boot`  

### Checkpatch:
`scripts/checkpatch.pl --git HEAD --ignore FILE_PATH_CHANGES --ignore LONG_LINE --ignore LONG_LINE_STRING --ignore LONG_LINE_COMMENT --strict`

### Device Tree Bindings:
`pip3 install git+https://github.com/devicetree-org/dt-schema.git@master`  
or  
`pip3 install dtschema` (preferred)  

Additional packages:  
`pip3 install jsonschema yamllint`  
`sudo apt-get install libyaml-dev`  
Export Path:  
`export PATH=$PATH:/home/amiclaus/.local/bin`  
### dt-bindings check:
`make dtbs_check DT_SCHEMA_FILES=Documentation/devicetree/bindings/iio/amplifiers/adi,ada4250.yaml`  
or  
`make dt_binding_check`  
or  
**with flags**: `make DT_CHECKER_FLAGS=-m DT_SCHEMA_FILES=Documentation/devicetree/bindings/iio/frequency/adi,adrf6780.yaml dt_binding_check`

### Overlays
with parameters: `dtoverlay=rpi-ad7746,addr=0xXX`

### How to copy image:
`sudo dd if=/dev/sde of=/dev/sdf bs=4M status=progress`  
or  
`lsblk`  
`sudo fdisk -l /dev/sde`  
`sudo dd if=/dev/sdf of=/media/amiclaus/799D2070502D4D79/adrv9009zu11eg_fmcbridge_prod_test_2022.img bs=512 count=22618130 status=progress`  

### Miscellaneous Stuff:
Set IP for network interface: `sudo ifconfig enx00e04c680465 192.168.56.5/24`  
