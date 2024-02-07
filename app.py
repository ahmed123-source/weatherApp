from flask import Flask, jsonify, request, render_template
import logging
from flask_caching import Cache
from getWeather import OpenWeatherMap

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up caching
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

"""
@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    weather_data = OpenWeatherMap.get_weather(city)
    if 'error' in weather_data:
        return jsonify(weather_data), 500
    #print(city)
    return jsonify(weather_data)
"""

@app.route('/weather', methods=['GET', 'POST'])
@cache.cached(timeout=300,key_prefix=lambda: request.get_json()['city'])
def get_weather():
    # Get the user request 
    data = request.get_json()
    city = data.get('city','')
    print(city)
    if not city:
        logger.error("City not provided in the request.")
        return jsonify({"error": "City not provided"}), 400  # Bad Request 
    logger.info(f"Request received for weather in {city}.") 

    weather_data = OpenWeatherMap.get_weather(city)
    if 'error' in weather_data:
        logger.error(f"Error in retrieving weather data: {weather_data['error']}")
        return jsonify(weather_data), 500
    #print(city)
    return jsonify(weather_data)

@app.route('/weatherApp')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
