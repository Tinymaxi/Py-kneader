import Adafruit_DHT
import time
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 21
 

humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
if humidity is not None and temperature is not None:
    x = str("Temp={0:0.1f}C Hum={1:0.1f}%".format(temperature, humidity))
else:
    x = str("Sensor failure. Check wiring.");
 
    
    
