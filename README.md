Disease Prediction System
A Machine Learning-based web application that predicts possible diseases based on user-input symptoms.

Project Overview:
This project uses a trained machine learning model to analyze symptoms provided by the user and predict the most likely disease.
It helps in early detection and provides quick insights for better decision-making.

Features:
Predicts disease based on symptoms
Uses Machine Learning (Random Forest Classifier)
Data preprocessing and label encoding
Model evaluation using accuracy
Interactive web app using Streamlit
Fast predictions using saved (pickled) model

Tech Stack:
Python
Pandas
NumPy
Scikit-learn
Streamlit
Pickle

How It Works:
1. Data Preprocessing:
Load dataset using Pandas
Remove unwanted columns
Split into features (X) and target (y)
Encode target labels using LabelEncoder 
2. Model Training:
Use RandomForestClassifier
Split data using train_test_split
Train model on training data
3. Model Evaluation:
Evaluate using accuracy score
Optional: Confusion Matrix visualization
4. Model Saving:
Save trained model using pickle
Load model for future predictions
5. Deployment (Streamlit):
User selects symptoms
Model predicts disease
Output displayed on UI
