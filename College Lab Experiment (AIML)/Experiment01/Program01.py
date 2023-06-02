# PROGRAM TO SOLVE SYSTEM OF LINEAR EQUATIONS IN ONE VARIABLE...

"""
Created on Fri Mar 3 15:23:34 2023
Experiment 01 (On Linear Equations in one variables)...
@author: Haysten D'costa
"""
def equation(a, b, c): # Function definition...
    x = -(b + c)/a
    return x

a = int(input("Enter the value for a : "))
b = int(input("Enter the value for b : "))
c = int(input("Enter the value for c : "))
result = equation(a, b, c)
print(f"Result of the equation is : {result}")
