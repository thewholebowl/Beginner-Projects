def primes(t):
    l = []
    for i in range(2,t+1,1):
        prim = True
        for j in range(2,(i//2)+1,1):      #I did not use sqrt() because it causes errors in the first few numbers
            if i%j==0:
                prim = False
                break
            else:
                continue
        if prim:
            l.append(i)
    print(l)
s = int(input("Enter upper limit for the primes: "))
primes(s)

