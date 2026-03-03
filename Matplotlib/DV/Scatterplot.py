#Scatter Plot using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 25, 30, 40])

plt.scatter(x, y)

plt.title("Simple Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()

# Scatter Plot using Pandas

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Hours_Studied": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 85]
}

df = pd.DataFrame(data)

df.plot(x="Hours_Studied", y="Marks", kind="scatter")

plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.show()