#!/usr/bin/python
import sys
#sys.path.append('/home/andy/dev/e-Paper/RaspberryPi_JetsonNano/python/lib/waveshare_epd/')
sys.path.append("/home/andy/dev/e-Paper/RaspberryPi_JetsonNano/python")
import os
import time
import epd2in13d
#from lib.waveshare_epd import epd2in13d
from PIL import Image, ImageDraw, ImageFont

if len(sys.argv) == 1:
    # Print usage...
    print("usage: ",sys.argv[0], " <temp out> <temp in>")
    print("   eg: ",sys.argv[0], " -0.7 22.2")
    sys.exit()

print("(temp_out)arg1 = " + sys.argv[1])
print("(temp_in)arg2 = " + sys.argv[2])

temp_out = sys.argv[1]
temp_in = sys.argv[2]
pic_dir = '/home/andy/dev/e-Paper/RaspberryPi_JetsonNano/python/pic' # Points to pic directory .
degree_sign= u'\N{DEGREE SIGN}'

try:
    # Display init, clear
    display = epd2in13d.EPD()
    #display.init(display.lut_full_update)
    display.init()
    #display.Clear()
    W = display.height
    H = display.width
    print('screen width:', W)
    print('screen height:', H)
    ### ... IMAGE CODE ... ###
    fonttext = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 20)
    fontnum = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 55)

    # width: 212
    #height: 104
    imagein = Image.new(mode='1', size=(H, W), color=255)
    drawin = ImageDraw.Draw(imagein)
    drawin.rectangle([(0,106),(104,212)],fill = 0)
    #drawin.text((0, 0), '99.9', font=fontnum, fill=0, align='left')
    x = 0
    y = 10

    draw = ImageDraw.Draw(imagein)
    #drawin.text(((H-w)/2,(W-h)/2), temp_in, fill=0)
    w, h = drawin.textsize(temp_in,font=fontnum)
    drawin.text(((H-w)/2,10), temp_in, fill=0, font=fontnum)

    w, h = drawin.textsize('inside',font=fonttext)
    #drawin.text(((H-w)/2, 80), 'inside', font=fonttext, fill=0)
    drawin.text((0, 80), 'inside', font=fonttext, fill=0)

    #drawin.text((0, 107), '-0.9', font=fontnum, fill=1, align='left')
    #drawin.text((0, 117), temp_out, font=fontnum, fill=1, align='left')
    w, h = drawin.textsize(temp_out,font=fontnum)
    drawin.text(((H-w)/2,117), temp_out, fill=1, font=fontnum)
    #drawin.text((0, 188), 'outside', font=fonttext, fill=1, align='left')

    w, h = drawin.textsize('outside',font=fonttext)
    #drawin.text(((H-w)/2, 188), 'outside', font=fonttext, fill=1)
    drawin.text(((H-w), 188), 'outside', font=fonttext, fill=1)

    #print("display..")
    #display.display(display.getbuffer(imageb),display.getbuffer(imager))
    display.display(display.getbuffer(imagein))
    #print("display.. done")


except IOError as e:
    print(e)
