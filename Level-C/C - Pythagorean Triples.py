
def solve():
    n = int(input())
    
    if n <= 2:
        print(-1)
    elif n % 2 != 0:
        m = (n**2 - 1) // 2
        k = (n**2 + 1) // 2
        print(f"{m} {k}")
    else:
        m = (n**2) // 4 - 1
        k = (n**2) // 4 + 1
        print(f"{m} {k}")
 
if __name__ == "__main__":
    solve()