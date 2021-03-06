#!/usr/bin/python
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
import time
import epd2in13d
#from lib.waveshare_epd import epd2in13d
from PIL import Image, ImageDraw, ImageFont, ImageOps
from datetime import datetime

if len(sys.argv) == 1:
    # Print usage...
    print("usage: ",sys.argv[0], " <temp out> <temp in> [f]")
    print("   eg: ",sys.argv[0], " -0.7 22.2")
    print("   eg: ",sys.argv[0], " -0.7 22.2 f # if a full refresh is required")
    sys.exit()

print("(temp_out)arg1 = " + sys.argv[1])
print("(temp_in)arg2 = " + sys.argv[2])


temp_out = sys.argv[1]
temp_in = sys.argv[2]

temp_out = float(temp_out)
format(temp_out, '.1f')
temp_out=str(temp_out)
temp_in = float(temp_in)
format(temp_in, '.1f')
temp_in=str(temp_in)

#print("---")
#print(temp_out)
#print("---")
#
if len(sys.argv) > 3:
    fullrefresh = sys.argv[3]
else:
    fullrefresh = 'p'
pic_dir = dir_path+'/pic' # Points to pic directory .
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
    fonttime = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 10)
    fontnum = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 55)

    # width: 212
    #height: 104
    imagein = Image.new(mode='1', size=(W, H), color=255)
    drawin = ImageDraw.Draw(imagein)
    drawin.rectangle([(106,0),(212,104)],fill = 0)

    draw = ImageDraw.Draw(imagein)

    # INSIDE TEMP NUM
    w, h = drawin.textsize(temp_in,font=fontnum)
    #drawin.text( (((W/2)-w)/2, ((H/2)-(h/2))  ), temp_in, fill=0, font=fontnum)
    drawin.text( (((W/2)-w)/2, 0  ), temp_in, fill=0, font=fontnum)

    # THE WORD 'inside'
    w, h = drawin.textsize('inside',font=fonttext)
    drawin.text((0, 80), 'inside', font=fonttext, fill=0)

    # OUTSIDE TEMP NUM
    w, h = drawin.textsize(temp_out,font=fontnum)
    #drawin.text(   ( ((W/2)+(W/4))-(w/2), ((H/2)-(h/2))   ), temp_out, fill=1, font=fontnum)
    drawin.text(   ( ((W/2)+(W/4))-(w/2), (H-h)-10   ), temp_out, fill=1, font=fontnum)

    # THE WORD 'outside'
    w, h = drawin.textsize('outside',font=fonttext)
    drawin.text(((W-w), 0), 'outside', font=fonttext, fill=1)


    # THE TIME 
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)
    w, h = drawin.textsize(current_time,font=fonttime)
    #drawin.text(((H-w)/2, ((W-h)/2)+10), current_time, font=fonttime, fill=1)
    drawin.text((0, 0), current_time, font=fonttime, fill=0)


    # ACTUALLY PRINT EVERYTHING TO SCREEN:
    im_flip = ImageOps.flip(imagein)
    im_mirror = ImageOps.mirror(im_flip)
    #display.display(display.getbuffer(imagein))
    if(fullrefresh == "f"):
      print("full refresh")
      display.display(display.getbuffer(im_mirror))
    else:
      print("partial refresh")
      display.DisplayPartial(display.getbuffer(im_mirror))


except IOError as e:
    print(e)
