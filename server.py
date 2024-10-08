# this is a flask instance/app that will be running on our server
# it is also commonly named as main.py 

from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve


# this makes our app a flask app
app = Flask(__name__)

# define routes that you ll be accessing on the web

@app.route('/')
@app.route('/index')
# unlike weather page, our index page is not receiving any data like title, status
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    # here weather_data is the json data object containing all the weather info of the city from the openWeather API

    # check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Mumbai"

    weather_data = get_current_weather(city)
     # if we enter an invalid city, then accessing name, weather[0] etc from the json data would raise an error,the json data will only have {'cod': '404', 'message': 'city not found'}
    
    if not weather_data['cod'] == 200:
        return render_template("city_not_found.html")
    return render_template(
        "weather.html",
        title = weather_data["name"], #getting the city name from the json data object of the api 
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}"
    )

# run the file

if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port=8000,  expose_tracebacks=True)



