# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Working with NumPy Arrays
# -----------------------------

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Create a 2D array
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print("2D Array:\n", arr2)

# Calculate mean of arr1
print("Mean of arr1:", np.mean(arr1))

# Calculate sum of arr2
print("Sum of arr2:", np.sum(arr2))

# Transpose of arr2
print("Transpose of arr2:\n", np.transpose(arr2))

# -----------------------------
# 2. Working with Pandas DataFrames
# -----------------------------

# Create a DataFrame from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 90, 95]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Add a new column 'Grade'
df['Grade'] = ['B', 'A', 'A+']
print("\nDataFrame with Grade:\n", df)

# Calculate average marks
print("\nAverage Marks:", df['Marks'].mean())

# -----------------------------
# 3. Plotting with Matplotlib
# -----------------------------

# a) Line plot: y = x^2
x = np.array([0, 1, 2, 3, 4])
y = x ** 2
plt.plot(x, y)
plt.title("Line Plot of y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

# b) Bar chart: Student Marks
plt.bar(df['Name'], df['Marks'], color='orange')
plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()
