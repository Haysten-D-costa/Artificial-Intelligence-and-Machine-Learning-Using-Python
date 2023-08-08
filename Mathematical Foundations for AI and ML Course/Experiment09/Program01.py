'''
Problem Statement:
We aim to visualize a Gaussian distribution, also known as a normal distribution. The distribution 
is defined by its mean and standard deviation. We want to plot the probability density function 
of the Gaussian distribution using a line plot.
'''

import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the Gaussian distribution
mu = 0    # mean
sigma = 1 # standard deviation

# Define the range of the x-axis
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

# Compute the values of the Gaussian distribution at each point on the x-axis
y = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mu)/sigma)**2)

# Plot the Gaussian distribution
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Probability density')
plt.title('Gaussian distribution')
plt.show()