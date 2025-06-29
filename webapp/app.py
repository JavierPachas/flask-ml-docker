from flask import Flask, request, jsonify, render_template
from flask.logging import create_logger
import logging
import traceback
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    LOG.info("Scaling Payload...")
    scaler = StandardScaler().fit(payload)
    return scaler.transform(payload)

@app.route("/")

def home():
    return "<h3>Sklearn Prediction Container</h3>"

@app.route("/predict", methods=['POST'])
def predict():
    try:
        clf = joblib.load("california_housing_prediction.joblib")
    except Exception as e:
        LOG.error("Error loading model: %s", str(e))
        LOG.error("Exception traceback: %s", traceback.format_exc())
        return "Model not loaded", 500

    json_payload = request.get_json()
    LOG.info("Received JSON payload: %s", json_payload)

    expected_keys = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
    if not all(key in json_payload for key in expected_keys):
        return jsonify({"error": "Missing one or more input features"}), 400

    input_df = pd.DataFrame([json_payload])
    LOG.info("Inference payload DataFrame:\n%s", input_df)

    scaled_payload = scale(input_df)
    prediction = list(clf.predict(scaled_payload))
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)