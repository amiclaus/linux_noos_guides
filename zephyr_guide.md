### Documentation
`https://docs.zephyrproject.org/latest/develop/getting_started/index.html`  
### Build Commands
`west build -t menuconfig`  
`west build -b nucleo_f446re samples/hello_world`  
`west -v build -p always -c -b nucleo_f413zh samples/sensor/adt7420/`  
`west flash`  

#### Build with flags
`west build -p always -b adin6310_ethernet_switch samples/application_development/adin6310_eth_config/ -DLIB_ADIN6310_PATH=/home/amiclaus/Downloads/adinx310_tsn_driver_library_rel3.0.0/ADINx310_TSN_Driver_Library_Rel3.0.0`  

Flash with jlink:  
`west flash --runner jlink` 

Flash with custom openocd:  
`west flash --openocd-search ~/MaximSDK/Tools/OpenOCD/scripts/ --openocd ~/MaximSDK/Tools/OpenOCD/openocd`  
### Check Output
`sudo picocom -b 115200 /dev/ttyACM0`  

### Update Zephyr SDK Env
`export ZEPHYR_TOOLCHAIN_VARIANT=zephyr`  
