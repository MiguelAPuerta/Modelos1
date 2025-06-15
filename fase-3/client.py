import requests

# Train
# Define the JSON body
payload = {
    'data_file': "train.csv",
    "model_file": "model.pkl",               # previously trained model path
    "clean": True                            # optional; defaults to True
}

# Send POST request
endpoint = 'http://localhost:5001/train'
response = requests.post(endpoint, json=payload)

# Print response
print("train", response.json())


# Predict
# Define the JSON body
payload = {
    "input_file": "test.csv",          # path to input CSV on the server
    "prediction_file": "prediction.csv",    # desired output file path
    "model_file": "model.pkl",               # previously trained model path
    "clean": True                            # optional; defaults to True
}

# Send POST request
endpoint = 'http://localhost:5001/predict'
response = requests.post(endpoint, json=payload)

# Print response
print("predict", response.json())