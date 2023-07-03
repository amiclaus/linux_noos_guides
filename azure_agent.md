#### Documentation:
`https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/v2-linux?view=azure-devops`  
#### Miscellaneous Stuff
5.2.194.157  
`~/Desktop/azure_agent/run.sh`  
VNCViewer: 192.168.1.30:5900 (public wifi)  
Start server: `sudo x11vnc -forever -loop -noxdamage -repeat -rfbauth /home/azure/.vnc/passwd -shared`  
`export BUILD_DIR=~/Desktop/builds/build_xilinx_ad7134_fmc_zed`  
`python3 tools/scripts/build_projects.py -builds_dir ~/Desktop/builds -project ad713x_fmcz -build_name iio .`  
