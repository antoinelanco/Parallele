import sys
import time
import binascii
import RPi.GPIO as GPIO

gplist = [6,12,16,17,4,23,18,22,21,20]
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
            if ifZero(data):
                print "zero"
                print res
                sys.exit(0)
            res = res+ArrayBinToChar(data)
            print res
            GPIO.output(gplist[8],GPIO.HIGH)


def ArrayBinToChar(tab):
    print "test"
    res = tab[0]+tab[1]+tab[2]+tab[3]+tab[4]+tab[5]+tab[6]+tab[7]
    print res
    n = int(res, 2)
    print "test"+str(n)
    return binascii.unhexlify('%x' % n)

def ifZero(tab):
    res = 0
    i=0
    while i<8:
        res = res + int(tab[i])
        i=i+8
    if res == 0:
        return True
    else:
        return False

try:
    Parallele()
except KeyboardInterrupt:
    GPIO.cleanup()
