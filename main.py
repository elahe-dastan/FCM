import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# first of all I have to read the data
data = pd.read_csv("test.csv")

fig = plt.figure()
f = fig.add_subplot()
# plot the data
f.scatter(data["X1"], data["X2"], c='b')

x = data.values
num_data = len(x)

# initialize U matrix
U = np.random.rand(num_data, 4)
C = np.empty((4, 2))

m = 2

# number of steps
for k in range(50):
    previous_U = np.copy(U)
    # the center of each cluster
    for j in range(4):
        numerator = 0
        denominator = 0
        # number of data
        for i in range(num_data):
            numerator += np.power(U[i, j], m) * x[i]
            denominator += np.power(U[i, j], m)

        C[j] = numerator/denominator

    for jj in range(4):
        for ii in range(num_data):
            numerator = x[ii] - C[jj]
            numerator_norm = np.linalg.norm(numerator)
            numerator_norm = np.power(numerator_norm, 2/(m-1))
            numerator_norm = 1/numerator_norm
            denominator = 0
            for center in range(4):
                d = x[ii] - C[center]
                d_norm = np.linalg.norm(d)
                d_norm = np.power(d_norm, 2/(m-1))
                denominator += 1/d_norm

            U[ii, jj] = numerator/denominator

    if np.linalg.norm(U - previous_U) < 0.3:
        break

f.scatter(C[:, 0], C[:, 1], c='red')
plt.show()
