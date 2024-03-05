a=40
b=36
c=30
d=a-b
e=b-c
#d is 4, e is 6
if d>e:
    print("the first month is more effective")
elif d<e:
    print("the second month is more effective")
else:
    print("the two months are equally effective") 
X=True
Y=False
W=(X or Y) and not (X and Y)
print(W)
#the truth table: 
#X Y W
#T T F
#T F T
#F T T
#F F F