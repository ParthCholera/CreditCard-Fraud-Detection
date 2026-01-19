import streamlit as st
import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction features:")

features = []
for i in range(30):
    val = st.number_input(f"Feature V{i+1}", value=0.0)
    features.append(val)

if st.button("Predict"):
    data = np.array(features).reshape(1, -1)
    pred = model.predict(data)[0]
    if pred == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legit Transaction")
