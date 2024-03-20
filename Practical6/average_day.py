average_day={'sleeping':8,'classes':6,'studying':3.5,'TV':2,'music':1,'other':3.5}
#create a dictionary
print(average_day)
#print this dictionary

import matplotlib.pyplot as plt
time_day=[8,6,3.5,2,1,3.5]
activities=['sleeping','classes','studying','TV','music','other']
#store the data used for the pie chart
plt.figure()
plt.pie(time_day, labels=activities, startangle=90, autopct='%1.1f%%')
#the pie chart use the values in time_day, and labels in activities
#this chart also display the percentage of every activity
plt.show()
#show this chart
plt.clf()
#close