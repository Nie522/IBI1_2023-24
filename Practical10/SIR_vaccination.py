import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#import useful libraries

N = 10000  # Total people
I = 1  # Infected people initially
R = 0  # Recovered people initially
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate

# Define vaccination rates from 0% to 100%
vaccination_rates = np.linspace(0, 1, 11)
arrays_i = {rate: [] for rate in vaccination_rates}

for rate in vaccination_rates:
    # Calculate the initial number of susceptible people
    S = int(N * (1 - rate))
    # Reset infected and recovered for each rate
    I = 1
    R = 0

    # Initialize the array to store the number of infected people
    infected_over_time = []

    for t in range(1000):
        # Calculate contact rate, ensuring it does not exceed 1
        contact_rate = min(beta * I / N, 1)

        # Simulate new infections
        new_infections = np.random.binomial(S, contact_rate)
        new_I = I + new_infections

        # Simulate recoveries
        new_recoveries = np.random.binomial(I, gamma)
        new_R = R + new_recoveries

        # Update the counts
        S -= new_infections
        I = new_I - new_recoveries
        R = new_R

        # Record the number of infected people at each time point
        infected_over_time.append(I)

    # Store the results for each vaccination rate
    arrays_i[rate] = infected_over_time

# Plot the model results for each vaccination rate
plt.figure(figsize=(8, 6), dpi=150)

for rate, infected_series in arrays_i.items():
    # Use a colormap to differentiate the lines for each vaccination rate
    plt.plot(infected_series, label=f'Infected (Vaccination: {int(rate*100)}%)', color=cm.viridis(rate))

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.show()

# Save the plot as an image file
plt.savefig("./SIR_model_vaccination.png")