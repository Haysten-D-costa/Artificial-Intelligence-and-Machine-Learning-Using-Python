# PROGRAM TO SOLVE SYSTEM OF LINEAR EQUATIONS IN ONE VARIABLE...

"""
Created on Fri Mar  3 15:38:18 2023
Experiment 02 (On Linear Equations in one variables)...
@author: Haysten D'costa
"""
def equation(a, b, c, d): # Function definition...
    if(a == c):
        print("Equation has Infinitely many solutions...")
    elif(d == b):
        print("Equation has No solution...")
    else:
        x = (d - b)/(a - c)
        print(f"Solution of the equation is {x}")

a = int(input("Enter the value for a : "))
b = int(input("Enter the value for b : "))
c = int(input("Enter the value for c : "))
d = int(input("Enter the value for d : "))
equation(a, b, c, d)