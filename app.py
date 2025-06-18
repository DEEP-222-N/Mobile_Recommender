from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model, scaler, and dataset
with open("knn_model.pkl", "rb") as f:
    knn, scaler, df_filtered = pickle.load(f)

# Dropdown options
companies = sorted(df_filtered['Company Name'].dropna().unique().tolist())
rams = sorted(df_filtered['RAM_GB'].dropna().unique().astype(int).tolist())
storages = sorted(df_filtered['Storage_GB'].dropna().unique().astype(int).tolist())
batteries = sorted(df_filtered['Battery Capacity(mAh)'].dropna().unique().astype(int).tolist())
rear_cams = sorted(df_filtered['Back Cam Primary (MP)'].dropna().unique().astype(int).tolist())
front_cams = sorted(df_filtered['Front Cam Primary (MP)'].dropna().unique().astype(int).tolist())

@app.route('/')
def home():
    return render_template(
        'index.html',
        companies=companies,
        rams=rams,
        storages=storages,
        batteries=batteries,
        rear_cams=rear_cams,
        front_cams=front_cams
    )

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from form
        user_input = [
            float(request.form['price']),
            float(request.form['ram']),
            float(request.form['storage']),
            float(request.form['battery']),
            float(request.form['back_cam']),
            float(request.form['front_cam']),
        ]

        selected_company = request.form.get('company')

        # Get KNN predictions
        user_scaled = scaler.transform([user_input])
        distances, indices = knn.kneighbors(user_scaled)
        recommendations = df_filtered.iloc[indices[0]]

        # Show only selected company results if possible
        filtered = recommendations[recommendations['Company Name'] == selected_company] if selected_company else recommendations

        display_cols = [
            'Company Name', 'Model Name', 'Launched Price (INR)',
            'RAM_GB', 'Storage_GB', 'Battery Capacity(mAh)',
            'Back Cam Primary (MP)', 'Front Cam Primary (MP)'
        ]

        return render_template(
            'result.html',
            recommended=filtered[display_cols].to_dict(orient='records') if not filtered.empty else None,
            fallback=recommendations[display_cols].to_dict(orient='records'),
            selected_company=selected_company
        )

    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
