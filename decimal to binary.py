x = int(input("Enter number to find binary: "))
l = []
if x == 0:
    print("0")
else:
    while x >= 1:
        l.append(x % 2)
        x = x // 2
    t = ""
    for d in l[::-1]:
        t += str(d)
    print(t)
