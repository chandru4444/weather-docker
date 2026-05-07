from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "9fcaadd2c9463b0e25e553bc94ef5248"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/weather')
def weather():
    city = request.args.get('city')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] != 200:
        return "City not found"

    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

    return render_template("index.html", weather=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)