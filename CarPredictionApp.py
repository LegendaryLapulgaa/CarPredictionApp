import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the model
model = joblib.load(open('car_prediction_data.pkl', 'rb'))

# Streamlit app
st.title("🚗 Car Price Prediction App")
st.markdown("This app predicts the **resale price** of a car based on various features.")

# Input fields
year = st.number_input('Year of Purchase', min_value=1990, max_value=2025, step=1)
present_price = st.number_input('Present Price (in lakhs)', min_value=0.0, format="%.2f")
kms_driven = st.number_input('Kilometers Driven', min_value=0)
owner = st.selectbox('Number of Previous Owners', [0, 1, 2, 3])
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
selling_type = st.selectbox('Selling Type', ['Dealer', 'Individual'])
transmission = st.selectbox('Transmission Type', ['Manual', 'Automatic'])

# Process input
fuel_type_petrol = 1 if fuel_type == 'Petrol' else 0
fuel_type_diesel = 1 if fuel_type == 'Diesel' else 0
transmission_manual = 1 if transmission == 'Manual' else 0
selling_type_individual = 1 if selling_type == 'Individual' else 0
car_age = 2025 - year

# Model input order must match training
features = [[
    present_price, kms_driven, owner, car_age,
    fuel_type_diesel, fuel_type_petrol,
    selling_type_individual, transmission_manual
]]

# Predict
if st.button("Predict Price"):
    prediction = model.predict(features)
    st.success(f"Estimated Selling Price: ₹ {prediction[0]:,.2f} Lakhs")
