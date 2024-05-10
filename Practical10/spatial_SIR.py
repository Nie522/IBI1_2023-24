import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100,100))
# Create a 100×100 array completely made of zeroes

outbreak = np.random.choice(range(100),2) 
# Randomly select the x and y coordinates of where the outbreak is happening 
population[outbreak[0], outbreak[1]] = 1
# Change the two status from 0 (susceptible) to 1 (infected)

N = 10000 #Total people
I = 1 #Infected people initially
R = 0 #Resistant people initially
#create the variables
beta = 0.3 #define infection rate
gamma = 0.05 #define recovery rate

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Initial State')
plt.show()
# Plot the initial state

for t in range(100):
# create the loop of 100 times
    infectedIndex = np.where(population==1)
    # find infected points
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # get x, y coordinates for each point
        # infect each neighbour with probability beta
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
            # infect all 8 neighbours
            # this is a bit finicky, may we use dx, dy to test the specific distance
                if (xNeighbour,yNeighbour) != (x,y):
                # Make sure the infector self isn't infected
                # This step is not necessary in practice because the infected person will not re-infect himself
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # make sure I don't fall off an edge
                        if population[xNeighbour,yNeighbour]==0:
                        # only infect neighbours that are not already infected!
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for new infected point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
    new_I = np.where(population == 1)
    for x,y in zip(new_I[0],new_I[1]):
        if np.random.choice([0, 1], p=[1 - gamma, gamma]):
            population[x,y] = 2  # change the new recovery point into 2

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Final State')
plt.show()
# plot the final state