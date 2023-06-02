# SOLVING SYSTEM OF LINEAR EQUATION IN MORE THAN ONE (MULTIPLE) VARIABLE...

import numpy as np
import numpy.linalg as la

eq = int(input("Enter no. of equations : "))
x = int(input("Enter the no. of coefficients for equation 1 : "))
list1 = []
print("Enter the coefficients : ")
for i in range(x):
    values1 = int(input())
    list1.append(values1)
    
y = int(input("Enter the no. of coefficients for equation 2 : "))
list2 = []
print("Enter the coefficients : ")
for i in range(y):
    values2 = int(input())
    list2.append(values2)
    
list1.extend(list2)
matrix1 = []
while list1!=[]:
    matrix1.append(list1[:2])
    list1 = list1[2:]
print(matrix1)
print("Enter the constant values for the equation : ")
list3 = []

for i in range(eq):
    values3 = int(input())
    list3.append(values3)

print("Equations are : ")
print(f"    Equation 01 : 1x + 2y = 5")
print(f"    Equation 02 : 3x + 4y = 6")
    
print("\nRESULT : \n")
matrix2 = []
while list3!=[]:
    matrix2.append(list3[:1])
    list3 = list3[1:]
print(matrix2)
matrix1inv = la.inv(matrix1)
result = matrix1inv.dot(matrix2)
print(result)
    