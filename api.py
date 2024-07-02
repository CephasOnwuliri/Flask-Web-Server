Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, request, jsonify
... import requests
... from ipdata import ipdata
... 
... app = Flask(__name__)
... 
... @app.route('/api/hello')
... def hello():
...     visitor_name = request.args.get('visitor_name', 'Guest')
...     client_ip = request.remote_addr
...     
...     # Use ipdata to get location info
...     ipdata_client = ipdata.IPData('your_api_key_here')
...     response = ipdata_client.lookup(client_ip)
...     
...     city = response.get('city', 'Unknown')
...     
...     # Get temperature data
...     weather_api_key = 'your_weather_api_key_here'
...     weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'
...     weather_response = requests.get(weather_url).json()
...     temperature = weather_response['main']['temp']
...     
...     return jsonify({
...         'client_ip': client_ip,
...         'location': city,
...         'greeting': f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {city}"
...     })
... 
... if __name__ == '__main__':
