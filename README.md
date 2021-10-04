# micropython-esp32-spi-sdcard-and-screen-driver
Proof of concept of Pure micropython espidf SPI driver for sdcard and screen at the same SPI bus (example: with ILI9XXX.py driver)

Tested on my M5 CORE 2 with lv_Micropython 1.15.

Notes:
- The SPI screen driver need to be called first
- Half_duplex not supported
- Do not forget to set power on to the SD card first

Example usage on ESP8266 / ESP32:

    import machine, sdcard, os
    sd = sdcard.SDCard(machine.SPI(1), machine.Pin(15))
    os.mount(sd, '/sd')
    print(os.listdir('/'))

Example usage on ESP32 with ili93XXX.py screen driver:

    import machine, sdcard, os
    from ili9XXX import ili9341
    lcd = ili9341(mosi=23, miso=38, clk=18, dc=15, cs=5, invert=True, rot=0x10, width=320, height=240,
                 rst=-1, power=-1, backlight=-1, half_duplex=False) # half_duplex do not work with SDCard    
    sd = sdcard.SDCard(sdcard.SPI(), machine.Pin(4))
    os.mount(sd, "/sd")
    print(os.listdir('/sd'))
