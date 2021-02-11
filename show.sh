#!/bin/bash
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
  #echo "TEMP${NUM} = ${TEMP[$NUM]} "
  NUM=$(expr $NUM + 1 )
done
rm $TMP >/dev/null 2>&1

TEMP_IN=${TEMP[1]}

TEMP_OUT=$(/usr/bin/curl -q -s -k https://rlmn.co/temperature/)

echo "$TEMP_OUT $TEMP_IN"
DISPLAY=/home/andy/dev/e-Paper/RaspberryPi_JetsonNano/python/display.py
/usr/bin/python $DISPLAY $TEMP_OUT $TEMP_IN


