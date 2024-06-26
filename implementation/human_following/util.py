import RPi.GPIO as GPIO
GPIO.setwarnings(False)

import os, time

edgetpu=0 # If Coral USB Accelerator connected, then make it '1' otherwise '0'

# Motor pins
m1_1 = 8
m1_2 = 11
m2_1 = 9  
m2_2 = 25  

def init_gpio():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(m1_1,GPIO.OUT)
	GPIO.setup(m1_2,GPIO.OUT)
	GPIO.setup(m2_1,GPIO.OUT)
	GPIO.setup(m2_2,GPIO.OUT)

def cleanup_gpio():
	GPIO.cleanup()

def back():
    GPIO.output(m1_1, False)
    GPIO.output(m1_2, True)
    GPIO.output(m2_1, True)
    GPIO.output(m2_2, False)
    
def right():
	print("right")
	GPIO.output(m1_1, True)
	GPIO.output(m1_2, False)
	GPIO.output(m2_1, True)
	GPIO.output(m2_2, False)

def left():
	print("left")
	GPIO.output(m1_1, False)
	GPIO.output(m1_2, True)
	GPIO.output(m2_1, False)
	GPIO.output(m2_2, True)
	
def forward():
	print("forward")
	GPIO.output(m1_1, True)
	GPIO.output(m1_2, False)
	GPIO.output(m2_1, False)
	GPIO.output(m2_2, True)
	
def stop():
	print("stopped")
	GPIO.output(m1_1, False)
	GPIO.output(m1_2, False)
	GPIO.output(m2_1, False)
	GPIO.output(m2_2, False)
