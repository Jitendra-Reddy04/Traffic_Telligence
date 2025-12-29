from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# LOAD SAVED MODEL OBJECTS
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
holiday_encoder = pickle.load(open("holiday_encoder.pkl", "rb"))
weather_encoder = pickle.load(open("weather_encoder.pkl", "rb"))


# HOME ROUTE
@app.route("/")
def home():
    return render_template("index.html")


# PREDICTION ROUTE
@app.route("/predict", methods=["POST"])
def predict():
    try:
        holiday = request.form["holiday"]
        temp = float(request.form["temp"])
        rain = float(request.form["rain"])
        snow = float(request.form["snow"])
        weather = request.form["weather"]

        day = int(request.form["day"])
        month = int(request.form["month"])
        year = int(request.form["year"])
        hours = int(request.form["hours"])
        minutes = int(request.form["minutes"])

        holiday_enc = holiday_encoder.transform([holiday])[0]
        weather_enc = weather_encoder.transform([weather])[0]

        input_data = np.array([[
            temp,
            rain,
            snow,
            day,
            month,
            year,
            hours,
            minutes,
            0,         
            holiday_enc,
            weather_enc
        ]])
        input_scaled = scaler.transform(input_data)

        #  Prediction 
        prediction = model.predict(input_scaled)[0]

        return render_template(
            "output.html",
            result=f"Estimated Traffic Volume: {int(prediction)} vehicles/hour"
        )

    except Exception as e:
        return render_template(
            "output.html",
            result=f"Error occurred: {str(e)}"
        )


# RUN APP
if __name__ == "__main__":
    app.run(debug=True)
