# PROGRAM TO SOLVE SYSTEM OF LINEAR EQUATIONS MORE THAN ONE(MULTIPLE) VARIABLE...

import numpy as np
import numpy.linalg as la

A = np.array([[1,2],[3,4]])
B = np.array([[5],[6]])
Ainv = la.inv(A)
x = Ainv.dot(B)

print(f"The equations are : {A[0][0]}x + {A[0][1]}y = {B[0]}")
print(f"\t\t    {A[1][0]}x + {A[1][1]}y = {B[1]}\n")
print(f"RESULT : \n-> The value of x is  : {x[0]}")
print(f"-> The value of y is  : {x[1]}")
