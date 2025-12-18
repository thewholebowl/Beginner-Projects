print("""1. Addition
2. Subtraction
3. Multiplication
4. Division""")
l = []
try:
    op = input("What do you want to do: ")
    op = op.lower().strip()
except:
    print("What are you trying to do?")
    quit(0)
if op=="1" or "addition" or "add" or "plus" or "+" or "sum":
    num = int(input("How many numbers to add: "))
    for i in range(0,num,1):
        l.append(int(input("Enter number: ")))
    print(f"The sum is {sum(l)}")
if op=="3" or "multiplication" or "multiply" or "into" or "x" or "*" or "mult":
    num = int(input("How many number to multiply: "))
    for i in range(0,num,1):
        l.append(int(input("Enter number: ")))
    mult = l[0]
    for i in range(1,len(l),1):
        mult = mult*l[i]
    print(f"The product is {mult}")
if op=="2" or "minus" or "subtraction" or "-":
    num = int(input("How many numbers to subtract: "))
    for i in range(0,num,1):
        l.append(int(input("Enter number: ")))
    sub = l[0]
    for i in range(1,len(l),1):
        sub = sub-l[i]
    print(f"The difference is {sub}")
if op=="aryan" or "divison" or "div" or "divide" or "upon"
