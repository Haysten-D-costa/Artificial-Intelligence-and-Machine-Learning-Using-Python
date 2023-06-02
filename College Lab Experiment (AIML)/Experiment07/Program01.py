'''
Problem Statement:
We want to understand the relationship between weather conditions and the probability of 
people using an umbrella. To investigate this, we collected data on rainy and non-rainy 
days and determined the corresponding conditional probabilities of people using an umbrella. 
The problem is to visualize this information using a bar chart.

Given Information:
- The probability of rain is 0.3 (30% chance of rain).
- Given that it is raining, the probability of using an umbrella is 0.8 (80% chance).
- Given that it is not raining, the probability of using an umbrella is 0.2 (20% chance).

Solution:
To depict the conditional probabilities graphically, we use a bar chart. The chart will 
have the weather conditions ('Rain' and 'No Rain') on the x-axis and the probability of 
using an umbrella on the y-axis.
'''

import matplotlib.pyplot as plt

# Conditional probabilities
rain_prob = 0.3
umbrella_given_rain_prob = 0.8
umbrella_given_no_rain_prob = 0.2

# Data for the bar chart
x = ['Rain', 'No Rain']
y = [umbrella_given_rain_prob, umbrella_given_no_rain_prob]

# Plotting the bar chart
plt.bar(x, y)
plt.xlabel('Weather')
plt.ylabel('Probability of Using Umbrella')
plt.title('Conditional Probability: Use of Umbrella given Weather')
plt.show()