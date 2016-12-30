import sys
import time
import RPi.GPIO as GPIO

gplist = [6,12,16,17,4,23,18,22,19,26]
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
            while a<9:
                print str(a)+" : "+data[a]+" : "+str(gplist[a-1])
                GPIO.output(gplist[a-1],int (data[a]))
                a=a+1
            GPIO.output(gplist[8],GPIO.HIGH)
            count=count+1
    # time.sleep(1)
    # while 1:
    #     if GPIO.input(gplist[9]):
    #         a=0
    #         while a<8:
    #             GPIO.output(gplist[a],GPIO.LOW)
    #             a=a+1
    #         GPIO.output(gplist[8],GPIO.HIGH)
    #         sys.exit(0)


def charToArrayBin(char):
    L = list(bin(ord(char)))
    L[1]=L[0]
    return L
    #index 1 a 8




try:
    Parallele()
except KeyboardInterrupt:
    GPIO.cleanup()
