import sys
import time
import RPi.GPIO as GPIO

forward=37
backward=38

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(forward, GPIO.OUT)
	GPIO.setup(backward, GPIO.OUT)

def forward(x):
  GPIO.output(forward, GPIO.HIGH)
  GPIO.output(backward, GPIO.LOW)
  print("Moving forward")
  time.sleep(x)
  GPIO.output(forward, GPIO.LOW) 
  
def reverse(x):
  GPIO.output(backward, GPIO.HIGH)
  GPIO.output(forward, GPIO.LOW)
  print("Moving backward")
  time.sleep(x)
  GPIO.output(backward, GPIO.LOW)

def build_voltage_forward(x):
  for x in range(3):
    GPIO.output(forward, GPIO.HIGH)
    print("High")
    time.sleep(0.5)
    GPIO.output(forward, GPIO.LOW)
    print("Low")
    time.sleep(0.25)
    
  GPIO.output(forward, GPIO.HIGH)
  time.sleep(0.3)
  
def build_voltage_backwards(x):
  for x in range(6):
    GPIO.output(backward, GPIO.HIGH)
    print("High")
    time.sleep(0.5)
    GPIO.output(backward, GPIO.LOW)
    print("Low")
    time.sleep(0.25)

  GPIO.output(backward, GPIO.HIGH)
  time.sleep(0.5)
  
def stop():
   GPIO.output(backward, GPIO.LOW)
   GPIO.output(forward, GPIO.LOW)
   GPIO.cleanup()
  
def commands(command, time):
	Setup()
	
	if 'forward' in command:
		build_voltage_forward(time)
	if 'backwards' in command:
		build_voltage_backwards(time)
	
	Stop()
   
def clean():
   GPIO.cleanup()
 
