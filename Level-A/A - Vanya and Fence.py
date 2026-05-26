"""
Problem Name: A. Vanya and Fence
Platform: Codeforces
Language: Python 3
Description: Calculate the minimum width of the road required for friends to walk 
             unnoticed by the guard. A person takes a width of 1 if their height is 
             less than or equal to the fence height, and a width of 2 (bends down) 
             if they are taller than the fence.
"""

# Read all inputs at once from standard input for efficiency
# N: number of friends
# h: height of the fence
# *a: unpacks the remaining inputs into a list representing the friends' heights
N, h, *a = map(int, open(0).read().split())

# Initially assume everyone takes up a width of at least 1
# So, we start the total width (ans) with the total number of friends
ans = N

# Iterate through each friend's height in the list
for i in a:
    # If the friend is taller than the fence, they have to bend down.
    # This adds 1 more to the width they occupy (making their total width 2 instead of 1).
    if i > h:
        ans += 1 

# Print the minimum possible valid width of the road
print(ans)