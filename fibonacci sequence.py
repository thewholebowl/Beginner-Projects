a = 0 #first term
b = 1 #second term
num = int(input("Enter number of terms for fibonnaci sequence: ")) #ask for number of terms
print(a) #first term
print(b) #second term
for i in range(0,num): #loop to calculate and print num terms
    c = a+b #calculate C
    print(c)
    a = b #increasing the term value
    b = c
