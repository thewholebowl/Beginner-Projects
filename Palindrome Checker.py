def palindrome_checker(t):
    t = t.strip().lower()
    l1 = list(t)
    l2 = []
    for i in range(-1,-len(t)-1,-1):
        l2.append(t[i])
    if l1==l2:
        return "The string is a palindrome"
    else:
        return "The string is not a palindrome"
t = input("Enter word to check if it is a palindrome: ")
print(palindrome_checker(t))
