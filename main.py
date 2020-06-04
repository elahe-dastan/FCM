import pandas as pd
import matplotlib.pyplot as plt
import FCM

# First of all I have to read the data
header = pd.read_csv('test.csv', nrows=0).columns.tolist()
data = pd.read_csv("sample1.csv")

if len(header) == 2:
    # Plot the data
    fig = plt.figure()
    f = fig.add_subplot()
    f.scatter(data[header[0]], data[header[1]], c='b')

max_num_clusters = 11
x = data.values
num_data = len(x)
steps = 50
minimum_error = 10000000
best_num_clusters = 0

# Defining answer
for c in range(1, max_num_clusters):
    e, centers = FCM.run(num_data, c, header, steps, x)
    print(e)
    if e < minimum_error:
        minimum_error = e
        best_num_clusters = c

if len(header) == 2:
    ce = 0
    for ce in range(best_num_clusters):
        f.scatter(centers[ce, 0], centers[ce, 1], c='red')
    plt.show()
