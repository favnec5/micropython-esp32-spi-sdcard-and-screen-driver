# micropython-esp32-spi-sdcard-and-screen-driver
Proof of concept of Pure micropython espidf SPI driver for sdcard and screen at the same SPI bus (example: with ILI9XXX.py driver)
Tested on my M5 CORE 2 with lv_Micropython 1.15.

Notes:
- The SPI screen driver need to be called first
- Half_duplex not supported
- Do not forget to set power on to the SD card first

