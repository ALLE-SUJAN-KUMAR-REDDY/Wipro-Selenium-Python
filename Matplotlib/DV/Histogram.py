# Histogram using Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# generate random data
data = np.array([10, 20, 20, 30, 30, 30, 40, 40, 50, 60])

plt.hist(data)

plt.title("Simple Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

# Histogram with Bins
# bins controls how many groups (intervals) are created.

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(10, 100, 50)

plt.hist(data, bins=5)

plt.title("Histogram with 5 Bins")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

# Histogram using Pandas

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Marks": [40, 50, 60, 70, 80, 90, 50, 60, 70, 85]
}

df = pd.DataFrame(data)

df["Marks"].plot(kind="hist", bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()