import joblib
import pandas as pd

# Load model
model = joblib.load("churn_model.pkl")

# Example new customer data (same format as training)
sample = pd.DataFrame([{
    "age": 30,
    "income": 50000,
    "total_orders": 5,
    "total_spent": 2000,
    "avg_order_value": 400
}])

prediction = model.predict(sample)

print("Prediction (0=No Churn, 1=Churn):", prediction[0])