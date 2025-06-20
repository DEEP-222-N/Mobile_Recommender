# Mobile Recommendation System

Live Demo

https://mobile-recommender-jmwz.onrender.com/

Mobile Recommendation System
The Mobile Recommendation System is a personalized web application that helps users find smartphones that best match their preferences. Built using Flask for the backend and a clean, responsive frontend with HTML and CSS, this project uses a K-Nearest Neighbors (KNN) model to recommend phones based on specifications such as budget, RAM, storage, and battery capacity.

Key Features
User-Driven Input
Users can enter specific preferences like budget, RAM size, internal storage, and battery capacity. The app processes these inputs and suggests smartphones that are most aligned with the user’s needs.

KNN-Based Recommender System
At the core of the application is a content-based filtering approach using the K-Nearest Neighbors algorithm. It identifies the most similar phones from a dataset by comparing user input with existing phone features using distance metrics. The goal is to return relevant and practical options rather than generic suggestions.

Clean Web Interface
The app is lightweight and intuitive, offering a simple form-based input system and displaying results in an organized, user-friendly manner. The UI is designed to ensure a smooth and distraction-free experience.

Preprocessed and Scaled Dataset
The recommendation engine is trained on a structured dataset of mobile phone specifications. All features were preprocessed and scaled to ensure accurate distance calculations by the KNN model.

Technology Stack
Python – for model development and backend logic

Pandas, NumPy – for data handling and preprocessing

Scikit-learn – for building and applying the KNN recommender

Flask – to serve the model through a web application

HTML, CSS – for the frontend design and layout

Pickle – for saving the model, scaler, and dataset objects

How It Works
The user accesses the homepage and fills in desired phone specifications.

The input is scaled using the same transformation applied to the training data.

The KNN model finds the closest matches from the dataset based on similarity.

The top recommended phones are presented with details for each.
