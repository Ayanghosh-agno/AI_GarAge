import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT,initial=GPIO.HIGH	)
GPIO.setup(18, GPIO.OUT,initial=GPIO.HIGH	)
#Provide your IBM Watson Device Credentials
organization = "vp695w"
deviceType = "Ayan1"
deviceId = "123456"
authMethod = "token"
authToken = "12345678"

# Initialize GPIO

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        print(type(cmd.data))
        i=cmd.data['command']
        if i=='LIGHTON':
                print("light is on")
                GPIO.output(12, GPIO.LOW)

        elif i=='LIGHTOFF':
                print("light is off")
                GPIO.output(12, GPIO.HIGH)
        elif i=='DOORON':
                print("DOOR is oN")
                GPIO.output(18, GPIO.LOW)
        
        elif i=='DOOROFF':
                print("DOOR is off")
                GPIO.output(18, GPIO.HIGH)
        
        

try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)#.............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:   
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
