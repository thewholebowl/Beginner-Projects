from math import *
x = int(input("Enter number of rows of Pascal's Triangle: "))
for i in range(1,x+1,1):
    for j in range(x-i,-1,-1):
        print("   ",end="")
    for k in range(1,i+1,1):
        r = factorial(i-1)
        e = factorial(k-1)
        d = factorial(i-k)
        print(int(r/(e*d)),end="   ")
    print()
