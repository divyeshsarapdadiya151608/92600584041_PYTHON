# 7. Handle missing data using the dropna and fillna methods.
# Handling missing data using Pandas
import pandas as pd

data = {
    'Name': ['Rahul', 'Amit', 'Priya', 'Neha'],
    'Age': [20, None, 22, 21],
    'Marks': [85, 90, None, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove rows containing missing values
print("\nAfter dropna():")
print(df.dropna())

# Fill missing values
print("\nAfter fillna():")
print(df.fillna({
    'Age': df['Age'].mean(),
    'Marks': df['Marks'].mean()
}))
