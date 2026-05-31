import sys

def count_zeroes(n):
    # Initialize the count of zeroes
    zeroes = 0
    
    # Keep dividing by 5 and adding the quotient to count all factors of 5
    while n >= 5:
        n //= 5
        zeroes += n
    return zeroes

def solve():
    # Fast I/O: read all inputs at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # m is the target number of zeroes we want
    m = int(input_data[0])
    
    # Mathematical shortcut: the answer is always very close to 4 * m
    start_n = 4 * m
    
    # Trailing zeroes only increase at multiples of 5, so we move to the nearest multiple of 5
    while start_n % 5 != 0:
        start_n += 1
        
    # We only need to check a few multiples of 5 (step = 5)
    # Checking up to start_n + 45 is mathematically enough to find the answer
    for n in range(start_n, start_n + 45, 5):
        # Calculate how many zeroes this 'n' produces
        zeros = count_zeroes(n)
        
        # If we hit the exact target 'm'
        if zeros == m:
            print(5) # There are always 5 numbers sharing the same zeroes count
            # Generate and print the 5 consecutive numbers (n, n+1, n+2, n+3, n+4)
            ans_n = [n + i for i in range(5)]
            print(*ans_n)
            return
            
        # If zeroes exceed 'm', it means 'm' is a skipped value (impossible to achieve)
        elif zeros > m:
            break
            
    # If the loop finishes or breaks without finding 'm', print 0
    print(0)

if __name__ == '__main__':
    solve()