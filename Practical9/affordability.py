money=int(input("Please input your total money: "))
price=int(input("Please input the price of chocolate: "))
#Let the user input the money and price
def calculator(money,price):
    #Definine the calculator function
    number=money//price
    #Calculate the number of bars that can be bought
    change=money-number*price
    #Calculate the change that will be left over
    return (number,change)
    #Return them so that we can extract them from the function running result
affordability=calculator(money,price)
#Run this fuction and save the running result
print(f"You can afford {affordability[0]} chocolate bars and have {affordability[1]} left over.")
#Example: You can input 100 as the total money, and 7 as the price of one chocolate bar.
#Then you will have the output:
#You can afford 14 choclate bars and have 2 left over.