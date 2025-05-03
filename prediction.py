import pandas as pd
import numpy as np
import joblib

# Load model
loaded_model = joblib.load('model.pkl')
loaded_scaler = joblib.load('scaler.pkl')

df_dummy = pd.DataFrame({
    "MonthlyIncome": [13500],
    "StockOptionLevel": [1],
    "JobLevel": [4],
    "Age": [42],
    "TotalWorkingYears": [23],
    "OverTime_No": [1], # OverTime: No
    "OverTime_Yes": [0],
    "MaritalStatus_Divorced": [0],
    "MaritalStatus_Married": [1],
    "MaritalStatus_Single": [0],
    "JobRole_Healthcare Representative": [0],
    "JobRole_Human Resources": [0],
    "JobRole_Laboratory Technician": [0],
    "JobRole_Manager": [0],
    "JobRole_Manufacturing Director": [0],
    "JobRole_Research Director": [0],
    "JobRole_Research Scientist": [0],
    "JobRole_Sales Executive": [0],
    "JobRole_Sales Representative": [1], # JobRole sebagai Sales Representative
    "Department_Human Resources": [0],
    "Department_Research & Development": [0],
    "Department_Sales":[1], # Department Sales
})

# Scaling dummy input
df_dummy_scaled = loaded_scaler.transform(df_dummy)

# Mapping hasil prediksi
mapping = {0: "Karyawan kemungkinan akan Stay", 1: "Karyawan kemungkinan akan Leave"}

# Prediksi menggunakan model
prediction = loaded_model.predict(df_dummy_scaled)
probabilities = loaded_model.predict_proba(df_dummy_scaled)

# Probabilitas untuk Stay (Attrition: 0) dan Leave (Attrition: 1)
proba_stay = probabilities[:, 0] * 100 # Probabilitas untuk Stay
proba_leave = probabilities[:, 1] * 100 # Probabilitas untuk Leave

# Tampilkan hasil
print(f"Prediksi Attrition: {mapping[prediction[0]]}")
print(f"Probabilitas Stay: {proba_stay[0]:.2f}%")
print(f"Probabilitas Leave: {proba_leave[0]:.2f}%")