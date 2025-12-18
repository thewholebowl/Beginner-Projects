l = []
try:
    tobe = input("Enter string to be ciphered: ")
except:
    print("What are you doing?")
    quit()
tobe = tobe.strip().lower()
c = input("Enter shift number: ")
if len(c)<1:
    print("What are you doing?")
    quit()
c = int(c)%26
for i in tobe:
    x = ord(i)+c
    if i==" ":
        pass
    elif x<122:
        l.append(chr(x))
    else:
        while x>122:
            x = x-26
        l.append(chr(x))
for j in l:
    print(j,end="")
