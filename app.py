import streamlit as st
import joblib
import pandas as pd
import os

st.title("Customer Churn Prediction App")

# Load model safely
model_path = os.path.join(os.path.dirname(__file__), "churn_model.pkl")
model = joblib.load(model_path)

# Inputs
age = st.slider("Age", 18, 70)
income = st.number_input("Income")
orders = st.number_input("Total Orders")
spent = st.number_input("Total Spent")
avg = st.number_input("Avg Order Value")

if st.button("Predict"):

    data = pd.DataFrame([{
        "age": age,
        "income": income,
        "total_orders": orders,
        "total_spent": spent,
        "avg_order_value": avg
    }])

    result = model.predict(data)[0]

    if result == 1:
        st.error("Customer likely to CHURN")
    else:
        st.success("Customer will STAY")