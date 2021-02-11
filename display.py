#!/usr/bin/python
import os
import time
from lib.waveshare_epd import epd2in13d


from PIL import Image, ImageDraw, ImageFont

import sys

try:   
   sys.argv[1:] # do something with sys.argv[1:]  
except IndexError:  
   print("usage is...")
   sys.exit()


if len(sys.argv) == 1:
    # Print usage...
    print("usage")
    sys.exit()

print("(temp_out)arg1 = " + sys.argv[1])
print("(temp_in)arg2 = " + sys.argv[2])

temp_out = sys.argv[1]
temp_in = sys.argv[2]
pic_dir = 'pic' # Points to pic directory .
degree_sign= u'\N{DEGREE SIGN}'

try:
    # Display init, clear
    display = epd2in13d.EPD()
    #display.init(display.lut_full_update)
    display.init()
    #display.Clear()
    w = display.height
    h = display.width
    #print('width:', w)
    #print('height:', h)
    ### ... IMAGE CODE ... ###
    #body = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 18, index=5)
    font15 = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 20)
    font62 = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 55)

    #imagein = Image.new(mode='1', size=(w, h), color=255)
    imagein = Image.new(mode='1', size=(h, w), color=255)
    drawin = ImageDraw.Draw(imagein)
    drawin.rectangle([(0,106),(104,212)],fill = 0)
    #drawin.text((0, 0), '99.9', font=font62, fill=0, align='left')
    drawin.text((0, 10), temp_in, font=font62, fill=0, align='left')
    drawin.text((0, 80), 'inside', font=font15, fill=0, align='left')

    #drawin.text((0, 107), '-0.9', font=font62, fill=1, align='left')
    drawin.text((0, 117), temp_out, font=font62, fill=1, align='left')
    drawin.text((0, 188), 'outside', font=font15, fill=1, align='left')


    #print("display..")
    #display.display(display.getbuffer(imageb),display.getbuffer(imager))
    display.display(display.getbuffer(imagein))
    #print("display.. done")


except IOError as e:
    print(e)
