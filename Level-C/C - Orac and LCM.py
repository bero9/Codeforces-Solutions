
import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    List = [int(x) for x in input_data[1:n+1]]
    
    if n == 1:
        print(List[0])
        return

    suffix_gcd = [0] * n
    suffix_gcd[n-1] = List[n-1]
    
    for i in range(n-2, -1, -1):
        suffix_gcd[i] = math.gcd(List[i], suffix_gcd[i+1])
        
    ans = 0
    
    for i in range(n-1):
        l = math.lcm(List[i], suffix_gcd[i+1])
        if i == 0:
            ans = l
        else:
            ans = math.gcd(ans, l)
            
    print(ans)

if __name__ == '__main__':
    solve()