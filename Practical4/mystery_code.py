# What does this piece of code do?
# Answer: generate 100 random numbers between 1 and 10 and sum them

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0 #the initial count is zero
total_random_number=0 #the initial total number is zero
while progress<100: #total count is 0-99, is 100
	progress+=1 #the number of progress in each loop is increased by one
	n = randint(1,10) #generate a random number between 1 and 10
	total_random_number = total_random_number+n #add up total_random_number and random number

print(total_random_number)
