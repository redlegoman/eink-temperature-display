#!/usr/bin/python
import sys
#sys.path.append('/home/andy/dev/e-Paper/RaspberryPi_JetsonNano/python/lib/waveshare_epd/')
sys.path.append("/home/andy/dev/e-Paper/RaspberryPi_JetsonNano/python")
import os
import time
import epd2in13d


#from lib.waveshare_epd import epd2in13d



from PIL import Image, ImageDraw, ImageFont


try:   
   sys.argv[1:] # do something with sys.argv[1:]  
except IndexError:  
   print("usage is...")
   sys.exit()


if len(sys.argv) == 1:
    # Print usage...
    print("usage")
    sys.exit()


textin = sys.argv[1]
pic_dir = '/home/andy/dev/e-Paper/RaspberryPi_JetsonNano/python/pic' # Points to pic directory .
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
    font62 = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 35)

    imagein = Image.new(mode='1', size=(w, h), color=255)
    #imagein = Image.new(mode='1', size=(h, w), color=255)
    drawin = ImageDraw.Draw(imagein)
    #drawin.text((0, 0), '99.9', font=font62, fill=0, align='left')
    drawin.text((0, 10), textin, font=font62, fill=0, align='left')


    #print("display..")
    #display.display(display.getbuffer(imageb),display.getbuffer(imager))
    display.display(display.getbuffer(imagein))
    #print("display.. done")


except IOError as e:
    print(e)
