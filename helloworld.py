import os
import time
from lib.waveshare_epd import epd2in13d


from PIL import Image, ImageDraw, ImageFont
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
    print('width:', w)
    print('height:', h)
    ### ... IMAGE CODE ... ###
    #body = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 18, index=5)
    font15 = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 15)
    font62 = ImageFont.truetype(os.path.join(pic_dir, 'Font.ttc'), 55)

    #imagein = Image.new(mode='1', size=(w, h), color=255)
    imagein = Image.new(mode='1', size=(h, w), color=255)
    drawin = ImageDraw.Draw(imagein)
    drawin.rectangle([(0,106),(104,212)],fill = 0)
    drawin.text((0, 0), '99.9', font=font62, fill=0, align='left')
    drawin.text((0, 85), 'inside', font=font15, fill=0, align='left')

    drawin.text((0, 107), '-0.9', font=font62, fill=1, align='left')
    drawin.text((0, 193), 'outside', font=font15, fill=1, align='left')


    print("display..")
    #display.display(display.getbuffer(imageb),display.getbuffer(imager))
    display.display(display.getbuffer(imagein))
    print("display.. done")


except IOError as e:
    print(e)
