born = int(input("Please input the year you were born: "))
#Let the user input his/her born year
def favor_James(eighteen_year):
    eighteen_year=18+born
    #Calculate for the year when he/she is 18 years old
    if 1973<=eighteen_year<=1986:
        print("Your favourite James Bond is Roger Moore")
    elif 1987<=eighteen_year<=1994:
        print("Your favourite James Bond is Timothy Dalton")
    elif 1995<=eighteen_year<=2005:
        print("Your favourite James Bond is Pierce Brosnan")
    elif 2006<=eighteen_year<=2021:
        print("Your favourite James Bond is Daniel Craig")
    #Know who he/she will favor
    else:
        print("Please input a number between 1955 and 2003")
    #If nobody matches, tell the user maybe he/she input a year not included
favor_James(born)
#run the function so that in the loop it can print the result