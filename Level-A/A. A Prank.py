"""
Problem Name: A. A Prank
Platform: Codeforces
Approach: Greedy / Longest Consecutive Sequence
Time Complexity: O(N) where N is the number of elements.
Space Complexity: O(N) to store the padded array.

Description:
The problem asks for the maximum number of elements we can erase from a strictly 
increasing array such that the remaining elements can still uniquely identify the erased ones.
This is only possible if the erased elements form a consecutive sequence (difference of 1).
We can erase elements as long as we keep the boundaries (first and last elements of the sequence).
"""

def solve():
    # Read the number of elements
    n = int(input())
    
    # Read the array and pad it with 0 at the beginning and 1001 at the end.
    # This acts as boundaries since the problem states elements are in the range [1, 1000].
    # It helps in avoiding complex edge-case handling for the first and last elements.
    a = [0] + list(map(int, input().split())) + [1001]
    
    max_erased = 0       # Stores the maximum number of erasable elements found so far
    current_length = 1   # Tracks the length of the current consecutive sequence
    
    # Iterate through the array starting from the second element
    for i in range(1, len(a)):
        # Check if the current element and the previous one are consecutive
        if a[i] - a[i-1] == 1:
            current_length += 1
        else:
            # The consecutive sequence has broken.
            # If a sequence has length L, we can erase at most (L - 2) elements 
            # (keeping the start and end of the sequence for restoration).
            max_erased = max(max_erased, max(0, current_length - 2))
            
            # Reset the length counter for the new sequence
            current_length = 1
            
    # Final check in case the array ends while still inside a consecutive sequence
    max_erased = max(max_erased, max(0, current_length - 2))
    
    # Print the final answer
    print(max_erased)

if __name__ == "__main__":
    solve()