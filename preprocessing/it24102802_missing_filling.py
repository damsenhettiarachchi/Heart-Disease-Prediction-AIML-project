import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/heart_disease.csv")  

# Separate numerical and categorical columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = df.select_dtypes(include=['object']).columns.tolist()

# Fill missing values
# Numerical columns: median
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Categorical columns: mode
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Save the new dataset
df.to_csv("missing_filled.csv", index=False)

print("Missing values filled and file saved as 'dataset_filled.csv'")
