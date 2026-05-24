"""
Problem Name: A. Nastya and Rice
Platform: Codeforces
Approach: Math / Interval Intersection
Time Complexity: O(1) per testcase, O(T) overall
Space Complexity: O(T) to store input and output arrays

Description:
To determine if the weights are consistent, we calculate the minimum and 
maximum possible weights of all 'n' grains combined. Then, we check if 
this weight interval intersects with the expected package weight interval.
"""

import sys

def solve():
    # Fast I/O: Read all inputs at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    idx = 1
    
    # Store results in a list to print them all at once (faster than multiple prints)
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])  
        a = int(input_data[idx+1])
        b = int(input_data[idx+2])
        c = int(input_data[idx+3])
        d = int(input_data[idx+4])
        
        # Calculate the actual possible range of 'n' grains
        left = (a - b) * n
        right = (a + b) * n
        
        # The expected range of the package
        final_left = c - d
        final_right = c + d
        
        idx += 5
        
        # Interval intersection logic:
        # Two intervals [L1, R1] and [L2, R2] intersect IF AND ONLY IF:
        # L1 <= R2 AND R1 >= L2
        if left <= final_right and right >= final_left:
            out.append("Yes")
        else:
            out.append("No")
            
    # Print all results separated by newlines
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()