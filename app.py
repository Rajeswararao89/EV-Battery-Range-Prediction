# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

st.set_page_config(page_title="EV Battery & Range Predictor", layout="wide")

st.title("🔋 EV Battery Health & Range Prediction Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload EV Sensor Data (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔎 Uploaded Data")
    st.dataframe(df.head())

    # Load Models
    battery_model = joblib.load("battery_model.pkl")
    range_model = joblib.load("range_model.pkl")

    # Make predictions
    features = ['temperature', 'voltage', 'current', 'state_of_charge', 'load', 'speed', 'energy_consumed_kWh']
    df['Predicted Battery Health'] = battery_model.predict(df[features])
    df['Predicted Range'] = range_model.predict(df[features])

    st.subheader("📈 Predictions")
    st.write(df[['Predicted Battery Health', 'Predicted Range']].head())

    # Charts
    st.subheader("📊 Charts")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔋 State of Charge Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df['state_of_charge'], bins=30, kde=True, ax=ax, color="green")
        st.pyplot(fig)

    with col2:
        st.markdown("### 🧪 Feature Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df[features + ['Predicted Battery Health', 'Predicted Range']].corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        st.pyplot(fig)

else:
    st.warning("Please upload a valid EV sensor dataset to begin.")
