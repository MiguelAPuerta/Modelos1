from flask import Flask, jsonify, request
from train import train_model
from predict import predict_model

app = Flask(__name__)

train_status = "not training"
predict_status = "not predicting"
    
@app.route("/")
def hello_world():
    return jsonify({"Hello": "World"})

@app.route("/status")
def status():
    return jsonify({"training status": train_status}, {"predicting status": predict_status})

@app.route("/predict", methods=['POST'])
def predict():
    if predict_status == "training":
        return jsonify({"error": "already training"}), 400

    data = request.json
    input_file = data.get("input_file")
    prediction_file = data.get("prediction_file")
    model_file = data.get("model_file")
    clean = data.get("clean", True)

    if not input_file:
        return jsonify({"error": "Missing required parameters: input_file"}), 400
    
    if not model_file:
        return jsonify({"error": "Missing required parameters: model_file"}), 400

    predict_model(input_file, prediction_file, model_file, clean)

    return jsonify({"Prediction Complete. Saved predictions to ": prediction_file})

@app.route("/train", methods=["POST"])
def train():
    if train_status == "training":
        return jsonify({"error": "already training"}), 400

    data = request.json
    data_file = data.get("data_file")
    model_file = data.get("model_file")
    clean = data.get("clean", True)

    if not data_file:
        return jsonify({"error": "Missing required parameters: data_file"}), 400

    train_model(data_file, model_file, clean)

    return jsonify({"Training Complete, new model created. Saved to ": model_file})

if __name__ == "__main__":
    app.run(debug=True)