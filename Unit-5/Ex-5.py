# 5. Perform basic data analysis using a Pandas DataFrame.
# Basic data analysis using Pandas
import pandas as pd

data = {
    'Name': ['Rahul', 'Amit', 'Priya', 'Neha'],
    'Age': [20, 21, 22, 20],
    'Marks': [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nFirst 2 Records:")
print(df.head(2))

print("\nData Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Marks:")
print(df['Marks'].mean())

print("\nHighest Marks:")
print(df['Marks'].max())

print("\nLowest Marks:")
print(df['Marks'].min())
