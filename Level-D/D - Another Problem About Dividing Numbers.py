def sieve(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)
    
    return res
num = int((10**9)**0.5)+1
primes = sieve(num)
def pf(number):
    sn = 0
    for p in primes:
        while number%p==0:
            number = number//p
            sn+=1
    if number >1:
        sn+=1
    return sn
t = int(input())
for _ in range(t):
    a,b,k = map(int,input().split())
    pfa = pf(a)
    pfb = pf(b)
    sup = pfa+ pfb
    if a==b and k==1:
        print("No")
        continue
    if a%b==0 or b%a==0:
        if 1<=k<=sup:
            print("Yes")
        else:
            print("No")
    else:
        if 2<=k<=sup:
            print("Yes")
        else:
            print("No")