import sys
import time
import binascii
import RPi.GPIO as GPIO

gplist = [1,2,3,4,5,6,7,8,26,20]
data = [0,0,0,0,0,0,0,0]
GPIO.setmode(GPIO.BCM)
#init data
i=0
while i<8:
    GPIO.setup(gplist[i], GPIO.IN)
    i=i+1
#init sync
GPIO.setup(gplist[9], GPIO.IN)
GPIO.setup(gplist[8], GPIO.OUT, initial=GPIO.HIGH)

def Parallele():
    res = ''
    while 1:
        if GPIO.input(gplist[9]):
            print "transfert"
            GPIO.output(gplist[8],GPIO.LOW)
            a=0
            while a<8:
                data[a]=str(GPIO.input(gplist[a]))
                a=a+1
            res = res+ArrayBinToChar(data)
            print res
            GPIO.output(gplist[8],GPIO.HIGH)

def ArrayBinToChar(tab):

    res = tab[0]+'b'+tab[1]+tab[2]+tab[3]+tab[4]+tab[5]+tab[6]+tab[7]
    n = int(res, 2)
    return binascii.unhexlify('%x' % n)


try:
    Parallele()
except KeyboardInterrupt:
    GPIO.cleanup()
