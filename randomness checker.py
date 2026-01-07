from random import *
from math import *
dsum = 0
L = []
try:
    t = int(input("Enter sample size :: "))
except:
    print("You entered something i did not like")
    quit(0)
if t < 0:
    print("Why did you put a negative number?")
    quit(0)
elif t==0:
    print("You know the result will be zero")
    quit(0)
else:
    pass
for i in range(1,t,1):
    x = randint(1,9)
    L.append(x)
for i in range(1,10,1):
    print(f"{i} appears {L.count(i)} times")
for i in range(1,10,1):
    print(f"Deviation from normal distribution of {i} is {floor(abs((t/9)-L.count(i)))}")
for i in range(1,10,1):
    dsum = dsum + floor(abs((t/9)-L.count(i)))
print(f"Total deviation sum is {dsum}")
print(f"Mean percentage deviation from normal singular distribution is {round(abs(((dsum/t)*100)),3)}%")
print(f"Probability of randomness is {100 - round(abs(((dsum/t)*100)),3)}%")
if 100 - round(abs(((dsum/t)*100)),3) >98:
    print("                                 YOUR RANDOM NUMBER GENERTOR IS RANDOM")
else:
    print("                         YOUR RANDOM NUMBER GENERATOR IS NOT RANDOM ENOUGH")
