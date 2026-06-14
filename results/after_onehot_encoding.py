import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset AFTER one-hot encoding
df = pd.read_csv("results/outputs/member4_onehot_encoded.csv")  # change to your file name

# Get the one-hot encoded columns (you can filter by keywords if needed)
ohe_columns = [col for col in df.columns if 
               'Exercise Habits' in col or 
               'Alcohol Consumption' in col or 
               'Stress Level' in col or 
               'Sugar Consumption' in col]

# Plot bar charts for each one-hot encoded column
for col in ohe_columns:
    plt.figure(figsize=(5,3))
    sns.countplot(x=df[col], palette="pastel")
    plt.title(f"Distribution of {col} (After One-Hot Encoding)")
    plt.xticks([0,1], ['Not Present (0)', 'Present (1)'])
    plt.tight_layout()
    plt.savefig(f"after_onehot_{col.replace(' ', '_')}.png")  # save chart
    plt.show()
