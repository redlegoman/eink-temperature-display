e-ink temperature display

uses the library found here : https://github.com/waveshare/e-Paper

I used a wavershare 2.13 e-Ink display purchased from The PiHut : https://thepihut.com/collections/raspberry-pi-display-hats/products/three-colour-2-13-eink-display-phat-red-black-white

display.py accepts two numbers: outside temperature and inside temperature  
if a third param is set to "f" then the display does a full refresh rather than a partial refresh, which can get messy after a while.

```display.py -0.1 22.2
```

to do a full refresh:

```display.py -0.1 22.2 f
```

a wrapper script which I use to get tempertures from a ds18b20 attached to the Pi and a local URL which delivers the outside temperature is called "show.sh"
syntax:

```show.sh [f]
```

the "f" executes a full refresh
