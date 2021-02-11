#!/bin/bash
CURWD=$(dirname $0)
if [[ -f $CURWD/include.sh ]]
then
  . $CURWD/include.sh
else
  echo "include.sh missing - copy include.example.sh?"
  exit 1
fi
TMP=/tmp/show.txt
LOG=/dev/null
DDIR=/sys/bus/w1/devices
THISHOST=$(/bin/hostname)

DALLASES="$DDIR/28-*/w1_slave"

NUM=1
for DALLAS in $DALLASES
do
  CRC="NO"
  while [[ $CRC == "NO" ]]
  do
    cat $DALLAS > $TMP
    cat $TMP >> $LOG
    CRC=$(cat $TMP|grep crc|awk '{print $12}')
    GOTDALLASINSIDE=$(cat $TMP | tail -1|awk -F"=" '{print $2}')
    GOTDALLASINSIDE=$(echo "scale=1 ; $GOTDALLASINSIDE / 1000.00"|/usr/bin/bc)
    TEMP[${NUM}]=$GOTDALLASINSIDE
  done
  NUM=$(expr $NUM + 1 )
done
rm $TMP >/dev/null 2>&1

TEMP_IN=${TEMP[1]}

_curl="/usr/bin/curl"
TEMP_OUT="$(${_curl} -q -s -k ${URL} )"
echo "$TEMP_OUT $TEMP_IN"
DISPLAY=$DIR/display.py
if [[ $1 = "f" ]]
then
  /usr/bin/python $DISPLAY $TEMP_OUT $TEMP_IN f
else 
  /usr/bin/python $DISPLAY $TEMP_OUT $TEMP_IN 
fi


