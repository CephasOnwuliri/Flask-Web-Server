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
...     ipdata_client = ipdata.IPData('8f81b3ee4b0d59aefb2ea7d7b0b569d9800e7944b2ecbd1396606c3e
')
...     response = ipdata_client.lookup(client_ip)
...     
...     city = response.get('city', 'Unknown')
...     
...     # Get temperature data
...     weather_api_key = '27e8308f9f2c4372e1904d96152d5229'
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
