import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x, y)

# X axis label
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("simple plot")
# show method will display the data
plt.show()


# simple data
subjects = ["Maths", "Science", "English", "History", "Computer"]
marks = [85, 78, 92, 74, 88]

# creates the line graph
plt.plot(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

# matplotlib with pandas integration
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 130, 170, 160]
}

df = pd.DataFrame(data)

plt.plot(df['Month'], df['Sales'])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()