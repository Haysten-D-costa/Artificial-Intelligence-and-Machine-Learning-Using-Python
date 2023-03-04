"""
Created on Fri Mar 3 15:23:34 2023
Experiment 01 (On Equations)...
@author: Haysten Dcosta
"""
def equation(a, b, c):
    x = -(b + c)/a
    return x

a = int(input("Enter the value for a : "))
b = int(input("Enter the value for b : "))
c = int(input("Enter the value for c : "))
result = equation(a, b, c)
print(f"Result of the equation is : {result}")
