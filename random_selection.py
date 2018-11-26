import random as rand
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create a list of names
members = ['james','michael','shelmith','cyrus','naomi','christine']

# reshuffle the list before hand
rand.shuffle(members)
print(members)

# randomly select one element
print(rand.choice(members))

# randomly select 3 elemnts with replacement
print(rand.choices(members, k=3))

# randomly sample without replacement
print(rand.sample(members, 3))

# sample values from the normal distribution
# define mean and standard deviation
mu, sigma = 30, 10
age = np.random.normal(mu, sigma, 1000)
print(age[1:10])

# plot a histogram
plt.hist(age, bins = 30, density=True)
#plt.xlabel('Age')
#plt.ylabel('Density')
#plt.title('Distribution of Age')
plt.show



