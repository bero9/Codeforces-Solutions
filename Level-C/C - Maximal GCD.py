
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
        
    n = int(input_data[0])
    k = int(input_data[1])
    S =( k*(k+1))/2
    if S > n :
        print(-1)
        return
    Fac = get_divisors(n)
    #print(Fac)
    global g
    for i in Fac:
        if n//i >=S:
            g = i
        else:
            break
    List = [i*g for i in range(1,k)]
    List.append(n-sum(List))
    print(*List)


    
    

if __name__ == '__main__':
    solve()