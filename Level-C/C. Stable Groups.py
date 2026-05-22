"""
Approach: Greedy Algorithm & Sorting
Time Complexity: O(N log N)
Space Complexity: O(N)

Description:
The array is sorted to find the natural gaps between adjacent elements.
Gaps that are larger than 'X' require inserting additional elements.
By sorting the required insertions for each gap, we greedily fill the 
smallest gaps first using our budget 'K', minimizing the total number of connected components.
"""

import sys

def solve():
    # Fast I/O: Read all contents from standard input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    x = int(input_data[2])
    
    # Read the array and sort it to process adjacent elements
    a = [int(y) for y in input_data[3:]]
    a.sort()
    
    gaps = []
    
    # Calculate how many elements need to be inserted for gaps strictly greater than X
    for i in range(n - 1):
        diff = a[i+1] - a[i]
        if diff > x:
            # (diff - 1) // x is the integer math equivalent of ceil(diff / x) - 1.
            # This avoids floating-point precision issues with very large integers.
            gaps.append((diff - 1) // x)
            
    # If there are no gaps larger than X, the entire array forms 1 component
    if not gaps:
        sys.stdout.write("1\n")
        return
        
    # Sort gaps to greedily bridge the smallest gaps first (cost efficiency)
    gaps.sort()
    
    # Initial number of components is (number of gaps + 1)
    ans = len(gaps) + 1 
    
    for cost in gaps:
        if cost <= k:
            k -= cost      # Pay the cost to bridge the gap
            ans -= 1       # Bridging a gap reduces total components by 1
        else:
            # Optimization: Gaps are sorted, so if we can't afford this one, 
            # we definitely cannot afford the larger ones that follow.
            break
            
    # Print the final minimum number of components
    sys.stdout.write(str(ans) + '\n')

if __name__ == '__main__':
    solve()