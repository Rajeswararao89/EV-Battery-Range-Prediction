import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load models
battery_model = joblib.load("battery_model.pkl")
range_model = joblib.load("range_model.pkl")

# Custom Page Config
st.set_page_config(
    page_title="EV Battery & Range Predictor",
    page_icon="🔋",
    layout="centered"
)

# Title & Branding
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔋 EV Battery Health & Range Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Predict battery health and remaining range using real-time EV sensor data</h4>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.title("🔧 Input Settings")
st.sidebar.markdown("Adjust the EV sensor data to get predictions:")

# Input Fields with Columns
col1, col2 = st.columns(2)

with col1:
    temperature = st.sidebar.slider("Temperature (°C)", 0.0, 60.0, 30.0)
    voltage = st.sidebar.slider("Voltage (V)", 350.0, 450.0, 400.0)
    current = st.sidebar.slider("Current (A)", 0.0, 200.0, 100.0)

with col2:
    load = st.sidebar.slider("Load (kg)", 100.0, 500.0, 200.0)
    speed = st.sidebar.slider("Speed (km/h)", 0.0, 120.0, 40.0)
    soc = st.sidebar.slider("State of Charge (%)", 0.0, 100.0, 80.0)

# Derived Feature
energy_consumed = (voltage * current) / 1000 * (speed / 60)

# Create input array
input_features = np.array([[temperature, voltage, current, soc, load, speed, energy_consumed]])

# Predict
battery_health = battery_model.predict(input_features)[0]
range_km = range_model.predict(input_features)[0]

# Show Input Summary
st.subheader("📊 Input Sensor Data Summary")
sensor_data = pd.DataFrame({
    'Sensor': ['Temperature (°C)', 'Voltage (V)', 'Current (A)', 'Load (kg)', 'Speed (km/h)', 'State of Charge (%)'],
    'Value': [temperature, voltage, current, load, speed, soc]
})

st.dataframe(sensor_data, use_container_width=True)

# Show as Bar Chart
st.bar_chart(sensor_data.set_index('Sensor'))

st.markdown("---")
with st.spinner('🔄 Running model predictions...'):
    battery_health = battery_model.predict(input_features)[0]
    range_km = range_model.predict(input_features)[0]

# Display Predictions with Metrics
col3, col4 = st.columns(2)

with col3:
    st.metric("🔋 Battery Health (%)", f"{battery_health:.2f}")

with col4:
    st.metric("🛣️ Predicted Range (km)", f"{range_km:.2f}")

st.markdown("---")

# Footer
st.markdown("<p style='text-align:center; color:gray;'>Built with ❤️ using Streamlit | <a href='https://github.com/Rajeswararao89/EV-Battery-Range-Prediction-project' target='_blank'>GitHub Repo</a></p>", unsafe_allow_html=True)
