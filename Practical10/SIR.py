import numpy as np
import matplotlib .pyplot as plt
#import necessary libraries
N = 10000 #Total people
I = 1 #Infected people initially
S = N-I #Susceptible people
R = 0 #Resistant people initially
#create the variables
beta = 0.3 #define infection rate
gamma = 0.05 #define recovery rate
array_i = [I]
array_s = [S]
array_r = [R]
#create arrays to store the change of key variables
for t in range(1000):
#create a loop of 1000 times
#In each loop, pick susceptible individuals at random to become infected
#Then pick infected individuals at random to become recovered
    new_I = S * I / N * beta
    #calculate the number of new infectors
    #susceptible_to_infect = np.random.choice(range(S), size=new_I, replace=False)
    #I think this is no use so I delete it
    #randomly choose new infectors; 'replace = False' is to choose without repetition
    S -= new_I
    I += new_I
    #update the number of S and I
    new_R = I * gamma
    #calculate the number of new recovery
    #infected_to_recover = np.random.choice(range(I), size=new_R, replace=False)
    #I think this is no use so I delete it
    #randomly choose new recovered people; 'replace = False' is to choose without repetition
    I -= new_R
    R += new_R
    #update the number of I and R
    array_s.append(S)
    array_i.append(I)
    array_r.append(R)
    #record the number of people at each point in this time
plt.figure(figsize=(6, 4), dpi=150)
#set up the dimensions and resolution of this figure
plt.plot(array_s, label='Susceptible')
plt.plot(array_i, label='Infected')
plt.plot(array_r, label='Recovered')
#the plot include arrays of S, I and R
plt.xlabel('Time')
#x axis represents time
plt.ylabel('Number of People')
#y axis representss number of people
plt.title('SIR Model')
#the title is SIR model
plt.legend()
plt.show()
#show the plot
'''
plt.savefig("SIR_model.png", format='png')
#save the plot as SIR_model.png
plt.close()
'''