import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
while True:
    lines = ser.readline().decode('ascii')
    print(str(lines))
    logFile = open("logFile.csv","a")
    logFile.write(str(lines))
    logFile.close()

#Humidity = 44.56%, temp_h = 28.37F, Pressure = 100603.50Pa, temp_p = 27.56F, light_lvl = 1.48V, VinPin = 4.20V
