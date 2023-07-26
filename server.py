from flask import Flask, render_template, request
from weather import get_condition
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    # return "Hello World!"
    return render_template("index.html")

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    # Check if input is empty or only having spaces
    if not bool(city.strip()):
        city = "Kolkata"

    weather_data = get_condition(city)
    if not weather_data['cod'] == 200 :
        return render_template("not-found.html")

    return render_template(
        "weather.html",
        status = weather_data["weather"][0]["description"].capitalize(),
        title = weather_data["name"],
        temp = f'{weather_data["main"]["temp"]}',
        feels_like = f'{weather_data["main"]["feels_like"]}'
    )


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port="8000")
    serve(app, host="0.0.0.0", port="8000")