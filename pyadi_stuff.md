#### Environment Variables:
`export PYTHONPATH=/usr/lib/python3.9/site-packages/:$PYTHONPATH`  
#### Testing:
`sudo python3 -m pytest --color yes -vs test/test_adxl313.py --uri="serial:/dev/ttyACM0" --hw=ADXL314`
#### Checking commits:
`sudo pre-commit run --all-files`
#### IIO Generate XML:
`iio-emu_gen_xml ip:10.48.65.134 > test/emu/devices/ad4851.xml`
