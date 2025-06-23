import pandas as pd

# ✅ Step 1: Load the CSV using your provided path
df = pd.read_csv(r"C:\Users\Nishrath\Desktop\DEV\weekly_temperature_data.csv")

# ✅ Step 2: Convert 'Date' column to datetime and extract 'Month'
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%B')  # Get full month name

# ✅ Step 3: Group by City and Month and calculate sum of temperature
grouped = df.groupby(['City', 'Month'])['Temperature'].sum().reset_index()

# ✅ Step 4: Pivot table: Cities as rows, Months as columns
pivot_table = grouped.pivot(index='City', columns='Month', values='Temperature').fillna(0)

# ✅ Step 5: Calculate total summer temperature (June, July, August)
summer_months = ['June', 'July', 'August']
pivot_table['Summer_Total'] = pivot_table[summer_months].sum(axis=1)

# ✅ Step 6: Find the city with the highest total summer temperature
hottest_city = pivot_table['Summer_Total'].idxmax()
highest_temp = pivot_table['Summer_Total'].max()

# ✅ Step 7: Print results
print("Grouped Data:\n", grouped)
print("\nPivot Table (Month-wise Summary):\n", pivot_table)
print(f"\n🔥 Hottest city in summer: {hottest_city} with total {highest_temp}°C")
