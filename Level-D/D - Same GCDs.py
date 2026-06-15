import sys
import math
# MAX_VAL = 10000000000
 
# divisors = [[] for _ in range(MAX_VAL + 1)]
 
# def precompute_divisors():
#     for i in range(1, MAX_VAL + 1):
#         for j in range(i, MAX_VAL + 1, i):
#             divisors[j].append(i)
 
# precompute_divisors()
# O(log(min(a, b))).
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
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
import math
 
def get_divisors(n):
    divisors = []
    # حلقة حتى الجذر التربيعي للعدد
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # إضافة القاسم المقابل إذا لم يكن متطابقاً
            if i*i != n:
                divisors.append(n // i)
    return sorted(divisors)
 
# مثال: قواسم الرقم 36
# النتيجة: [1, 2, 3, 4, 6, 9, 12, 18, 36]
def get_phi(n):
    """
    Calculates Euler's totient function phi(n).
    Complexity: O(sqrt(n))
    """
    result = n
    i = 2
    # Check for prime factors up to sqrt(n)
    while i * i <= n:
        if n % i == 0:
            # If i is a prime factor, apply the formula: result = result * (1 - 1/i)
            # This is equivalent to: result = result - result // i
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    
    # If n > 1, then the remaining n is a prime factor
    if n > 1:
        result -= result // n
        
    return result
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    
    for i in range(1, len(input_data), 2):
        a , m = int(input_data[i]),int(input_data[i+1])
        
        g = math.gcd(a, m)
    
        m_prime = m // g
    
        print(get_phi(m_prime))
        
 
        
        
 
    
    
 
if __name__ == '__main__':
    solve()