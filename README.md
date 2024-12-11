SellSmart: Predicting Retail Sales with Machine Learning
SellSmart is a cutting-edge project that leverages machine learning to predict retail sales accurately. This project serves as a learning initiative and a demonstration of modern software development, machine learning, and deployment workflows.

Key Features
Data Preprocessing: Clean and prepare raw retail data for training.
Machine Learning: Train and deploy a Random Forest Regressor model.
Flask API: A REST API to serve predictions.
Streamlit Frontend: A user-friendly interface for interactive predictions.
Cloud Integration: Deployment and hosting on AWS with Ngrok integration for testing.
MLflow: Experiment tracking and model management.
Technologies Used
Python: Core programming language.
Flask: Backend API framework.
Streamlit: Interactive frontend framework.
MLflow: Machine learning experiment tracking.
Docker: Containerization for consistent deployment.
AWS EC2: Cloud hosting environment.
Ngrok: Remote API access.
pandas: Data manipulation and preprocessing.
scikit-learn: Machine learning modeling and evaluation.
Challenges and Learnings
Dependency Conflicts: Overcame Python version mismatches and library dependency errors.
Cloud Deployment: Gained experience setting up and debugging AWS EC2 instances.
Frontend-Backend Integration: Learned effective communication between API and frontend applications.
Error Debugging: Resolved numerous runtime and deployment errors with persistence and research.
How to Use the Project
1. Clone the Repository
bash
Copy code
git clone https://github.com/Francis-Subasinghe/SellSmart.git
cd SellSmart
2. Set up the Environment
bash
Copy code
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Run the Flask App
bash
Copy code
python app.py
4. Run the Streamlit Frontend
bash
Copy code
streamlit run streamlit_app.py
Future Enhancements
Refined Deployment: Explore Kubernetes or AWS Lambda for scalable deployments.
Advanced Frontend: Build a dynamic React-based frontend.
Power BI Integration: Visualize predictions and insights directly in Power BI.
Enhanced Features: Add user authentication and advanced analytics.
