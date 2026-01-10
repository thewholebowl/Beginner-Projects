x = int(input("Enter any positive integer: "))
s = 0
l = len(str(x))
print()
for i in str(x):
    p = int(i)**l
    print(f"{i}**{l} = {p}")
    print(f"{s}+{p} = {s+p}")
    s = s+(p)
    print()
if s == x:
    print(f"{x} is an Armstrong Number")
else:
    print(f"{x} is not an Armstrong Number")
