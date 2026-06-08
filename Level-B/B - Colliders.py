import sys

MAX_N = 100005

spf = [i for i in range(MAX_N)]

def precompute_spf():

    for i in range(2, int(MAX_N**0.5) + 1):
        if spf[i] == i:  # إذا كان الرقم أولياً
            for j in range(i * i, MAX_N, i):
                if spf[j] == j:
                    spf[j] = i

def get_prime_factors(x):

    factors = []
    while x > 1:
        p = spf[x]
        factors.append(p)

        while x % p == 0:
            x //= p
    return factors

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    is_on = [False] * (n + 1)          
    active_factors = [0] * MAX_N       
    
    precompute_spf()
    
    idx = 2
    output = []
    
    for _ in range(m):
        op = input_data[idx]
        x = int(input_data[idx+1])
        idx += 2
        
        if op == '+':
            if is_on[x]:
                output.append("Already on")
            else:
                factors = get_prime_factors(x)
                conflict_collider = 0
                
                for p in factors:
                    if active_factors[p] != 0:
                        conflict_collider = active_factors[p]
                        break
                
                if conflict_collider != 0:
                    output.append(f"Conflict with {conflict_collider}")
                else:
                    output.append("Success")
                    is_on[x] = True
                    for p in factors:
                        active_factors[p] = x
                        
        elif op == '-':
            if not is_on[x]:
                output.append("Already off")
            else:
                output.append("Success")
                is_on[x] = False
                factors = get_prime_factors(x)
                for p in factors:
                    active_factors[p] = 0
                    
    print('\n'.join(output))

if __name__ == '__main__':
    solve()