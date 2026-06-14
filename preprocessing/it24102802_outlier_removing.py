import pandas as pd

# Load the dataset
df = pd.read_csv("results/outputs/missing_filled.csv")  

# List numerical columns to check for outliers
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Function to remove outliers using IQR
def remove_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    return df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]


for col in num_cols:
    df = remove_outliers(df, col)

# Save the new dataset
df.to_csv("outliers_removed.csv", index=False)
print("Outliers removed and dataset saved successfully!")
