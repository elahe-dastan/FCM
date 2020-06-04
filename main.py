import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# First of all I have to read the data
header = pd.read_csv('test.csv', nrows=0).columns.tolist()
data = pd.read_csv("sample1.csv")

# Plot the data
fig = plt.figure()
f = fig.add_subplot()
for h in header:
    f.scatter(data[h], c='b')

x = data.values
num_data = len(x)
max_num_clusters = 11
steps = 50

# Defining answer
for c in range(max_num_clusters):
    # Initialize U matrix
    U = np.random.rand(num_data, c)
    C = np.empty((c, len(header)))

    m = 2

    # number of steps
    for k in range(steps):
        previous_U = np.copy(U)
        # the center of each cluster
        for j in range(c):
            numerator = 0
            denominator = 0
            # number of data
            for i in range(num_data):
                numerator += np.power(U[i, j], m) * x[i]
                denominator += np.power(U[i, j], m)

            C[j] = numerator / denominator

        for jj in range(c):
            for ii in range(num_data):
                numerator = x[ii] - C[jj]
                numerator_norm = np.linalg.norm(numerator)
                numerator_norm = np.power(numerator_norm, 2 / (m - 1))
                numerator_norm = 1 / numerator_norm
                denominator = 0
                for center in range(4):
                    d = x[ii] - C[center]
                    d_norm = np.linalg.norm(d)
                    d_norm = np.power(d_norm, 2 / (m - 1))
                    denominator += 1 / d_norm

                U[ii, jj] = numerator_norm / denominator

        if np.linalg.norm(U - previous_U) < 0.3:
            break

    f.scatter(C[:, 0], C[:, 1], c='red')
    plt.show()
