**Mount Drive:**  
`sudo mount -t drvfs E: /mnt/e`  
**Unmount:**  
`sudo umount /mnt/e`  
**Serial Port Bind:**
In Windows Powershell:  
`usbipd list`  
`usbipd bind --busid 2-7`  
`usbipd attach --wsl --busid 2-7`  
