from flask import Flask, request
import requests

app = Flask(__name__)

API_KEY="9fcaadd2c9463b0e25e553bc94ef5248"

@app.route('/')
def home():
    return '''
    <h1>Weather App</h1>

    <form action="/weather">
        <input type="text" name="city" placeholder="Enter city">
        <button type="submit">Get Weather</button>
    </form>
    '''

@app.route('/weather')
def weather():
    city = request.args.get('city')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] != 200:
        return str(data)

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"""
    <h1>Weather in {city}</h1>
    <p>Temperature: {temp} °C</p>
    <p>Description: {desc}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)