import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset AFTER label encoding
df = pd.read_csv("results/outputs/member3_label_encoding.csv")  # change this to your actual encoded file name

# List of label encoded columns (update if needed)
label_encoded_cols = ['Gender', 'Smoking', 'Family Heart Disease', 'High Blood Pressure',
                      'Low HDL Cholesterol', 'High LDL Cholesterol', 'Diabetes']

# Create countplots for each encoded column
for col in label_encoded_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(x=col, data=df, palette="Set2")
    plt.title(f"Distribution of {col} (After Label Encoding)")
    plt.savefig(f"{col}_after_encoding.png")  # save chart for each column
    plt.show()
