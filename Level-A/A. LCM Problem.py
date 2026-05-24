"""
Problem Name: A. LCM Problem
Platform: Codeforces
Approach: Math / Number Theory
Time Complexity: O(1) per testcase
Space Complexity: O(T) for input/output buffering

Description:
To find two numbers (x, y) such that l <= x < y <= r and LCM(x, y) <= r,
we can simply pick x = l and y = 2*l. The LCM of (l, 2l) is exactly 2l.
If 2l <= r, this pair is our guaranteed valid answer.
If 2l > r, then no such pair can possibly exist within the range.
"""

import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    idx = 1
    
    out = []
    
    for _ in range(t):
        l = int(input_data[idx])
        r = int(input_data[idx+1])
        idx += 2
        
        # Core Logic: Single mathematical condition
        if 2 * l <= r:
            out.append(f"{l} {2 * l}")
        else:
            out.append("-1 -1")
            
    # Print all answers at once
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()