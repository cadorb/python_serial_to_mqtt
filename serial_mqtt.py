#!/usr/bin/python
import time
import serial
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
color = ""
ser = serial.Serial('/dev/ttyACM1', 9600, timeout=0,  parity=serial.PARITY_EVEN, rtscts=1)
print("Listening on %s..." % ser.name)

while(1):
  s = ser.read(100)
  if(len(s) == 1):
    print s
    if(s == "3"):
      color = "RED"
    if(s == "9"):
      color = "BLUE"
    if(s == "E"):
      color = "YELLOW"
    if(s == "D"):
      color = "WHITE"
    publish.single("/iot", payload=color, qos=0, retain=False, hostname="10.3.5.41", port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None, protocol=mqtt.MQTTv311, transport="tcp")
  time.sleep(1)
