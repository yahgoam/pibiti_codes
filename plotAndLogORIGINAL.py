import serial
import datetime
import time
from matplotlib import pyplot as plt
from drawnow import *

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

time.sleep(3)

humidity = []
temp = []
pressure = []
temp2 = []
light = []


plt.ion()
cnt = 0

def makeFig(): 

    plt.subplot(221)
    plt.grid(True)
    plt.title("Humidade")
    plt.plot(humidity)
    plt.legend(loc='upper left')


    plt.subplot(222)
    plt.grid(True)
    plt.title("Temperatura")
    plt.plot(temp)


    plt.subplot(223)
    plt.grid(True)
    plt.title("Pressao")
    plt.plot(pressure)


    plt.subplot(224)
    plt.grid(True)
    plt.title("Intensidade de Luz")
    plt.plot(light)

    

while True:
    lines = ser.readline().rstrip()
    if lines[0] == '1':
            dataSerial = lines.split(',')

            if (len(dataSerial)> 1):
                humidity.append(float(dataSerial[1]))
                temp.append(float(dataSerial[2]))
                pressure.append(float(dataSerial[3]))
                #temp2.append(float(dataSerial[3]))
                light.append(float(dataSerial[5]))

        
                drawnow(makeFig)
                plt.pause(.000001)                     
                cnt=cnt+1
                if(cnt>50):                           
                    humidity.pop(0)                      
                    temp.pop(0)
                    pressure.pop(0)
                    light.pop(0)

                print(humidity)
                print(temp)
                print(pressure)
                print(light)

    #log
    lines = ser.readline().decode('ascii')
    logFile = open("logFile.csv","a")
    logFile.write(str(lines))
    logFile.close()
    #end log
    time.sleep(1)