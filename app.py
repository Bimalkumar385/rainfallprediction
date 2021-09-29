from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/predict', methods=["POST" , "GET"])
def predict():
        b = []
        if request.method == "POST":
            Year = np.int32(request.form['year'])

            Month = np.int32(request.form['month'])

            Day = np.int32(request.form['day'])

            MinTemp = np.float32(request.form['mintemp'])

            MaxTemp = np.float32(request.form['maxtemp'])

            Humidity9am = np.float32(request.form['humidity9'])

            Humidity3pm = np.float32(request.form['humidity3'])

            Pressure9am = np.float32(request.form['pressure9'])

            Pressure3pm = np.float32(request.form['pressure3'])

            Temp9am = np.float32(request.form['temp9'])

            Temp3pm = np.float32(request.form['temp3'])

            WindSpeed9am = np.float32(request.form['wind9'])

            WindSpeed3pm = np.float32(request.form['wind3'])

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

