import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# first of all I have to read the data
data = pd.read_csv("sample1.csv")

# plot the data
plt.scatter(data["X1"], data["X2"])
plt.show()
