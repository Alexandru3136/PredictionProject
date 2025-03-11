from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Încărcăm modelul antrenat
model = joblib.load("predictor_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    home_goals = data["home_goals"]
    away_goals = data["away_goals"]

    # Pregătim datele pentru predicție
    input_data = pd.DataFrame([[home_goals, away_goals]], columns=["Home Goals", "Away Goals"])
    prediction = model.predict(input_data)[0]

    # Interpretăm rezultatul
    result = "Egal" if prediction == 0 else "Gazde câștigă" if prediction == 1 else "Oaspeți câștigă"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
