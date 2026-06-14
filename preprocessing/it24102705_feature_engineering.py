import pandas as pd

df = pd.read_csv('results/output/member5_scaled.csv')  

# Feature Engineering: Dropping unnecessary columns
df = df.drop(['Fasting Blood Sugar'], axis=1)

print("Columns after feature engineering:")
print(df.columns)

df.to_csv('member6_feature_engineered.csv', index=False)  
print("Cleaned dataset saved as 'cleaned_dataset.csv'")

