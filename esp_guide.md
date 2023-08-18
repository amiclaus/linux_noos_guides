#### ESP-AT Documentation:
`https://docs.espressif.com/projects/esp-at/en/latest/esp32/`  
#### ESP-AT How to Compile:
`https://docs.espressif.com/projects/esp-at/en/latest/esp32/Compile_and_Develop/How_to_clone_project_and_compile_it.html`  
#### ESP-IDF Documentation:
`https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html`  
#### ESP-AT Version:
`git clone -b v2.4.0.0 --recursive https://github.com/espressif/esp-at.git`  

### Custom Flash Guide

Full Documentation at: `https://docs.espressif.com/projects/esp-at/en/latest/esp32/Compile_and_Develop/How_to_clone_project_and_compile_it.html`  

1. Clone ESP-AT v2.4.0.0: `git clone -b v2.4.0.0 --recursive https://github.com/espressif/esp-at.git`  
2. Change to the repository directory: `cd esp-at`  
3. `./build.py install` -> Select Platform: ESP32 (Option 1) -> Select Module: WROOM-32 (Option 1) -> Select Silence Mode (Option 1)  
4. `./build.py menuconfig` -> (Top) -> Compiler options -> Optimization Level -> Enable (X) Optimize for size (-Os)  
                           -> (Top) -> Component config -> AT -> Disable [ ] AT ble command support.  
                           -> (Top) -> Component config -> AT -> Disable [ ] AT ble hid command support.  
                           -> (Top) -> Component config -> AT -> Disable [ ] AT blufi command support.  
                           -> (Top) -> Component config -> AT -> Disable [ ] AT bt command support.  
5. `./build.py build`  
6. `./build.py -p (PORT) flash` (replace PORT with your serial port name, for example `/dev/ttyACM0`)  
