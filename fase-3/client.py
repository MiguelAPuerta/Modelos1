import requests


# Train
# Open the CSV file you want to upload
with open('train.csv', 'rb') as f:
    # Prepare multipart/form-data payload
    files = {
        'data_file': f  # field name must match Flask's `request.files['data_file']`
    }

    data = {
        'model_file': 'model.pkl',    # Just a name for the output model file
        "clean": True                 # optional; defaults to True
    }

    # Send POST request to the Flask server
    response = requests.post('http://localhost:5001/train', files=files, data=data)

    # Print the response
    try:
        print("Server response:", response.status_code, response.json())
    except Exception as e:
        print("Failed to parse JSON:", e)
        print("Raw response:", response.text)


# Predict
# Open the files
with open('test.csv', 'rb') as f:
    files = {
        'input_file': f,           # path to input CSV
    }

    data = {
        'model_file': "model.pkl",              # previously trained model path
        "prediction_file": "prediction.csv",    # desired output file path
        "clean": True                           # Optional form field
    }

    response = requests.post('http://localhost:5001/predict', files=files, data=data)

    try:
        print("Server response:", response.status_code, response.json())
    except Exception as e:
        print("Failed to parse JSON:", e)
        print("Raw response:", response.text)