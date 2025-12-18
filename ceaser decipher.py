code = input("Enter string to be deciphered: ")
for i in range(1,26,1):
    for j in code:
        x = ord(j)+i
        if x>122:
            while x>122:
                x = x-26
            print(chr(x),end="")
        else:
            print(chr(x),end="")
    print()
