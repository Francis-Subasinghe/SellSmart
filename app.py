!pip install pyngrok
from flask import Flask, request, jsonify
from pyngrok import ngrok
import pandas as pd
import mlflow.pyfunc

!ngrok authtoken 2P1COQyv8ThEv0HpisRjiPCRVQj_f8JFBXFvcXtxcBCidXf9

# Load the MLflow model
model = mlflow.pyfunc.load_model("/content/mlruns/0/329f09c3c0324af79f00cecbd57f4fc2/artifacts/model")  # Replace <run_id> with your actual Run ID

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Sales Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON
        input_data = request.get_json()
        input_df = pd.DataFrame(input_data)

        # Make predictions
        predictions = model.predict(input_df)
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    # Expose the Flask app using ngrok
    public_url = ngrok.connect(5000, "http")
    print(f"Your app is available at {public_url}")


    # Start the Flask app
    app.run(port=5000)
