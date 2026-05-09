import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("Addition:\n", A+B)
print("Subtraction:\n", A-B)
print("Multiplication:\n", np.dot(A,B))
print("Inverse of A:\n", np.linalg.inv(A))

'''
output
Addition:
[[ 6  8]
 [10 12]]

Subtraction:
[[-4 -4]
 [-4 -4]]

Multiplication:
[[19 22]
 [43 50]]

Inverse of A:
[[-2.   1. ]
 [ 1.5 -0.5]]

 '''
