# Read the total length of the initial string
n = int(input())
# Read the string consisting of decimal digits
s = input()

# Calculate the total number of characters that will be erased during the game
num = n - 11

# Count the occurrences of '8' in the critical range (the first n - 10 characters)
# s[:num+1] slices the string up to index n - 10, which determines the first digit's fate
count = s[:num+1].count('8')

# Game theory winning condition for Vasya:
# (num // 2) represents Petya's total moves to eliminate '8's.
# If Petya's moves plus the available '8's exceed the total erased count,
# Vasya safely secures at least one '8' at the beginning of the final string.
if (num // 2) + count > num:
    print("YES")
else:
    print("NO")