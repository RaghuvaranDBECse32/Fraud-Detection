import pandas as pd

def detect_fraud(data):
    # Example Fraud Detection Logic

    # Flag policies where Sum Assured is disproportionately high compared to income
    data['Fraud_Risk'] = (data['POLICY_SUMASSURED'] / data['Annual Income']) > 10

    # Flag policies with unusually high premiums
    data['High_Premium'] = data['Premium'] > data['Annual Income'] * 0.2

    # Combine flags to detect fraud
    data['Potential_Fraud'] = data['Fraud_Risk'] | data['High_Premium']

    return data[['Dummy Policy No', 'Fraud_Risk', 'High_Premium', 'Potential_Fraud']]
