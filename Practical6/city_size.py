uk_values=[0.56,0.62,0.04,9.7]
china_values=[0.58,8.4,29.9,22.2]
#store the values of both uk and china
uk_values.sort()
china_values.sort()
#sort the values in the two lists respectively
print('Sorted uk people values are ',uk_values,' Sorted china people values are ',china_values)
#print the two sorted lists

uk_cities=['Edinburgh','Glasgow','Stirling','London']
uk_people=[0.56,0.62,0.04,9.7]
china_cities=['Haining','Hangzhou','Shanghai','Beijing']
china_people=[0.58,8.4,29.9,22.2]
#store the population size data

import matplotlib.pyplot as plt
import numpy as np
figure,(ax1,ax2)=plt.subplots(1,2,figsize=(12,6))
#create two plots and let them show above and below
ax1.bar(uk_cities,uk_people)
#the first bar is for uk city size
for i,v in enumerate(uk_people):
    ax1.text(i,v+0.1,str(v),ha='center',va='bottom')
#display the accurate numbers
ax1.set_xlabel("City")
ax1.set_ylabel("People(millions)")
ax1.set_title("City size of UK")
#let the ax1 figure display the meaning of x axis and y axis
ax2.bar(china_cities,china_people)
#the second bar is for china city size
for i,v in enumerate(china_people):
    ax2.text(i,v+0.1,str(v),ha='center',va='bottom')
#display the accurate numbers
ax2.set_xlabel("City")
ax2.set_ylabel("People(millions)")
ax2.set_title("City size of China")
#let the ax2 figure display the meaning of x axis and y axis
plt.tight_layout()
#adjust the space between ax1 and ax2
plt.show()
#show the figure
plt.clf()