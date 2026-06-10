import sys
import math
MAX_VAL = 100000

divisors = [[] for _ in range(MAX_VAL + 1)]

def precompute_divisors():
    for i in range(1, MAX_VAL + 1):
        for j in range(i, MAX_VAL + 1, i):
            divisors[j].append(i)

precompute_divisors()

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    List = []
    
    last_seen = [0] * (MAX_VAL + 1) 
    
    for i in range(1,len(input_data),2):
        x = int(input_data[i])
        y = int(input_data[i+1])
        List.append(x)
        ans = divisors[x]
        cout = len(List)
        
        valid_count = 0
        for d in ans: 
            
            if last_seen[d] < cout - y:
                valid_count += 1
            
            last_seen[d] = cout 
            
        print(valid_count)

if __name__ == '__main__':
    solve()