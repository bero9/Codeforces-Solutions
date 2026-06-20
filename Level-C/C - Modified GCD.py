import sys
import math
# MAX_VAL = 600851475143

# divisors = [[] for _ in range(MAX_VAL + 1)]

# def precompute_divisors():
#     for i in range(1, MAX_VAL + 1):
#         for j in range(i, MAX_VAL + 1, i):
#             divisors[j].append(i)
# precompute_divisors()
#///////////////////////////////////////////////////////////
# # O(log(min(a, b))).
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#///////////////////////////////////////////////////////////////////
# def sieve(n):
#     prime = [True] * (n + 1)
#     p = 2
#     while p * p <= n:
#         if prime[p]:
#             for i in range(p * p, n + 1, p):
#                 prime[i] = False
#         p += 1
#     res = []
#     for p in range(2, n + 1):
#         if prime[p]:
#             res.append(p)
    
#     return res
#///////////////////////////////////////////////////////////////////

# import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i*i != n:
                divisors.append(n // i)
    return divisors
#///////////////////////////////////////////////////////////////////
def custom_euclidean_gcd(a, b):
   
    while b != 0:
        # a تأخذ قيمة b
        # b تأخذ قيمة باقي قسمة a على b
        a, b = b, a % b
    return a

# import math

# import math

# def prime_factorization(n: int) -> list[int]:
#     factors = []
    
#     # 1. استخراج جميع العوامل الزوجية
#     while n % 2 == 0:
#         factors.append(2)
#         n //= 2
        
#     # 2. نختبر الأرقام الفردية فقط
#     # لا نستخدم for loop بسيطة مع isqrt هنا لأن n تتغير قيمتها وتصغر
#     i = 3
#     while i * i <= n:
#         while n % i == 0:
#             factors.append(i)
#             n //= i
#         i += 2
        
#     # 3. ما تبقى هو عدد أولي
#     if n > 2:
#         factors.append(n)
        
#     return factors
#///////////////////////////////////////////////////////////////////

# #أنها عدد الأعداد الصحيحة الموجبة الأقل من أو تساوي  
# # n     
# # n والتي تكون أولية بالنسبة لـ 
# # (أي أن القاسم المشترك الأكبر بينها وبين  العدد يساوي الواحد).
# def get_phi(n):
#     """
#     Calculates Euler's totient function phi(n).
#     Complexity: O(sqrt(n))
#     """
#     result = n
#     i = 2
#     # Check for prime factors up to sqrt(n)
#     while i * i <= n:
#         if n % i == 0:
#             # If i is a prime factor, apply the formula: result = result * (1 - 1/i)
#             # This is equivalent to: result = result - result // i
#             while n % i == 0:
#                 n //= i
#             result -= result // i
#         i += 1
    
#     # If n > 1, then the remaining n is a prime factor
#     if n > 1:
#         result -= result // n
        
#     return result
#///////////////////////////////////////////////////////////////////
# sorted_arr = sorted(enumerate(a), key=lambda x: x[1],reverse=True)

import sys
import math


import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    a  = int(input_data[0])
    b = int(input_data[1])
    n = int(input_data[2])
    idx =3
    ans =custom_euclidean_gcd(a,b)
    List = get_divisors(ans)
    
    for i in range(n):
        Low = int(input_data[idx])
        high = int(input_data[idx+1])
        idx +=2
        k = False
        
        
        if high in List:
            print(high)
            continue
        List.append(Low)
        List.append(high)
        List = sorted(List)
        index_Low = List.index(Low)
        index_high = List.index(high)
        #print(List)
        if index_high - index_Low <=1:
            print(-1)
        else:
            print(List[index_high-1])
        List.pop(index_high)
        List.pop(index_Low)
       # print(List)

        
        
        
        #print(List)
        
            
            
        




        

    
    

if __name__ == '__main__':
    solve()