#### Environment Variables:
`export PYTHONPATH=/usr/lib/python3.9/site-packages/:$PYTHONPATH`  
#### Testing:
`sudo python3 -m pytest --color yes -vs test/test_adxl313.py --uri="serial:/dev/ttyACM0" --hw=ADXL314`
