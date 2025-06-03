from flask import Flask, request,render_template
import requests

app = Flask(__name__)

API_KEY = "88bd79ae2c961c9054775827d3d49f33"

@app.route('/',methods=['GET','POST'])
def index():
    weather={}
    if request.method == 'POST':
        city= request.form['city' ]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url).json()
        if res.get("cod")!= 200:
            weather= {'error':res.get("message","city not found")}
        else:
            weather = {
                'city': city.title(),
                'temp': res['main']['temp'],
                'condition': res['weather'][0]['description'].title(),
                'humidity': res['main']['humidity']
            }
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)