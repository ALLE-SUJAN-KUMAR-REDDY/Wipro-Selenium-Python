import matplotlib.pyplot as plt

# usage
def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])   # placing text slightly above the bar


# Data for the bar chart
x = ["Engineering", "BSc", "MBA", "BCom", "BBA", "MSc"]
y = [9330, 4050, 3030, 5500, 8040, 4560]

# creating bar chart
plt.bar(x, y)

# Adding value labels
add_labels(x, y)

# Adding title and labels
plt.title("College Admission")
plt.xlabel("Courses")
plt.ylabel("Number of Admissions")

# Display the chart
plt.show()