# 6. Create a DataFrame from CSV or Excel files.
# Create DataFrame from CSV and Excel files
import pandas as pd

# Reading CSV file
df_csv = pd.read_csv("students.csv")
print("DataFrame from CSV:")
print(df_csv)

# Reading Excel file
df_excel = pd.read_excel("students.xlsx")
print("\nDataFrame from Excel:")
print(df_excel)
