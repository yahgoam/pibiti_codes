import serial 
import time

ser=serial.Serial('/dev/ttyACM1', 9600)

if ser.isOpen():
    ser.close()
ser.open()
ser.isOpen()
time.sleep(2)
word_arduino = '1'
ser.write(word_arduino.encode())
time.sleep(1)
line = ser.readline()

print(line.decode("ascii"))

# local_time = time.localtime(time.time())
# #time.struct_time(tm_year=2019, tm_mon=7, tm_mday=2, tm_hour=16, tm_min=29, tm_sec=0, tm_wday=1, tm_yday=183, tm_isdst=0)
#str(local.tm_hour) +':'+ str(local.tm_min)
# print(local_time)
#Humidity = 44.56%, temp_h = 28.37F, Pressure = 100603.50Pa, temp_p = 27.56F, light_lvl = 1.48V, VinPin = 4.20V
