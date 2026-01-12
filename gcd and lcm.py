x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
#GREATEST COMMON DIVISOR
lx = []
ly = []
for i in range(1, x + 1):           #Although I recommend Euclidean Algorithm
    if x % i == 0:
        lx.append(i)
for i in range(1, y + 1):
    if y % i == 0:
        ly.append(i)
gcd = 1
for i in lx:
    if i in ly and i > gcd:
        gcd = i
print(f"The greatest common divisor is {int(gcd)}")
#LEAST COMMON MULTIPLE
print(f"The least common multiple is {int((x*y)/gcd)}")
