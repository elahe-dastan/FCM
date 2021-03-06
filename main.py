import pandas as pd
import matplotlib.pyplot as plt
import FCM
import sys

# I get the name if the data file as an argument
file_name = sys.argv[1]

# I have to read the data from the file
header = pd.read_csv(file_name, nrows=0).columns.tolist()
data = pd.read_csv(file_name)

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
for c in range(2, max_num_clusters):
    fcm = FCM.FCM(num_data, c, header, steps, x)
    e, centers = fcm.run()
    print(e)
    if e < minimum_error:
        minimum_error = e
        best_num_clusters = c

if len(header) == 2:
    ce = 0
    for ce in range(best_num_clusters):
        f.scatter(centers[ce, 0], centers[ce, 1], c='red')
    plt.show()
