import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# first of all I have to read the data
data = pd.read_csv("sample1.csv")

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
for k in range(5):
    previous_U = np.copy(U)
    # the center of each cluster
    for j in range(4):
        numerator = 0
        denominator = 0
        # number of data
        for i in range(num_data):
            numerator += U[i, j] * x[i]
            denominator += U[i, j]

        C[j] = numerator/denominator

    for j in range(4):
        for i in range(num_data):
            numerator = 1/(x[i] - C[j])
            numerator = np.power(numerator, 2/(m-1))
            numerator_norm = np.linalg.norm(numerator)
            denominator = 0
            for center in range(4):
                denominator += 1/abs(x[i] - C[center])
            denominator = np.power(denominator, 2/(m-1))
            denominator_norm = np.linalg.norm(denominator)

            U[i, j] = numerator_norm/denominator_norm

    if np.linalg.norm(U - previous_U) < 0.3:
        break

    f.scatter(C[:, 0], C[:, 1], c='red')
    plt.show()
