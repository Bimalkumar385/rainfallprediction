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
            Year = int(request.form['year'])

            Month = int(request.form['month'])

            Day = int(request.form['day'])

            MinTemp = float(request.form['mintemp'])

            MaxTemp = float(request.form['maxtemp'])

            Humidity9am = float(request.form['humidity9'])

            Humidity3pm = float(request.form['humidity3'])

            Pressure9am = float(request.form['pressure9'])

            Pressure3pm = float(request.form['pressure3'])

            Temp9am = float(request.form['temp9'])

            Temp3pm = float(request.form['temp3'])

            WindSpeed9am = float(request.form['wind9'])

            WindSpeed3pm = float(request.form['wind3'])

            b.extend([ Year, Month, Day, MinTemp, MaxTemp, Humidity9am, Humidity3pm,
                      Pressure9am, Pressure3pm, Temp9am, Temp3pm, WindSpeed9am, WindSpeed3pm])
            model = joblib.load("static/RainForestModel.pkl")
            try:
                y_pred = model.predict([b])
                return render_template('prediction.html', msg="success", op=y_pred)
            except:
                pass
        return render_template('prediction.html',msg="unsuccess")

if __name__ == '__main__':
    app.run()

