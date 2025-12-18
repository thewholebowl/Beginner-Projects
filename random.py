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
print(f"1 appears {L.count(1)} times")
print(f"2 appears {L.count(2)} times")
print(f"3 appears {L.count(3)} times")
print(f"4 appears {L.count(4)} times")
print(f"5 appears {L.count(5)} times")
print(f"6 appears {L.count(6)} times")
print(f"7 appears {L.count(7)} times")
print(f"8 appears {L.count(8)} times")
print(f"9 appears {L.count(9)} times")
print(f"Deviation from normal distribution of 1 is {floor(abs((t/9)-L.count(1)))}")
print(f"Deviation from normal distribution of 2 is {floor(abs((t/9)-L.count(2)))}")
print(f"Deviation from normal distribution of 3 is {floor(abs((t/9)-L.count(3)))}")
print(f"Deviation from normal distribution of 4 is {floor(abs((t/9)-L.count(4)))}")
print(f"Deviation from normal distribution of 5 is {floor(abs((t/9)-L.count(5)))}")
print(f"Deviation from normal distribution of 6 is {floor(abs((t/9)-L.count(6)))}")
print(f"Deviation from normal distribution of 7 is {floor(abs((t/9)-L.count(7)))}")
print(f"Deviation from normal distribution of 8 is {floor(abs((t/9)-L.count(8)))}")
print(f"Deviation from normal distribution of 9 is {floor(abs((t/9)-L.count(9)))}")
for i in range(1,10,1):
    dsum = dsum + floor(abs((t/9)-L.count(i)))
print(f"Total deviation sum is {dsum}")
print(f"Mean percentage deviation from normal singular distribution is {round(abs(((dsum/t)*100)),3)}%")
print(f"Probability of randomness is {100 - round(abs(((dsum/t)*100)),3)}%")
if 100 - round(abs(((dsum/t)*100)),3) >98:
    print("                                 YOUR RANDOM NUMBER GENERTOR IS RANDOM")
else:
    print("                         YOUR RANDOM NUMBER GENERATOR IS NOT RANDOM ENOUGH")
