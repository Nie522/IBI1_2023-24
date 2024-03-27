import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import a few python libraries

#os.chdir("C:/Users/Nie522/Downloads")
#to the directory in which the file was saved

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#use the pandas library to read the content into a dataframe

my_columns = [False, False, False, True]
#only print the forth column
a = dalys_data.iloc[0:101:10, my_columns]
#from every 10th row starting from the first row, for the first 100 rows
print(a)
#show the DALYs

rows = dalys_data.loc[:, "Entity"]
#extract column "Enitity" as rows
my_rows = rows == 'Afghanistan'
#Convert rows to a list stored as Boolean
b = dalys_data.loc[my_rows, "DALYs"]
#use loc function to distract the DALYs of Afghanistan
print(b)

china_data = dalys_data.loc[rows == "China", :]
#extract the DALYs data of china as china_data
china_mean = np.mean(china_data.DALYs)
#calculate the mean of DALYs in china_Data
print("The mean of china DALYs is", china_mean)

plt.plot(china_data.Year, china_data.DALYs, 'g.')
#draw the plot of years and DALYs
#r, g, b, y, c, m, k are the symbols of color
#-: full line --: broken line -.: dot dash line :: dotted line
#o, s, ^, v, >, <, x, +, . are symbols of data points
plt.xticks(china_data.Year, rotation=-90)
#let the x labels rotate 90 degrees clockwise
plt.title('DALYs over time in China')
plt.xlabel('Year')
plt.ylabel('DALYs')
#add information about this plot
plt.show()
plt.clf()
#show the plot

UK_data = dalys_data.loc[rows == "United Kingdom", :]
#extract the DALYs data of UK
plt.plot(china_data.Year, china_data.DALYs, label='China', color='red')
#draw the data plot of china and add label. This line is red and full.
plt.plot(UK_data.Year, UK_data.DALYs, label='UK', color='blue')
#draw the data plot of UK and add label. This line is blue and full.  
plt.legend()
#display legend
plt.title('DALYs over years in China and UK')
plt.xlabel('Year')
plt.ylabel('DALYs')
#add information about this plot
plt.show()
plt.clf()
#show the plot