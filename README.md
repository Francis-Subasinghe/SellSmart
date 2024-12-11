SellSmart: Predicting Retail Sales with Machine Learning
SellSmart is a cutting-edge project that leverages machine learning to predict retail sales accurately. This project serves as a learning initiative and a demonstration of modern software development, machine learning, and deployment workflows.
________________________________________
Key Features
•	Data Preprocessing: Clean and prepare raw retail data for training.
•	Machine Learning: Train and deploy a Random Forest Regressor model.
•	Flask API: A REST API to serve predictions.
•	Streamlit Frontend: A user-friendly interface for interactive predictions.
•	Cloud Integration: Deployment and hosting on AWS with Ngrok integration for testing.
•	MLflow: Experiment tracking and model management.
________________________________________
Technologies Used
1.	Python: Core programming language.
2.	Flask: Backend API framework.
3.	Streamlit: Interactive frontend framework.
4.	MLflow: Machine learning experiment tracking.
5.	Docker: Containerization for consistent deployment.
6.	AWS EC2: Cloud hosting environment.
7.	Ngrok: Remote API access.
8.	pandas: Data manipulation and preprocessing.
9.	scikit-learn: Machine learning modeling and evaluation.
________________________________________
Challenges and Learnings
1.	Dependency Conflicts: Overcame Python version mismatches and library dependency errors.
2.	Cloud Deployment: Gained experience setting up and debugging AWS EC2 instances.
3.	Frontend-Backend Integration: Learned effective communication between API and frontend applications.
4.	Error Debugging: Resolved numerous runtime and deployment errors with persistence and research.
________________________________________
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
________________________________________
Future Enhancements
1.	Refined Deployment: Explore Kubernetes or AWS Lambda for scalable deployments.
2.	Advanced Frontend: Build a dynamic React-based frontend.
3.	Power BI Integration: Visualize predictions and insights directly in Power BI.
4.	Enhanced Features: Add user authentication and advanced analytics.

