# PROGRAM TO FIND MATRIX DETERMINANT, TRACE, IGENVALUES, IGENVECTORS AND SINGULAR VALUE DECOMPOSITION....

import numpy as np
from scipy import linalg
from scipy.linalg import svd

matrix01 = np.array([[1, 2],
                     [3, 4],])
print(f"-> Determinant of matrix       : {np.linalg.det(matrix01)}") # Gives the determinant of matrix...
print(f"-> Diagonal elements of matrix : {matrix01.diagonal()}") # Gives the diagonal elements of matrix...
print(f"-> Trace of matrix : {matrix01.trace()}") # Gives the diagonal elements of matrix...

# METHOD ONE OF GETTING EIGEN-VALUES AND EIGEN-VECTORS...
eigen_values, eigen_vectors = np.linalg.eig(matrix01)
print(f"\n-> Eigen Values : \n{eigen_values}")
print(f"-> Eigen Vectors : \n{eigen_vectors}")

# METHOD TWO OF GETTING EIGEN-VALUES AND EIGEN-VECTORS...
la,v=linalg.eig(matrix01)
l1,l2=la
print("-> The eigenvalues are : ",l1)
print("\n-> The eigen vectors are : ",l2)
print(v[:,0])
print(v[:,1])
print(np.sum(abs(v**2),axis=0))
v1=np.array(v[:,0]).T
print(linalg.norm(matrix01.dot(v1)-l1*v1))
U, singular, transopse= svd(matrix01)
print("\nThe singular value decomposition of matrix x is \n")
print("U is \n ",U)
print("\nsingular is\n ",singular)
print("\nV-transopse is \n ",transopse)
