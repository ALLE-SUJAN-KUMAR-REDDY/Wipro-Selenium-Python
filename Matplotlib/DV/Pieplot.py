# Pie Chart using Matplotlib

import matplotlib.pyplot as plt

# data
labels = ["Maths", "Science", "English", "History"]
marks = [85, 75, 90, 60]

plt.pie(marks, labels=labels)

plt.title("Subject Marks Distribution")

plt.show()

# Pie Chart with Percentage

import matplotlib.pyplot as plt

labels = ["Maths", "Science", "English", "History"]
marks = [85, 75, 90, 60]

plt.pie(marks, labels=labels, autopct="%1.1f%%")

plt.title("Subject Marks Percentage")

plt.show()

# Better Styled Pie Chart

import matplotlib.pyplot as plt

labels = ["Maths", "Science", "English", "History"]
marks = [85, 75, 90, 60]
explode = (0, 0.1, 0, 0)   # explode 2nd slice

plt.pie(marks, labels=labels, autopct="%1.1f%%", explode=explode, shadow=True)

plt.title("Styled Pie Chart")

plt.show()