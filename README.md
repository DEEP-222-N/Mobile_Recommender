# 📱 Mobile Recommendation System

**Live Demo:** [Click to try it out](https://mobile-recommender-jmwz.onrender.com/)  
**Power BI Dashboard:** [View Analysis](https://app.powerbi.com/view?r=eyJrIjoiMWRkYTA3ZWMtMTNhYy00ODM1LTk1NDYtYmQxOWE3MmRmYjhhIiwidCI6ImQxZjE0MzQ4LWYxYjUtNGEwOS1hYzk5LTdlYmYyMTNjYmM4MSIsImMiOjEwfQ%3D%3D)

---

## 📌 Overview

The **Mobile Recommendation System** is a web-based application that recommends smartphones based on user preferences like **budget**, **RAM**, **storage**, and **battery capacity**. It uses a **K-Nearest Neighbors (KNN)** algorithm for content-based filtering and is powered by a clean Flask backend and a responsive frontend built using HTML and CSS.

Additionally, the project includes a **Power BI dashboard** to explore pricing and specification trends in the mobile market using a separate analysis pipeline.

---

## 🧠 How It Works

1. User enters mobile preferences through a web form.
2. Inputs are scaled using the same transformation as the training data.
3. A KNN model compares the input to a dataset of mobile specifications.
4. Top matching phones are shown with relevant details.

---

## 🛠️ Tech Stack

### ⚙️ Backend & Model
- **Python**
- **Pandas**, **NumPy** – Data preprocessing
- **Scikit-learn** – KNN model implementation
- **Pickle** – Model and scaler serialization
- **Flask** – Web server for serving recommendations

### 🌐 Frontend
- **HTML**, **CSS** – Simple and clean responsive UI

### 📊 Data Analytics (Power BI)
- **Google Colab** (Pandas) – Data cleaning and preparation
- **Power BI**, **DAX** – Dashboard creation and analysis
- **Power Query** – Data shaping

---

## 📈 Power BI Insights

The dashboard analyzes smartphone trends across:

- 📊 **Brand-wise distribution** and market positioning  
- 💰 **Price vs. hardware** correlations (RAM, Storage, Battery, Camera)  
- 🔋 **Battery-to-price ratio** using custom DAX  
- 🌍 **International vs Domestic pricing**  
- 🏆 **Top value phones** based on custom efficiency scoring

---

## 🔑 Key Features

- ✅ User-driven input (budget, RAM, storage, battery)
- 🔍 Content-based recommendation with KNN
- 📱 Tailored phone suggestions
- 🎨 Lightweight, responsive UI
- 📊 Detailed data analysis dashboard in Power BI

---

## 🚀 Getting Started Locally

### 1. Clone the Repository

```git clone https://github.com/yourusername/mobile-recommender.git```

```cd mobile-recommender```

### 2. Install Requirements

```pip install -r requirements.txt```


### 3. Run the Flask App

```python app.py```

mobile-recommender/
├── app.py                # Flask backend
├── model.pkl             # Saved KNN model
├── scaler.pkl            # Scaler object
├── dataset.pkl           # Processed dataset
├── templates/
│   └── index.html        # Main UI page
├── static/
│   └── style.css         # Styling
├── PowerBI/
│   └── dashboard.pbix    # BI analysis (optional)
└── README.md             # Project documentation
