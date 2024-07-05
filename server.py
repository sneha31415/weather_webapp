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
def index():
    return "welcome to my weather app"

# run the file

if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port=8000)