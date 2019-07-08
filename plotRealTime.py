import serial
import datetime
import time
from matplotlib import pyplot as plt
from drawnow import *

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

temp1 = []
temp2 = []
analog = []
volts = []
pco2 = []

plt.ion()
cnt = 0

def makeFig(): #Create a function that makes our desired plot

    plt.subplot(211)
    plt.grid(True)

   # plt.ylim(0,50)
    plt.title("Temperatura")
    plt.plot(temp1, label = "Temperatura 1")
    plt.plot(temp2, label = "Temperatura 2")
    plt.legend(loc='upper left')
    #plt.xlim(0,50)

    plt.subplot(212)
    plt.grid(True)

    plt.title("pco2")
    plt.plot(pco2)
   # plt.xlim(0,50)

    plt.subplot(321)
    plt.legend(loc='upper left')
    plt.plot(temp2, label='Temp 2')
    

while True:
    lines = ser.readline().rstrip()
    dataSerial = lines.decode('ascii').split(',')
    if (len(dataSerial)> 1):
        temp1.append(float(dataSerial[2]))
        temp2.append(float(dataSerial[3]))
        # analog.append(float(dataSerial[4]))
        # volts.append(float(dataSerial[5]))
        pco2.append(float(dataSerial[4]))
    
    drawnow(makeFig)
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing  
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        temp1.pop(0)                       #This allows us to just see the last 50 data points
        temp2.pop(0)
        pco2.pop(0)
    print(temp1)
    print(temp1)
    print(temp1)
    print(cnt)
    time.sleep(1)

#Humidity = 44.56%, temp_h = 28.37F, Pressure = 100603.50Pa, temp_p = 27.56F, light_lvl = 1.48V, VinPin = 4.20V
