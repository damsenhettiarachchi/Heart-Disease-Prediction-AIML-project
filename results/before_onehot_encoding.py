import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset BEFORE one-hot encoding
df = pd.read_csv("results/outputs/member3_label_encoding.csv")   # change to your file name

# Columns for one-hot encoding
ohe_columns = ['Exercise Habits', 'Alcohol Consumption', 'Stress Level', 'Sugar Consumption']

# Plot countplots for each column
for col in ohe_columns:
    plt.figure(figsize=(6,4))
    sns.countplot(x=df[col], palette="Set2")
    plt.title(f"Distribution of {col} (Before One-Hot Encoding)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(f"before_onehot_{col.replace(' ', '_')}.png")  # save chart
    plt.show()
