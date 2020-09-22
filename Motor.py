import sys
import time
import RPi.GPIO as GPIO

Forward=37
Backward=38

def Setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Forward, GPIO.OUT)
	GPIO.setup(Backward, GPIO.OUT)

def forward(x):
  GPIO.output(Forward, GPIO.HIGH)
  GPIO.output(Backward, GPIO.LOW)
  print("Moving Forward")
  time.sleep(x)
  GPIO.output(Forward, GPIO.LOW) 
  
def reverse(x):
  GPIO.output(Backward, GPIO.HIGH)
  GPIO.output(Forward, GPIO.LOW)
  print("Moving Backward")
  time.sleep(x)
  GPIO.output(Backward, GPIO.LOW)

def BuildVoltageForward(x):
  for x in range(3):
    GPIO.output(Forward, GPIO.HIGH)
    print("High")
    time.sleep(0.5)
    GPIO.output(Forward, GPIO.LOW)
    print("Low")
    time.sleep(0.25)
    
  GPIO.output(Forward, GPIO.HIGH)
  time.sleep(0.3)
  
def BuildVoltageBackWards(x):
  for x in range(6):
    GPIO.output(Backward, GPIO.HIGH)
    print("High")
    time.sleep(0.5)
    GPIO.output(Backward, GPIO.LOW)
    print("Low")
    time.sleep(0.25)

  GPIO.output(Backward, GPIO.HIGH)
  time.sleep(0.5)
  
def Stop():
   GPIO.output(Backward, GPIO.LOW)
   GPIO.output(Forward, GPIO.LOW)
   GPIO.cleanup()
  
def Commands(command, time):
	Setup()
	
	if 'forward' in command:
		BuildVoltageForward(time)
	if 'backwards' in command:
		BuildVoltageBackWards(time)
	
	Stop()
   
def Clean():
   GPIO.cleanup()
 
