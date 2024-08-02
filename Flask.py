from flask import Flask, jsonify
import Adafruit_DHT
import Adafruit_ADS1x15

app = Flask(__name__)

# Initialize sensors
dht_sensor = Adafruit_DHT.DHT22
dht_pin = 4
adc = Adafruit_ADS1x15.ADS1115()

@app.route('/data')
def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
    bp = adc.read_adc(0, gain=1)  # Placeholder for actual BP sensor reading
    heart_rate = adc.read_adc(1, gain=1)  # Placeholder for actual heart rate sensor reading
    data = {
        'temperature': temperature,
        'humidity': humidity,
        'bp': bp,
        'heart_rate': heart_rate
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
