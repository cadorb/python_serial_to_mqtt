#!/usr/bin/python
import time
import serial
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

#brokerIp = "193.70.0.25"
#brokerPort = "1334"

brokerIp = "10.3.5.41"
brokerPort = 1883

color = ""
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0,  parity=serial.PARITY_EVEN, rtscts=1)
print("Writing on %s..." % ser.name)

while(1):
  msg = subscribe.simple("/iot", qos=0, msg_count=1, retained=False, hostname=brokerIp, port=brokerPort, client_id="", keepalive=60, will=None, auth=None, tls=None, protocol=mqtt.MQTTv311)

  msgcolor = msg.payload
  
  if(len(msgcolor) == 1):
    print msgcolor
    if(msgcolor == "3"):
      color = "r"
    if(msgcolor == "9"):
      color = "b"
    if(msgcolor == "E"):
      color = "y"
    if(msgcolor == "D"):
      color = "w"
print color
ser.write(color)
 
time.sleep(1)
