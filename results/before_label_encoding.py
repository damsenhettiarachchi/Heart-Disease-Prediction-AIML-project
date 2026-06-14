import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset BEFORE label encoding
df = pd.read_csv("results/outputs/outliers_removed.csv")  

# Categorical columns to visualize
cat_cols = ['Gender', 'Smoking', 'Family Heart Disease', 'High Blood Pressure',
            'Low HDL Cholesterol', 'High LDL Cholesterol', 'Diabetes']

# Plot count plots for each categorical column
for col in cat_cols:
    plt.figure(figsize=(7,5)) #Creates a figure
    sns.countplot(x=col, data=df, palette="Set2")
    plt.title(f"Count of {col} (Before Label Encoding)")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()

    # Save each plot
    plt.savefig(f"{col}_before_label_encoding.png")
    plt.show()


