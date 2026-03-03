import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: LOAD CSV DATA
# ==========================================

df = pd.read_csv("student_data.csv")

print("CSV Loaded Successfully!")
print(df.head())

# ==========================================
# STEP 2: CONNECT TO MONGODB
# ==========================================

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
collection = db["students"]

# Clear old data (important)
collection.delete_many({})

# ==========================================
# STEP 3: INSERT CSV DATA INTO MONGODB
# ==========================================

data_dict = df.to_dict("records")
collection.insert_many(data_dict)

print("CSV Data Inserted into MongoDB!")

# ==========================================
# STEP 4: READ DATA FROM MONGODB
# ==========================================

data = list(collection.find({}, {"_id": 0}))  # remove MongoDB _id
df = pd.DataFrame(data)

# ==========================================
# FEATURE ENGINEERING
# ==========================================

# Create Average Marks
df["Average_Marks"] = df[["Math", "Science", "English"]].mean(axis=1)

# Create Result Column
df["Result"] = df["Average_Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("\nUpdated Data:")
print(df)

# ==========================================
# ANALYSIS
# ==========================================

# Average score per subject
subject_avg = df[["Math", "Science", "English"]].mean()
print("\nAverage Score per Subject:")
print(subject_avg)

# Correlation between Attendance & Performance
correlation = df["Attendance"].corr(df["Average_Marks"])
print("\nCorrelation (Attendance vs Performance):", correlation)

# Performance by Gender
gender_performance = df.groupby("Gender")["Average_Marks"].mean()
print("\nPerformance by Gender:")
print(gender_performance)

# Pass vs Fail Count
result_count = df["Result"].value_counts()
print("\nPass vs Fail:")
print(result_count)

# ==========================================
# VISUALIZATION
# ==========================================

# Bar Chart → Average Subject Scores
plt.figure()
subject_avg.plot(kind="bar")
plt.title("Average Subject Scores")
plt.ylabel("Marks")
plt.show()

# Scatter Plot → Attendance vs Average Marks
plt.figure()
plt.scatter(df["Attendance"], df["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()

# Boxplot → Marks Distribution by Gender
plt.figure()
df.boxplot(column="Average_Marks", by="Gender")
plt.title("Marks Distribution by Gender")
plt.suptitle("")
plt.show()

# Pie Chart → Pass vs Fail
plt.figure()
result_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.ylabel("")
plt.show()

print("\nStudent MongoDB Project Completed Successfully!")