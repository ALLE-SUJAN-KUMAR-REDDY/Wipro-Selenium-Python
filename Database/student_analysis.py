# ============================================
# STUDENT PERFORMANCE ANALYSIS
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# STEP 1: LOAD DATA
# ============================================

df = pd.read_csv("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Database//student_data.csv")

print("First 5 Rows:")
print(df.head())

# ============================================
# FEATURE ENGINEERING
# ============================================

# Create Average_Marks
df["Average_Marks"] = df[["Math", "Science", "English"]].mean(axis=1)

# Create Result Column
df["Result"] = df["Average_Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("\nUpdated Data:")
print(df)

# ============================================
# ANALYSIS
# ============================================

#  Average score per subject
subject_avg = df[["Math", "Science", "English"]].mean()
print("\nAverage Score Per Subject:")
print(subject_avg)

#  Correlation between Attendance and Performance
correlation = df["Attendance"].corr(df["Average_Marks"])
print("\nCorrelation (Attendance vs Average Marks):", correlation)

#  Performance by Gender
gender_performance = df.groupby("Gender")["Average_Marks"].mean()
print("\nPerformance by Gender:")
print(gender_performance)

#  Pass vs Fail Count
result_count = df["Result"].value_counts()
print("\nPass vs Fail Count:")
print(result_count)

# ============================================
# VISUALIZATIONS (Matplotlib Only)
# ============================================

#  Bar Chart → Average Subject Scores
plt.figure()
subject_avg.plot(kind="bar")
plt.title("Average Subject Scores")
plt.ylabel("Marks")
plt.show()

#  Scatter Plot → Attendance vs Average Marks
plt.figure()
plt.scatter(df["Attendance"], df["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()

#  Boxplot → Marks Distribution by Gender
plt.figure()
df.boxplot(column="Average_Marks", by="Gender")
plt.title("Marks Distribution by Gender")
plt.suptitle("")
plt.show()

#  Pie Chart → Pass vs Fail
plt.figure()
result_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.ylabel("")
plt.show()

print("\nProject Completed Successfully!")