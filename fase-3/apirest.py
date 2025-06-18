from flask import Flask, jsonify, request
from train import train_model
from predict import predict_model

app = Flask(__name__)

global train_status
global predict_status
train_status = "not training"
predict_status = "not predicting"
    
@app.route("/")
def hello_world():
    return jsonify({"Hello": "World"})

@app.route("/status")
def status():
    return jsonify({
        "training status": train_status,
        "predicting status": predict_status
        })

@app.route("/predict", methods=['POST'])
def predict():
    if predict_status == "predicting":
        return jsonify({"error": "already predicting"}), 400

    input_file = request.files["input_file"]

    model_file = request.form.get("model_file", "model.pkl")
    prediction_file = request.form.get("prediction_file", "prediction.csv")
    clean = request.form.get("clean", "true").lower() == "true"

    if not input_file:
        return jsonify({"error": "Missing required parameters: input_file"}), 400
    
    if not model_file:
        return jsonify({"error": "Missing required parameters: model_file"}), 400

    predict_model(input_file, prediction_file, model_file, clean)

    return jsonify({
        "Prediction Complete. Saved predictions to ": prediction_file
        })

@app.route("/train", methods=["POST"])
def train():
    if train_status == "training":
        return jsonify({"error": "already training"}), 400

    data_file = request.files["data_file"]
    model_file = request.form.get("model_file", "model.pkl")
    clean = request.form.get("clean", "true").lower() == "true"

    if not data_file:
        return jsonify({"error": "Missing required parameters: data_file"}), 400

    train_model(data_file, model_file, clean)

    return jsonify({"Training Complete, new model created. Saved to ": model_file,})

if __name__ == "__main__":
    app.run(debug=True)