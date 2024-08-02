# Sensor Data Code Collecting:
import Adafruit_DHT
import time
import Adafruit_ADS1x15

# Initialize sensors
dht_sensor = Adafruit_DHT.DHT22
dht_pin = 4
adc = Adafruit_ADS1x15.ADS1115()

# Sensor reading function
def read_sensors():
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
    bp = adc.read_adc(0, gain=1)  # Placeholder for actual BP sensor reading
    heart_rate = adc.read_adc(1, gain=1)  # Placeholder for actual heart rate sensor reading
    return temperature, humidity, bp, heart_rate

# Main loop
while True:
    temp, hum, bp, hr = read_sensors()
    print(f"Temperature: {temp:.2f} C, Humidity: {hum:.2f}%, BP: {bp}, Heart Rate: {hr}")
    time.sleep(2)

