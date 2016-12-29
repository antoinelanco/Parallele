import socket, sys
import time
import sys
import RPi.GPIO as GPIO
import urllib
import threading
import os as os

gplist = [1,2,3,4,5,6,7,8,9,10]
GPIO.setmode(GPIO.BCM)
#init data
i=0
while i<8:
    GPIO.setup(gplist[i], GPIO.OUT)
    i=i+1
#init sync
GPIO.setup(gplist[9], GPIO.IN)
GPIO.setup(gplist[8], GPIO.OUT, initial=GPIO.LOW)

#repondre avec des "" ex : "antoine"
def Parallele():
    try:
        text = list(input('Your text (format "text"): '))
    except NameError:
        print 'Error format : "text"'
        GPIO.cleanup()
        sys.exit(0)
    count = 0
    while count<len(text):
        data = charToArrayBin(text[count])
        if GPIO.input(gplist[9]):
            a=1
            while a<8:
                GPIO.ouput(gplist[a-1],data[a])
                a=a+1
            GPIO.output(gplist[8],GPIO.HIGH)
            count=count+1


def charToArrayBin(char):
    L = list(bin(ord(char)))
    L[1]=L[0]
    return L
    #index 1 a 8




try:
    Parallele()
except KeyboardInterrupt:
    GPIO.cleanup()