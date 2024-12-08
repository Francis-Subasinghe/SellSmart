
from flask import Flask, request, jsonify
import pandas as pd
import mlflow.pyfunc

# Load the MLflow model
model = mlflow.pyfunc.load_model("mlruns/0/0/329f09c3c0324af79f00cecbd57f4fc2/artifacts/model")  # Replace <run_id> with your actual run ID

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the SellSmart Prediction API!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse JSON input
        input_data = request.get_json()
        input_df = pd.DataFrame(input_data)

        # Validate input
        if input_df.empty:
            return jsonify({"error": "Input data is empty"}), 400

        # Make predictions
        predictions = model.predict(input_df)
        return jsonify({"predictions": predictions.tolist()})
    except KeyError as e:
        return jsonify({"error": f"Missing required column: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__AC":
    app.run(host="0.0.0.0", port=5000)
