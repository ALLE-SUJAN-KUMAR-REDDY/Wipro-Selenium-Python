import  matplotlib.pyplot as plt
import pandas as pd
import  numpy as np
# X axis data

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [4000, 5500, 7000, 6500, 8000]
}

df = pd.DataFrame(data)

# Correct plotting
df.plot(x="Day", y="Steps", kind="line")

plt.title("Daily Steps Count")
plt.xlabel("Day")
plt.ylabel("Steps")
# plt.show()

# save as image - jpg
plt.savefig("BarChart.jpg")

# save as pdf
plt.savefig("bar.pdf", format="pdf")
