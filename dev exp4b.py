import pandas as pd

# Sample dataset (you can load from CSV using pd.read_csv("yourfile.csv"))
data = {
    'EmployeeID': ['E001', 'E002', 'E003', 'E004', 'E005', 'E006'],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'HoursWorked': [40, 45, 38, 50, 42, 55]
}

df = pd.DataFrame(data)

# Grouping by Department and calculating total and average
grouped = df.groupby('Department').agg(
    Total_Hours=('HoursWorked', 'sum'),
    Average_Hours=('HoursWorked', 'mean')
).reset_index()

# Creating a pivot table (not necessary in this case, but shown for format)
pivot_table = pd.pivot_table(df, index='Department', values='HoursWorked', 
                              aggfunc=['sum', 'mean'])

# Highlight the department with highest average hours
max_avg_dept = grouped.loc[grouped['Average_Hours'].idxmax()]

# Display results
print("Summary Report:\n")
print(grouped)
print("\nDepartment with Highest Average Hours:")
print(f"{max_avg_dept['Department']} with {max_avg_dept['Average_Hours']} hours (avg)")
