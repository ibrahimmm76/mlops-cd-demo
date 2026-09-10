from flask import Flask, jsonify, request

app = Flask(__name__)
MODEL_VERSION = "1.0"

@app.route("/")
def home():
    return jsonify({
        "service": "mlops-demo",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "model_version": MODEL_VERSION
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "value" not in data:
        return jsonify({"error": "Missing 'value' field"}), 400
    try:
        value = float(data["value"])
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input: 'value' must be a number"}), 400

    # ML dummy prediction logic
    prediction = value * 2
    return jsonify({
        "input": value,
        "prediction": prediction,
        "model_version": MODEL_VERSION
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)