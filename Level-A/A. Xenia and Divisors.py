
"""
Problem: Greedy Grouping of Three (1, 2, 3, 4, 6)
Approach: Frequency Counting / Greedy
Time Complexity: O(N) where N is the number of elements.
Space Complexity: O(1) since we only store counts for a fixed set of numbers (1 to 7).

Description:
The algorithm counts the occurrences of each number.
It immediately rejects the input if numbers 5 or 7 are present.
Then, it greedily checks if the numbers can form the only valid 
groups: (1, 2, 4), (1, 2, 6), and (1, 3, 6).
"""

def solve():
    # Read the number of elements
    n = int(input())
    
    # Read the array of integers
    nums = list(map(int, input().split()))
    
    # Frequency array to count occurrences of each number from 1 to 7
    counts = {i: 0 for i in range(1, 8)}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            print("-1")
            return

    # 1. Integers 5 and 7 are bad
    if counts[5] > 0 or counts[7] > 0:
        print("-1")
        return
        
    # 2. Every valid group has exactly one '1'
    # So the count of '1's must be exactly n // 3
    if counts[1] != n // 3:
        print("-1")
        return
        
    # 3. Calculate exactly how many of each group we can/must form
    # Group (1, 2, 4) is dictated entirely by the number of 4s
    count_124 = counts[4]
    
    # Group (1, 3, 6) is dictated entirely by the number of 3s
    count_136 = counts[3]
    
    # Group (1, 2, 6) takes the remaining 2s (after forming 1, 2, 4)
    count_126 = counts[2] - count_124
    
    # 4. Validation checks to ensure no numbers are left unused
    # If we needed more 4s than we had 2s, count_126 would be negative
    if count_126 < 0:
        print("-1")
        return
        
    # The number of 6s must exactly match the groups that require a 6
    if counts[6] != count_126 + count_136:
        print("-1")
        return
        
    # 5. If all checks pass, print the found groups greedily
    for _ in range(count_124):
        print("1 2 4")
    for _ in range(count_126):
        print("1 2 6")
    for _ in range(count_136):
        print("1 3 6")

if __name__ == "__main__":
    solve()