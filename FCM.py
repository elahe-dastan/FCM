import numpy as np


class FCM:
    # c is the number of clusters
    def __init__(self, num_data, c, header, steps, data):
        self.num_data = num_data
        self.c = c
        self.header = header
        self.steps = steps
        self.data = data
        self.u = np.empty((num_data, c))
        self.centers = np.empty((self.c, len(self.header)))
        self.m = 2

    def run(self):
        # Initialize U matrix
        self.u = np.random.rand(self.num_data, self.c)

        # number of steps
        for k in range(self.steps):
            previous_u = np.copy(self.u)

            self.find_center()

            self.change_membership()
            if np.linalg.norm(self.u - previous_u) < 0.3:
                break

        return self.evaluation()

    def find_center(self):
        # the center of each cluster
        for j in range(self.c):
            numerator = 0
            denominator = 0
            # number of data
            for i in range(self.num_data):
                numerator += np.power(self.u[i, j], self.m) * self.data[i]
                denominator += np.power(self.u[i, j], self.m)

            self.centers[j] = numerator / denominator

    def change_membership(self):
        for j in range(self.c):
            for i in range(self.num_data):
                numerator = self.data[i] - self.centers[j]
                numerator_norm = np.linalg.norm(numerator)
                numerator_norm = np.power(numerator_norm, 2 / (self.m - 1))
                numerator_norm = 1 / numerator_norm
                denominator = 0
                for center in range(self.c):
                    d = self.data[i] - self.centers[center]
                    d_norm = np.linalg.norm(d)
                    d_norm = np.power(d_norm, 2 / (self.m - 1))
                    denominator += 1 / d_norm

                self.u[i, j] = numerator_norm / denominator

    def evaluation(self):
        e = 0
        for j in range(self.c):
            size = 1
            cluster_e = 0
            for i in range(self.num_data):
                distance = np.linalg.norm(self.data[i] - self.centers[j])
                membership = self.u[i, j] * distance
                if self.u[i, j] > (1/(size+2)):
                    size += 1
                cluster_e += membership
            e += cluster_e/size

        return e, self.centers
