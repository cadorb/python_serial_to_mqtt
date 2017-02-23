#!/usr/bin/python
import time
import serial
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

#brokerIp = "193.70.0.25"
#brokerPort = "1334"

brokerIp = "10.3.5.41"
brokerPort = 1883

color = ""
ser = serial.Serial('/dev/ttyACM1', 9600, timeout=0,  parity=serial.PARITY_EVEN, rtscts=1)
print("Listening on %s..." % ser.name)

#s = "3"

while(1):
  s = ser.read(100)
  if(len(s) == 1):
    print s
    if(s == "3"):
      color = "r"
    if(s == "9"):
      color = "b"
    if(s == "E"):
      color = "y"
    if(s == "D"):
      color = "w"
    publish.single("/iot", payload=color, qos=0, retain=False, hostname=brokerIp, port=brokerPort, client_id="", keepalive=60, will=None, auth=None, tls=None, protocol=mqtt.MQTTv311, transport="tcp")
  time.sleep(1)
