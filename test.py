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

print(temp_out)



