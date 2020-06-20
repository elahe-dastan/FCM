# FCM
Fuzzy c-means (FCM) is a method of clustering which allows one piece of data to belong to two or more clusters.<br/>
This method is frequently used in pattern recognition.

# The algorithm
1.Initialize U=[uij] matrix, U(0) (The U matrix is initialized by random numbers in the beginning)<br/>
2.At k-step: calculate the centers vectors C(k)=[cj] with U(k)<br/>
3.Update U(k) , U(k+1)<br/>
4.If || U(k+1) - U(k)||< then STOP; otherwise return to step 2.

# Cost function
The cost function will be minimized when each point id belonged to a cluster more precisely and when the number of <br/.
clusters is fewer.

# Parameters 
I set parameter m to 2.

# Good clustering 
A good clustering is the one in which each point belongs to a cluster not more but if we continue adding more and more<br/>
clusters we'll have a cluster for each point which obviously is not what we are searching for so there is another factor<br/>
too, we should keep the number of clusters as few as possible.

