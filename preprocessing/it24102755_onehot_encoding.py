import pandas as pd

# Load the dataset
df = pd.read_csv("results/output/member3_label_encoding.csv")  # change filename if needed

onehot_columns = ['Exercise Habits', 'Alcohol Consumption', 'Stress Level', 'Sugar Consumption']

# Apply One-Hot Encoding
df_onehot = pd.get_dummies(df[onehot_columns], prefix=onehot_columns)

df.drop(columns=onehot_columns, inplace=True)

df = pd.concat([df, df_onehot], axis=1)

df.to_csv("member4_onehot_encoded.csv", index=False)

print("One-Hot Encoding for all 4 columns completed. Original columns replaced with new one-hot columns.")



