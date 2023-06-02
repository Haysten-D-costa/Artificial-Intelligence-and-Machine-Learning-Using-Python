# PROGRAM TO PERFORM OPERATIONS On MATRICES AND VECTORS...

import numpy as np
row_vector = np.array([1, 2, 3, 4, 5]) # Row vector...
column_vector = np.array([[1], [2], [3], [4], [5]]) # Column vector...
print(row_vector[0])
print(row_vector[1])
print(row_vector[2])
print(row_vector[3])
print(row_vector[4])

vector_matrix = ([[1, 2, 3],[4, 5, 6]])
print(vector_matrix)

# ADDITION OF TWO MATRICES :
x = np.array([[1, 2], [4, 5]])  # Matrix 1
y = np.array([[7, 8], [9, 10]]) # Matrix 2
z = np.array([[4, 9], [16, 25]])

print(f"\nElement wise Addition : \n{np.add(x, y)}")
print(f"\nElement wise Subtration : \n{np.subtract(x, y)}")
print(f"\nElement wise Multiplication : \n{np.multiply(x, y)}")
print(f"\nElement wise Division : \n{np.divide(x, y)}")
print(f"\nInverseL Mult method : \n{np.dot(x, y)}")

print(f"\nSquare root of matrix 'z' : \n{np.sqrt(z)}")
print(f"\nSum of elements of matrix 'z' : \n{np.sum(z)}")
print(f"\nSum of elements of matrix 'z' : \n{np.sum(z, axis=0)}") # Column wise addition...
print(f"\nSum of elements of matrix 'z' : \n{np.sum(z, axis=1)}") # Row wise addition...
print(f"\nTranspose of matrix 'z' : \n{(z.T)}") # Column wise addition...
print(f"\nElement wise max of matrix 'z' : \n{np.max(z)}") # Finding element wise max...
print(f"\nElement wise min of matrix 'z' : \n{np.min(z)}") # Finding element wise min...

print(f"\nAverage of elements in z : {np.mean(z)}")
print(f"\nVarience of elements in z : {np.var(z)}")
print(f"\nStandard Deviation of elements in z : {np.std(z)}")
print(f"\nInverse of matrix 'z' : \n{np.linalg.inv(z)}")
print(f"\nRank of matrix 'z' : \n{np.linalg.matrix_rank(z)}")
