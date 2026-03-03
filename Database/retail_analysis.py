# ============================================
# RETAIL DATA ANALYSIS PROJECT
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# STEP 1: DATA CLEANING
# ============================================

# Load CSV file
df = pd.read_csv("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Database//retail_data.csv")

print("First 5 Rows:")
print(df.head())

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Check null values
print("\nNull Values:")
print(df.isnull().sum())

# Handle null values (fill with 0)
df.fillna(0, inplace=True)

# ============================================
# STEP 2: ANALYSIS
# ============================================

# Region generating highest revenue
region_revenue = df.groupby("Region")["Revenue"].sum()
highest_region = region_revenue.idxmax()

print("\nRevenue by Region:")
print(region_revenue)
print("\nHighest Revenue Region:", highest_region)

# Monthly Sales Trend
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

#  Best Performing Category
category_revenue = df.groupby("Category")["Revenue"].sum()
best_category = category_revenue.idxmax()

print("\nCategory Revenue:")
print(category_revenue)
print("\nBest Performing Category:", best_category)

#  Top 5 Products by Revenue
top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Products by Revenue:")
print(top_products)

# ============================================
# STEP 3: VISUALIZATIONS (Matplotlib Only)
# ============================================

#  Bar Chart → Revenue by Region
plt.figure()
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

# Line Plot → Monthly Revenue Trend
plt.figure()
monthly_sales.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

#  Pie Chart → Category Contribution
plt.figure()
category_revenue.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Contribution")
plt.ylabel("")
plt.show()

#  Horizontal Bar Chart → Top 5 Products
plt.figure()
top_products.plot(kind="barh")
plt.title("Top 5 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()

print("\nProject Completed Successfully!")