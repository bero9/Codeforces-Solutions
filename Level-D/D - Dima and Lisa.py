import sys
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    if is_prime(n):
        print(1)
        print(n)
        return
    elif is_prime(n-2):
        print(2)
        print(f"{n-2} {2}")
        return
    else:
        for i in range(3,n):
            if is_prime(i) and is_prime(n-3-i):
                print(3)
                print(f"{3} {i} {n-3-i}")
                return






    


if __name__ == '__main__':
    solve()