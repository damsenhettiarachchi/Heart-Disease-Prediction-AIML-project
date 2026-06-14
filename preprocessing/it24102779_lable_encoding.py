import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset 
df = pd.read_csv("results/output/outliers_removed.csv")

part1_columns = ['Gender', 'Smoking', 'Family Heart Disease', 'Diabetes']

# Apply Label Encoding
le = LabelEncoder()
for col in part1_columns:
    df[col] = le.fit_transform(df[col])

# Save the dataset 
df.to_csv("member2_label_encoding.csv", index=False)

print("Part 1 label encoding completed. File saved as 'member2_label_encoding.csv'.")


