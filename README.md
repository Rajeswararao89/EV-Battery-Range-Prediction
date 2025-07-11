# 🔋 EV Battery Health & Range Prediction

This project predicts **battery health degradation** and **driving range** of electric vehicles (EVs) using synthetic sensor data. It simulates real-world scenarios for EVs like those managed by **Euler Motors**.

---

## 🚗 Project Highlights

- Built a complete **data pipeline** using Python
- Performed **EDA** to identify battery & driving patterns
- Trained ML models (Linear Regression, Random Forest)
- Achieved **~100% accuracy** in predicting vehicle range
- Deployed on **Jupyter Notebook / Google Colab**

---

## 📊 Features Used

- Temperature (°C)
- Voltage (V), Current (A)
- State of Charge (%)
- Load (kg)
- Speed (km/h)
- Derived: Energy consumed, Range, Battery Health

---

## 🤖 ML Models & Evaluation

| Task               | Model             | RMSE  | R² Score |
|--------------------|------------------|--------|----------|
| Battery Health     | Linear Regression | 12.96 | -0.01 |
| Battery Health     | Random Forest     | 13.73 | -0.14 |
| Range Prediction   | Linear Regression | 0.00  | 1.00 ✅ |
| Range Prediction   | Random Forest     | 0.58  | 1.00 ✅ |

---

## 📁 Folder Structure

Battery-Prediction-Project/
├── data/
│ └── ev_sensor_data.csv
├── notebook/
│ └── EV_Battery_Prediction.ipynb
├── outputs/
│ └── charts, models
└── README.md



---

## 🧠 Skills Demonstrated

- Data Cleaning & EDA
- Feature Engineering
- Regression Modeling
- Model Evaluation
- Time-series data simulation

---

## 💼 Ideal For

Showcasing in your **Data Science Internship CV** — particularly for **mobility, EV, or IoT** roles.

---

