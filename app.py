from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS class
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "https://cardio-care-frontend.vercel.app"}})  # Allow requests from localhost:3000

# Load your trained machine learning model
model = joblib.load('./heart_disease_pred.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get input data from the request

    # Convert the data to a Pandas DataFrame
    input_df = pd.DataFrame(data['features'], columns=[
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
    ])

    # Process the features and make predictions using the model
    prediction = model.predict(input_df)

    # Return the prediction as JSON response
    response = {'prediction': prediction.tolist()}
    output = response["prediction"][0]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
