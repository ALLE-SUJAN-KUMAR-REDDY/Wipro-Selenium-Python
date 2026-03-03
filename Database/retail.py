import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: LOAD CSV DATA
# ==========================================

df = pd.read_csv("retail_data.csv")

print("CSV Loaded Successfully")
print(df.head())

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Check null values
print("\nNull Values:")
print(df.isnull().sum())

# Fill null values if any
df.fillna(0, inplace=True)

# ==========================================
# STEP 2: CONNECT TO MYSQL
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Skr@199394"
)

cursor = connection.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS retail_db")
cursor.execute("USE retail_db")

# Drop table if exists (clean run)
cursor.execute("DROP TABLE IF EXISTS sales")

# Create Table dynamically
cursor.execute("""
CREATE TABLE sales (
    OrderID INT,
    Date DATE,
    Region VARCHAR(50),
    Product VARCHAR(50),
    Category VARCHAR(50),
    Quantity INT,
    Price FLOAT
)
""")

print("Table Created Successfully")

# ==========================================
# STEP 3: INSERT CSV DATA INTO MYSQL
# ==========================================

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales (OrderID, Date, Region, Product, Category, Quantity, Price)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row["OrderID"]),
        row["Date"].date(),
        row["Region"],
        row["Product"],
        row["Category"],
        int(row["Quantity"]),
        float(row["Price"])
    ))

connection.commit()
print("CSV Data Inserted into MySQL")

# ==========================================
# STEP 4: READ FROM MYSQL FOR ANALYSIS
# ==========================================

engine = create_engine("mysql+mysqlconnector://root:Skr%40199394@localhost/retail_db")

df = pd.read_sql("SELECT * FROM sales", engine)

df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]

# ==========================================
# STEP 5: ANALYSIS
# ==========================================

region_revenue = df.groupby("Region")["Revenue"].sum()
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()
category_sales = df.groupby("Category")["Revenue"].sum()
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)

print("\nRevenue by Region:\n", region_revenue)
print("\nMonthly Sales:\n", monthly_sales)
print("\nCategory Revenue:\n", category_sales)
print("\nTop 5 Products:\n", top_products)

# ==========================================
# STEP 6: VISUALIZATION
# ==========================================

plt.figure()
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.show()

plt.figure()
monthly_sales.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.show()

plt.figure()
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Contribution")
plt.ylabel("")
plt.show()

plt.figure()
top_products.plot(kind="barh")
plt.title("Top 5 Products")
plt.show()

print("\nProject Completed Successfully")