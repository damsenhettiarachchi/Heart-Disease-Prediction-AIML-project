import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load your preprocessed dataset (before scaling)
df = pd.read_csv("results/outputs/member4_onehot_encoded.csv")

# Select numerical columns for scaling
num_cols = ['Age', 'Blood Pressure', 'Cholesterol Level', 'BMI',
            'Sleep Hours', 'Triglyceride Level', 'CRP Level', 'Homocysteine Level']

# Copy original data for "before scaling"
before_scaling = df[num_cols].copy()

# Apply StandardScaler
scaler = StandardScaler()
after_scaling = pd.DataFrame(scaler.fit_transform(before_scaling), columns=num_cols)

# Plot boxplots side-by-side (before vs after)
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Before scaling
before_scaling.boxplot(ax=axes[0])
axes[0].set_title("Before Scaling")
axes[0].tick_params(axis='x', rotation=45)

# After scaling
after_scaling.boxplot(ax=axes[1])
axes[1].set_title("After Scaling")
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig("scaling_comparison.png")
plt.show()
