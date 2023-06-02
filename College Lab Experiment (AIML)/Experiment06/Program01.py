'''
Problem Statement:
We are interested in visualizing the nth order derivatives of different functions. The code 
snippet provided uses the matplotlib and sympy libraries to compute and plot the first four 
order derivatives of a given function.
'''

import matplotlib.pyplot as plt
from sympy import *

def nthOrderDerivative(function, n):
    # Computes the nth order derivative of the function with respect to 'x' at each angle from -360 to 360 degrees
    derivatives = [diff(function, x, n).subs(x, (angle*pi)/180) for angle in range(-360, 361)]
    return derivatives

# Plots the first four order derivatives of a function 
def visualizeNthOrderDerivative(function, xaxix_label):
    plt.title('Visualizing nth Order Derivatives') # Set the title of the plot
    plt.xlabel(xaxix_label)
    plt.xticks(range(0, 721, 60), labels=[str(x) for x in range(-360, 361, 60)]) # Set the x-ticks for the plot ranging from -360 to 360 degrees with a step size of 60 degrees
    plt.plot(nthOrderDerivative(function, 1), label='1st Order Derivative')
    plt.plot(nthOrderDerivative(function, 2), label='2nd Order Derivative')
    plt.plot(nthOrderDerivative(function, 3), label='3rd Order Derivative')
    plt.plot(nthOrderDerivative(function, 4), label='4th Order Derivative')
    plt.legend()
    plt.show()

# Define the variable 'x' as a symbol
x = symbols('x')

# Call the visualizeNthOrderDerivative() function for each of the input functions
visualizeNthOrderDerivative(sin(x), 'sin(x)')
visualizeNthOrderDerivative(sin(x)/x, 'sin(x)/x')
visualizeNthOrderDerivative(cos(x**2), 'cos(x^2)')
visualizeNthOrderDerivative(x**5 - 3*x**4 + 2*x**3 + 4*x**2 - 5*x + 1, 'x^5 - 3x^4 + 2x^3 + 4x^2 - 5x + 1')