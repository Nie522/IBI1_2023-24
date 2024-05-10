import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#import useful libraries

N = 10000 #Total people
I = 1 #Infected people initially
R = 0 #Resistant people initially
#create the variables
beta = 0.3 #define infection rate
gamma = 0.05 #define recovery rate

vaccination_rates = np.linspace(0, 1, 11)  # From 0% to 100% in 11 steps
#vaccination_rates = np.arange(0, 1.1, 0.1)  # From 10% to 100% in steps of 10%
#vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
#define the vaccination rates from 0% to 100%
arrays_s = {rate: [] for rate in vaccination_rates}
arrays_i = {rate: [] for rate in vaccination_rates}
arrays_r = {rate: [] for rate in vaccination_rates}
#initialise the arrays to store S, I and R

for rate in vaccination_rates:
    V = int ((N - I) * rate)
    # Calculate the initial number of susceptible people
    S = N - I - V
    #define vaccinated people as rate * population
    
    # Run the model for 1000 time steps
    for t in range(1000):
        # Calculate the number of new infections
        new_I = S * I / N * beta

        # Update the number of susceptible and infected people
        S -= new_I
        I += new_I
        
        # Calculate the number of new recoveries
        new_R = I * gamma
        
        # Update the number of infected and recovered people
        I -= new_R
        R += new_R
        
        # Record the number of people at each time point
        arrays_s[rate].append(S)
        arrays_i[rate].append(I)
        arrays_r[rate].append(R)

# Plot the model results for each vaccination rate
plt.figure(figsize=(8, 6), dpi=150)

# Plot each curve with a different color from the colormap
for rate, array_i in arrays_i.items():
    # Get color from the colormap based on the vaccination rate
    plt.plot(array_i, label=f'Infected (Vaccination: {int(rate*100)}%)', color=cm.viridis(rate), linestyle='-')

plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.show()
# show the plot
'''
plt.savefig("SIR_model.png", format='png')
#save the plot as SIR_model.png
'''