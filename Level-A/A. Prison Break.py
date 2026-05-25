import sys

def solve():
    """
    Solves the problem using fast I/O and direct mathematical calculation.
    """
    # Fast I/O: Reading all input at once into a list of strings
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # Read the number of test cases
    t = int(input_data[0])
    idx = 1
    
    # Process each test case
    for _ in range(t):
        # Read n, m (dimensions of matrix) and r, c (position of secret tunnel)
        n = int(input_data[idx])
        idx += 1
        m = int(input_data[idx])
        idx += 1
        r = int(input_data[idx])
        idx += 1
        c = int(input_data[idx])
        idx += 1
        
        # Calculate Manhattan distance from (r, c) to all four corners of the grid
        
        # Distance to Top-Left corner (1, 1)
        left_u = (abs(r-1) + abs(c-1))
        
        # Distance to Bottom-Left corner (1, m)
        left_d = abs(r-1) + abs(c-m)
        
        # Distance to Top-Right corner (n, 1)
        right_u = abs(r-n) + abs(c-1)
        
        # Distance to Bottom-Right corner (n, m)
        right_d = abs(r-n) + abs(c-m)
        
        # The minimum seconds needed is the distance from (r, c) to the farthest prisoner.
        # Farthest prisoner must be located at one of the four corners.
        # Calculate the maximum distance of all calculated corner distances.
        ans = max((left_d,left_u,right_d,right_u))
        
        # Fast output: writing the answer with a newline
        sys.stdout.write(f"{ans}\n")

if __name__ == '__main__':
    solve()