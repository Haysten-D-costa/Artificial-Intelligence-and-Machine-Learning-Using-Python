import numpy
import numpy.linalg as linear_algebra

no_of_variables = int(input('Enter the number of variables : '))
A = []
B = []

for i in range(no_of_variables):
    coefficients = input(f'Enter the Coefficients of Equation Number {i+1} : ')
    coefficients = [int(x) for x in coefficients.split()]
    A.append(coefficients)

constants = input('Enter the Constants : ')
constants = [B.append([int(x)]) for x in constants.split()]

A = numpy.array(A)
B = numpy.array(B)

A_inverse = linear_algebra.inv(A)
X = A_inverse.dot(B)

print('\nSolutions :-')
for i in range(len(X)):
    variable = chr(122 - (len(X)-1-i))
    print(variable, '=' , round(X[i][0], 2))