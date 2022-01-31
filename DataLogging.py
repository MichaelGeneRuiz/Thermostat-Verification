import pigpio
import DHT22
from time import sleep
from datetime import datetime

pi = pigpio.pi()

dht22 = DHT22.sensor(pi, 23)
dht22.trigger()

sleepTime = 3

def readDHT22():
    dht22.trigger()
    
    humidity = '%.2f' % (dht22.humidity())
    temp = '%.2f' % ((dht22.temperature() * 1.8) + 32)
    return (humidity, temp)

for i in range(10):
    
    now = datetime.now()
    
    humidity, temperature = readDHT22()
    
    f = open("/home/pi/Desktop/TempHumidProj/Logs/logfile.txt", "a")
    
    dt_string = now.strftime(now.strftime("%m/%d/%y  %H:%M:%S"))
    f.write(dt_string+"\n")
    f.write("Humidity is: " + humidity + "%\n")
    f.write("Temperature is: " + temperature + u"\N{DEGREE SIGN}"+"F\n")
    
    f.close()
    
    print("Temp/Humidity "+ str(i+1) + " is recorded.")
    
    sleep(sleepTime)
    
f = open("/home/pi/Desktop/TempHumidProj/Logs/logfile.txt", "a")
f.write("\n")
f.close()
