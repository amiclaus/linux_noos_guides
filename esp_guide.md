#### ESP-AT Documentation:
https://docs.espressif.com/projects/esp-at/en/latest/esp32/  
#### ESP-AT How to Compile:
https://docs.espressif.com/projects/esp-at/en/latest/esp32/Compile_and_Develop/How_to_clone_project_and_compile_it.html  
#### ESP-IDF Documentation:
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html  
#### ESP-AT Version:
`git clone -b v2.4.0.0 --recursive https://github.com/espressif/esp-at.git`  

### Custom Flash Guide

Full Documentation at: https://docs.espressif.com/projects/esp-at/en/latest/esp32/Compile_and_Develop/How_to_clone_project_and_compile_it.html  

1. Clone ESP-AT v2.4.0.0: `git clone -b v2.4.0.0 --recursive https://github.com/espressif/esp-at.git`  
2. Change to the repository directory: `cd esp-at`  
3. `./build.py install` -> Select Platform: ESP32 (Option 1) -> Select Module: WROOM-32 (Option 1) -> Select Silence Mode (Option 1)  
4. `./build.py menuconfig`  
   -> (Top) -> Compiler options -> Optimization Level -> Enable (X) Optimize for size (-Os)  
   -> (Top) -> Component config -> AT -> Disable [ ] AT ble command support.  
   -> (Top) -> Component config -> AT -> Disable [ ] AT ble hid command support.  
   -> (Top) -> Component config -> AT -> Disable [ ] AT blufi command support.  
   -> (Top) -> Component config -> AT -> Disable [ ] AT bt command support.  
6. Modify AT Command Port Pins to UART0  
   (https://docs.espressif.com/projects/esp-at/en/latest/esp32/Compile_and_Develop/How_to_set_AT_port_pin.html#modify-command-port-pins)  
   -> Edit `components/customized_partitions/raw_data/factory_param/factory_param_data.csv`  
   -> Set PLATFORM_ESP32 WROOM-32 `uart_port: 0`, `uart_tx_pin: 22`, `uart_rx_pin: 23`, `uart_cts_pin: -1`, `uart_rts_pin: -1`  
8. `./build.py build`  
9. `./build.py -p (PORT) flash` (replace PORT with your serial port name, for example `/dev/ttyACM0`)  

### Flash Firmware Release

Documentation on how to flash:  
https://docs.espressif.com/projects/esp-at/en/latest/esp32/Get_Started/Downloading_guide.html#linux-or-macos  

Steps:  
`pip install esptool==4.3` (latest version should work also)  
`wget https://github.com/amiclaus/linux_noos_guides/releases/download/release/ESP32-WROOM-32-AT-NINA-W102.zip`  
`unzip ESP32-WROOM-32-AT-NINA-W102.zip -d  "$(basename -s .zip ESP32-WROOM-32-AT-NINA-W102.zip)"`  
`cd ESP32-WROOM-32-AT-NINA-W102`  
`esptool.py --chip auto --port PORTNAME --baud 115200 --before default_reset --after hard_reset write_flash -z download.config`  
(Replace `download.config` with the content inside the file found in ESP32-WROOM-32-AT-NINA-W102 folder)  

#### Auxiliary hex file for entering boot mode

`wget https://github.com/amiclaus/linux_noos_guides/releases/download/release/flash_nina.hex`  
