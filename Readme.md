# FCM
Fuzzy c-means (FCM) is a method of clustering which allows one piece of data to belong to two or more clusters.<br/>
This method is frequently used in pattern recognition.

# The algorithm
1.Initialize U=[uij] matrix, U(0)<br/>
2.At k-step: calculate the centers vectors C(k)=[cj] with U(k)<br/>
3.Update U(k) , U(k+1)<br/>
4.If || U(k+1) - U(k)||< then STOP; otherwise return to step 2.