SellSmart
Predicting Retail Sales with Machine Learning

SellSmart is a machine learning-powered API for retail sales prediction. This project demonstrates an end-to-end workflow including data preprocessing, model training, deployment using Flask, and tracking with MLflow.

Features
Data Preprocessing: Cleans and transforms raw retail data for model training.
Machine Learning Model: Trains a Random Forest Regressor for accurate sales prediction.
MLflow Integration: Tracks experiments, logs parameters, and monitors model metrics for easy evaluation.
Flask API: Exposes endpoints for predicting sales based on input data.
Dockerized Deployment: Containerizes the application for consistent deployment across environments.
Scalable: Easily extendable to run on cloud platforms like AWS or Google Cloud.
Technologies Used
Python: Core programming language.
Flask: For building the RESTful API.
MLflow: For experiment tracking and model logging.
pandas: For data preprocessing and manipulation.
scikit-learn: For model training and evaluation.
Docker: To containerize the application.
Ngrok: For exposing the local app to a public URL for testing.
Setup Instructions
Prerequisites
Python 3.8 or above
Git
Docker (optional, but recommended for production-like deployment)
Virtual environment setup (optional, but recommended)
1. Clone the Repository
bash
Copy code
git clone https://github.com/Francis-Subasinghe/SellSmart.git
cd SellSmart
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the Flask App Locally
bash
Copy code
python app.py
4. Docker Setup (Optional)
Build and run the app using Docker:

bash
Copy code
docker build -t sellsmart-app .
docker run -p 5000:5000 sellsmart-app
5. Access the API
Locally: http://127.0.0.1:5000
Using Ngrok: Public URL provided by Ngrok.
API Endpoints
1. Welcome Message
URL: /
Method: GET
Response:
json
Copy code
{
  "message": "Welcome to the Sales Prediction API!"
}
2. Predict Sales
URL: /predict
Method: POST
Request Body (JSON):
json
Copy code
[
  {
    "Row ID": 1,
    "Postal Code": 42420,
    "Quantity": 2,
    "Discount": 0.0,
    "Profit": 41.91,
    "Year": 2016,
    "Month": 11,
    "Day": 8
  }
]
Response:
json
Copy code
{
  "predictions": [279.38]
}
Folder Structure
graphql
Copy code
SellSmart/
│
├── data/
│   ├── raw/                # Raw data files
│   ├── processed/          # Processed data files
│
├── scripts/                # Custom scripts for preprocessing and analysis
│
├── app.py                  # Flask API code
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── README.md               # Project documentation
└── mlruns/                 # MLflow experiment tracking folder
Contributing
Contributions are welcome! Feel free to:

Fork this repository
Submit issues
Create pull requests
License
This project is licensed under the MIT License.

Contact
Author: Francis Subasinghe
Email: imeshshenal1222@gmail.com
