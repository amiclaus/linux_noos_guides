### Documentation
`https://docs.zephyrproject.org/latest/develop/getting_started/index.html`  
### Build Commands
`west build -t menuconfig`  
`west build -b nucleo_f446re samples/hello_world`  
`west -v build -p always -c -b nucleo_f413zh samples/sensor/adt7420/`  
`west flash`  

### Check Output
`sudo picocom -b 115200 /dev/ttyACM0`  

### Update Zephyr SDK Env
`export ZEPHYR_TOOLCHAIN_VARIANT=zephyr`  
