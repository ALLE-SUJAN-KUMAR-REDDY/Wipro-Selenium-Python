# 1. Create a DataFrame containing missing (None/NaN) values.

import pandas as pd
import numpy as np
# Create DataFrame with missing values
data = {
    "Name": ["Ram", "Sam", "John", "Priya", "Anita"],
    "Age": [25, None, 28, 22, 35],
    "Department": ["IT", "HR", "Finance", "IT", "HR"],
    "Salary": [40000, 50000, None, 38000, 60000],
    "City": ["Delhi", "Mumbai", "Chennai", "Bangalore", "Bangalore"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


# 2. Detect missing values using appropriate function.

print("\nMissing Values:")
print(df.isnull())

# 3. Replace missing values with 0.

df_filled = df.fillna(0)
print("\nAfter Replacing Missing Values with 0:")
print(df_filled)

# 4. Drop rows containing missing values.

df_dropped = df.dropna()
print("\nAfter Dropping Missing Rows:")
print(df_dropped)

# 5. Sort the DataFrame by Age in ascending order.

print("\nSorted by Age (Ascending):")
print(df.sort_values(by="Age"))

# 6. Sort the DataFrame by Salary in descending order.

print("\nSorted by Salary (Descending):")
print(df.sort_values(by="Salary", ascending=False))

# 7. Perform groupby on Department and find average Salary per department.

print("\nAverage Salary per Department:")
print(df.groupby("Department")["Salary"].mean())

# 8. Find total Salary per department using groupby.

print("\nTotal Salary per Department:")
print(df.groupby("Department")["Salary"].sum())

# 9. Filter employees where Age > 25 AND City = 'Bangalore'.

print("\nEmployees Age > 25 AND City = Bangalore:")
filtered = df[(df["Age"] > 25) & (df["City"] == "Bangalore")]
print(filtered)

# 10. Create a new column 'Tax' which is 10% of Salary using apply().

df["Tax"] = df["Salary"].apply(lambda x: x * 0.10 if pd.notnull(x) else x)
print("\nAfter Adding Tax Column (10%):")
print(df)