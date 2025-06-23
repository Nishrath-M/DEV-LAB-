import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV file (no need for full path since it's in the same folder)
import pandas as pd

df = pd.read_csv(r"C:\Users\Nishrath\Downloads\sample_emails.csv")  # Use your path
print(df.head())
import matplotlib.pyplot as plt
import seaborn as sns

# Check dataset shape and info
print("Shape of dataset:", df.shape)
print(df.info())
print(df.isnull().sum())

# Parse date column
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.month
df['Hour'] = df['Date'].dt.hour
df['Day'] = df['Date'].dt.day_name()

# Top 5 senders
df['From'].value_counts().head(5).plot(kind='barh', title="Top 5 Senders")
plt.xlabel("Number of Emails")
plt.show()

# Spam vs Non-Spam
sns.countplot(data=df, x='Spam')
plt.title("Spam vs Non-Spam Emails")
plt.show()

# Body length analysis
df['BodyLength'] = df['Body'].astype(str).apply(len)
sns.histplot(df['BodyLength'], bins=20)
plt.title("Distribution of Email Body Length")
plt.show()
