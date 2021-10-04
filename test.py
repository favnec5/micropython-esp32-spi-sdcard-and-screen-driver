"""
 Esp32 sdcard.py driver test on M5stack Core2 with ili9341 driver at the same SPI bus
 note : half_duplex=False needed
"""

import lvgl as lv
import os
import utime
from machine import Pin


lv.init()

# Power Management
import axp192
import m5core2_power
power=m5core2_power.Power()

# LCD screen
from ili9XXX import ili9341
lcd = ili9341(mosi=23, miso=38, clk=18, dc=15, cs=5, invert=True, rot=0x10, width=320, height=240,
              rst=-1, power=-1, backlight=-1, half_duplex=False)

# Touch sensor
from ft6x36 import ft6x36
touch = ft6x36(width=320, height=280)  


# SdCard
import sdcard
#sd = sdcard.SDCard(sdcard.SPI(mosi=23, miso=38, clk=18), Pin(4)) # without screen
sd = sdcard.SDCard(sdcard.SPI(), Pin(4))
os.mount(sd, "/sd")
print(os.listdir('/sd'))


def test(e):
    f=open('sd/test','w+')
    for i in range(51):
        length = f.write(str(i))
        testLabel.set_text(str(i*2)+"%")
        print("writed:",str(i)+'('+str(length)+')')        
    f.close()
    print("final size:", os.stat('sd/test')[6])


scr=lv.scr_act()
btn=lv.btn(scr)
btn.center()
label=lv.label(btn)
label.set_text('Start card SD test')
btn.add_event_cb(test, lv.EVENT.CLICKED, None)

testLabel=lv.label(scr)
testLabel.set_text("_")
testLabel.align(lv.ALIGN.CENTER,0,40)

lv.scr_load(scr)
