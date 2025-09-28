import streamlit as st
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Algerian Forest Fire Prediction",
    page_icon="🔥",
    layout="centered"
)

# ------------------ Title & Description ------------------
st.title("🔥 Algerian Forest Fire Prediction")
st.markdown(
    """
    ### About this App  
    This web application predicts the likelihood of **forest fires in Algeria**  
    based on weather and environmental conditions using a Machine Learning model.  

    **Created by Mohammed Zaheeruddin**
    """
)

# ------------------ Load Models ------------------
linear_model = pickle.load(open('models/linear.pkl', 'rb'))
scaler_model = pickle.load(open('models/scaler.pkl', 'rb'))

# ------------------ Input Form ------------------
st.header("🌍 Enter Environmental Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    temperature = st.number_input("🌡️ Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)
    RH = st.number_input("💧 Relative Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
    Ws = st.number_input("🌬️ Wind Speed (km/h)", min_value=0.0, step=0.1)

with col2:
    Rain = st.number_input("☔ Rain (mm)", min_value=0.0, step=0.1)
    FFMC = st.number_input("🔥 FFMC Index", min_value=0.0, step=0.1)
    DMC = st.number_input("🌿 DMC Index", min_value=0.0, step=0.1)

with col3:
    ISI = st.number_input("⚡ ISI Index", min_value=0.0, step=0.1)
    claas = st.number_input("📊 Class", min_value=0.0, step=1.0)
    Region = st.number_input("🗺️ Region", min_value=0.0, step=1.0)

# ------------------ Prediction Button ------------------
if st.button("🔍 Predict Fire Risk"):
    new_data_scaled = scaler_model.transform(
        [[temperature, RH, Ws, Rain, FFMC, DMC, ISI, claas, Region]]
    )
    result = linear_model.predict(new_data_scaled)

    st.success(f"🔥 **Prediction Result:** {result[0]}")
