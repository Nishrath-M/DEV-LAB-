import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load built-in Seaborn dataset
df = sns.load_dataset("tips")

# Set Seaborn style
sns.set(style="whitegrid")

# Create subplots for multiple visualizations
plt.figure(figsize=(18, 12))

# 1. Bar Plot
plt.subplot(2, 3, 1)
sns.barplot(x="day", y="total_bill", data=df)
plt.title("Average Total Bill per Day")

# 2. Line Plot
plt.subplot(2, 3, 2)
sns.lineplot(x="size", y="tip", data=df)
plt.title("Tip vs Party Size")

# 3. Box Plot
plt.subplot(2, 3, 3)
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Box Plot of Total Bill per Day")

# 4. Heatmap of Correlation
plt.subplot(2, 3, 4)
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

# 5. Count Plot (Categorical Bar Chart)
plt.subplot(2, 3, 5)
sns.countplot(x="smoker", hue="sex", data=df)
plt.title("Count of Smokers by Gender")

# 6. Pair Plot in a New Window
plt.tight_layout()
plt.show()

# Pair Plot (opens separately due to size)
sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle("Pair Plot of Numerical Features", y=1.02)
plt.show()
