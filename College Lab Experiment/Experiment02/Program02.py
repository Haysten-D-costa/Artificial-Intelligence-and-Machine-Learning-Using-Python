# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:25:06 2023
Experiment 02 : Program 01
@author: Master Haysten D'costa
"""
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
#print(list1)
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

print(list3)
print("Equations are : ")
print(f"    Equation 01 : {list1[0]}x + {list1[1]}y = {list3[0]}")
print(f"    Equation 02 : {list2[0]}x + {list2[1]}y = {list3[1]}")
    
#print(list3)
matrix2 = []
while list3!=[]:
    matrix2.append(list3[:1])
    list3 = list3[1:]
    
print(matrix2)
matrix1inv = la.inv(matrix1)
result = matrix1inv.dot(matrix2)
print(result)
    