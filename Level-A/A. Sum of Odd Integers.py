import sys

def solve():
    """
    Solves the 'Sum of Odd Integers' problem.
    Uses parity checks and arithmetic progression to validate if 'n' 
    can be formed by the sum of 'k' distinct odd integers.
    """
    # Fast I/O: Read all inputs from standard input at once to avoid TLE
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # Loop through the input data, reading pairs of (n, k)
    # Starting from index 1 to skip the number of test cases (t)
    for i in range(1, len(input_data), 2):
        n = int(input_data[i])
        k = int(input_data[i+1]) 
        
        # Condition 1 (Parity Match): 
        # If 'n' is odd and 'k' is even, OR 'n' is even and 'k' is odd, it's impossible.
        # The sum of 'k' odd numbers must share the same parity as 'k'.
        if (n%2 == 1 and k%2 == 0) or (n%2 == 0 and k%2 == 1):
            sys.stdout.write("NO\n")
            continue
            
        # Condition 2 (Minimum Required Sum):
        # Calculate the sum of the first 'k' distinct odd numbers 
        # using the arithmetic sequence sum formula.
        ans = (k * (1 + (k * 2 - 1))) // 2
        
        # If the minimum possible sum of 'k' distinct odd numbers is strictly greater than 'n', 
        # it is impossible to form 'n'. Otherwise, it is possible.
        if ans > n:
            sys.stdout.write("NO\n")
        else:
            sys.stdout.write("YES\n")

if __name__ == '__main__':
    solve()