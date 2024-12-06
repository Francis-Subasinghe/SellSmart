# SellSmart
SellSmart
Predicting Retail Sales with Machine Learning
SellSmart is a machine learning-powered API for retail sales prediction. This project demonstrates end-to-end data preprocessing, model training, and deployment using Flask and MLflow.

Features
Data Preprocessing: Cleans and transforms raw retail data for model training.
Machine Learning Model: Trains a Random Forest Regressor for sales prediction.
MLflow Integration: Logs experiments, parameters, and model metrics for tracking and evaluation.
Flask API: Provides an endpoint to predict sales based on input data.
Scalable Deployment: Can be extended to run on cloud platforms like AWS or Google Cloud.
Technologies Used
Python: Core programming language.
Flask: For building the RESTful API.
MLflow: For experiment tracking and model logging.
pandas: For data preprocessing and manipulation.
scikit-learn: For model training and evaluation.
Ngrok: For testing the API remotely.
Setup Instructions
Prerequisites
Python 3.8 or above
Git
Virtual environment setup (optional but recommended)
1. Clone the Repository
bash
Copy code
git clone https://github.com/Francis-Subasinghe/SellSmart.git
cd SellSmart
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the Flask App
bash
Copy code
python app.py
4. Access the API
The app runs locally on http://127.0.0.1:5000.
If using ngrok, a public URL will be provided.
API Endpoints
1. Welcome Message
URL: /
Method: GET
Response:

json

{
  "message": "Welcome to the Sales Prediction API!"
}
2. Predict Sales
URL: /predict
Method: POST
Request Body (JSON):

json

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
├── README.md               # Project documentation
└── mlruns/                 # MLflow experiment tracking folder
Contributing
Feel free to fork this repository, submit issues, or make pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.

Contact
Author: Francis Subasinghe
Email: imeshshenal1222@gmail.com
GitHub: Francis-Subasinghe
