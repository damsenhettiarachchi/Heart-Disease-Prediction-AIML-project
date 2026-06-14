import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("results/outputs/member4_onehot_encoded.csv")  # replace with your latest dataset file

# Columns to scale
numerical_columns = [
    'Age', 
    'Blood Pressure', 
    'Cholesterol Level', 
    'BMI', 
    'Sleep Hours', 
    'Triglyceride Level', 
    'Fasting Blood Sugar', 
    'CRP Level', 
    'Homocysteine Level'
]

scaler = StandardScaler()

# Apply scaling
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Save the final scaled dataset
df.to_csv("member5_scaled.csv", index=False)

print("Scaling completed for 9 numerical columns.")
