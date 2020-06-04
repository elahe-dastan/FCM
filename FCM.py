import numpy as np


# c is the number of clusters
def run(num_data, c, header, steps, data):
    # Initialize U matrix
    u = np.random.rand(num_data, c)
    centers = np.empty((c, len(header)))

    m = 2

    # number of steps
    for k in range(steps):
        previous_u = np.copy(u)
        # the center of each cluster
        for j in range(c):
            numerator = 0
            denominator = 0
            # number of data
            for i in range(num_data):
                numerator += np.power(u[i, j], m) * data[i]
                denominator += np.power(u[i, j], m)

            centers[j] = numerator / denominator

        for jj in range(c):
            for ii in range(num_data):
                numerator = data[ii] - centers[jj]
                numerator_norm = np.linalg.norm(numerator)
                numerator_norm = np.power(numerator_norm, 2 / (m - 1))
                numerator_norm = 1 / numerator_norm
                denominator = 0
                for center in range(c):
                    d = data[ii] - centers[center]
                    d_norm = np.linalg.norm(d)
                    d_norm = np.power(d_norm, 2 / (m - 1))
                    denominator += 1 / d_norm

                u[ii, jj] = numerator_norm / denominator

        if np.linalg.norm(u - previous_u) < 0.3:
            break

    # Evaluation
    e = 0
    for jjj in range(c):
        size = 0
        cluster_e = 0
        for iii in range(num_data):
            distance = np.linalg.norm(data[iii] - centers[jjj])
            membership = u[iii, jjj] * distance
            if u[iii, jjj] > 0.5:
                size += 1
            cluster_e += membership
        e += cluster_e/size

    return e, centers
