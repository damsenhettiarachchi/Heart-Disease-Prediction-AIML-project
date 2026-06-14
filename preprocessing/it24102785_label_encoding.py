import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset 
df = pd.read_csv("results/output/member2_label_encoding.csv")

part2_columns = ['High Blood Pressure', 'Low HDL Cholesterol', 'High LDL Cholesterol']

# Apply Label Encoding
le = LabelEncoder()
for col in part2_columns:
    df[col] = le.fit_transform(df[col])

# Save the dataset
df.to_csv("member3_label_encoding.csv", index=False)

print("Part 2 label encoding completed. File saved as 'member3_label_encoding.csv'.")
