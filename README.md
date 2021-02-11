e-ink temperature display

display.py accepts two numbers: outside temperature and inside temperature

if a third param is set to "f" then the display does a full refresh rather than ap partial refresh, which can get messy after a while

example: display.py -0.1 22.2

to doa full refresh:
example: display.py -0.1 22.2 f

a wrapper script which I use to get tempertures from a ds18b20 attached to the Pi and a local URL which delivers the outside temperature is called "show.sh"
syntax:
show.sh [f]
the "f" executes a full refresh
