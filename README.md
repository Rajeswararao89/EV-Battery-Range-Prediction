# 🔋 EV Battery Health & Range Prediction Dashboard

A machine learning-powered web application that predicts **battery health** and **EV range** from vehicle sensor data using real-time analytics and visualizations. Built with Python, Streamlit, and Scikit-learn — inspired by real-world use cases like battery optimization in electric fleets.

🌐 **Live Demo**: [Click to Launch App]((https://ev-battery-range-prediction-project-aatrazjoaco6ukkratkigl.streamlit.app/))
📊 **Try it now**: Upload `ev_sensor_data.csv` to get instant predictions.

---

## 🚗 Project Overview

At scale, electric vehicles (EVs) generate **millions of sensor data points**. This project simulates such telemetry, applies machine learning models, and visualizes:

- ✅ Predicted **Battery Health** (based on voltage, current, temperature, etc.)
- ✅ Predicted **Driving Range**
- 📈 Feature correlation heatmaps
- 📊 Interactive charts (State of Charge, etc.)

---

## 🧠 Tech Stack

| Component        | Tool / Library           |
|------------------|--------------------------|
| Data Processing  | `pandas`, `numpy`        |
| Visualization    | `matplotlib`, `seaborn`  |
| ML Models        | `scikit-learn`           |
| UI & Deployment  | `streamlit`              |
| Model Serving    | `joblib`                 |

---

## 🧪 Features

- 📂 Upload your EV telemetry CSV
- 🤖 Predict battery health & EV range using trained ML models
- 🔍 Explore state of charge, load, speed, etc. with histograms
- 📊 View feature correlations in real-time
- 🖼️ Embedded image plots from previous model results

---

## 📁 Folder Structure

EV-Battery-Range-Prediction/
├── app.py # Streamlit frontend
├── battery_model.pkl # Trained model for battery health
├── range_model.pkl # Trained model for range
├── ev_sensor_data.csv # Sample EV sensor data
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── *.png # Saved visualizations


---

## 🧠 Machine Learning

Two regression models were trained:
- 🔋 `battery_model.pkl`: Predicts battery health
- 🛣️ `range_model.pkl`: Predicts range in kilometers

Models used:
- Linear Regression
- Random Forest Regressor

---

## 📦 Installation & Usage (Local)

```bash
# 1. Clone the repo
git clone https://github.com/Rajeswararao89/EV-Battery-Range-Prediction.git
cd EV-Battery-Range-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py

📸 Sample Visuals
