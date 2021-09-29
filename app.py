from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/predict', methods=["POST" , "GET"])
def predict():
        b = []
        if request.method == "POST":
            Year = request.form['year']

            Month = request.form['month']

            Day = request.form['day']

            MinTemp = request.form['mintemp']

            MaxTemp = request.form['maxtemp']

            Humidity9am = request.form['humidity9']

            Humidity3pm = request.form['humidity3']

            Pressure9am = request.form['pressure9']

            Pressure3pm = request.form['pressure3']

            Temp9am = request.form['temp9']

            Temp3pm = request.form['temp3']

            WindSpeed9am = request.form['wind9']

            WindSpeed3pm = request.form['wind3']

            b.extend([ Year, Month, Day, MinTemp, MaxTemp, Humidity9am, Humidity3pm,
                      Pressure9am, Pressure3pm, Temp9am, Temp3pm, WindSpeed9am, WindSpeed3pm])
            model = joblib.load("static/RainForestModel.pkl")
            try:
                y_pred = model.predict([b])
                return render_template('prediction.html', msg="success", op=y_pred)
            except:
                return render_template('prediction.html')
        return render_template('prediction.html')

if __name__ == '__main__':
    app.run()

