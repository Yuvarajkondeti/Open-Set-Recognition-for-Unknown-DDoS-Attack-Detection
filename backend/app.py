import os
import torch
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from model import CNN, osr_decision

app = Flask(__name__)
CORS(app)

# ================= PATH FIX =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "saved_model", "cnn_model.pth")

# ================= MODEL =================
INPUT_FEATURES = 79  # 80 columns minus Label

model = CNN(INPUT_FEATURES)
model.load_state_dict(
    torch.load(MODEL_PATH, map_location=torch.device("cpu"))
)
model.eval()

# Dummy class centers for OSR (simplified RPL)
class_centers = [
    torch.zeros(64),
    torch.ones(64)
]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    x = torch.tensor(data, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

    _, features = model(x)
    label, distance = osr_decision(features[0], class_centers)

    return jsonify({
        "prediction": label,
        "distance": round(distance, 4)
    })

if __name__ == "__main__":
    app.run(debug=True)
