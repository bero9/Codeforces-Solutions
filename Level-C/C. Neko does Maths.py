
def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i*i != n:
                divisors.append(n // i)
    return sorted(divisors)
import sys
import math
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    a = int(input_data[0])
    b = int(input_data[1])
    #print(math.lcm(a,b))
    D = abs(a-b)
    D_p = get_divisors(D)
    #print(D_p)
    min_lcm = float('inf')
    best_k = 0
    
    for i in D_p:
        k = (i - (a % i)) % i
        
        lcm = math.lcm(a+k,b+k)
        
        if lcm < min_lcm:
            min_lcm = lcm
            best_k = k
        elif lcm == min_lcm and k < best_k:
            best_k = k
            
    print(best_k)
 
if __name__ == '__main__':
    solve()