import sys
def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    
    primes = [i for i, alive in enumerate(is_prime) if alive]
    return primes

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1]) 
    List  = get_primes(n)
    ans=0
    for i in range(len(List)-1):
        num = List[i] +List[i+1] +1
        if num in List:
            ans+=1
    if ans>=k:
        print("YES")
    else:
        print("NO")

        
 
if __name__ == '__main__':
    solve()




