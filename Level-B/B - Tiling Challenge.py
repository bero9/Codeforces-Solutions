"""
Problem: Tiling Challenge (Codeforces)
Approach: Greedy Algorithm
Time Complexity: O(N^2) where N is the size of the board.
Space Complexity: O(N^2) to store the grid.

Description:
The algorithm scans the grid from top to bottom, left to right. 
Whenever it encounters an empty cell ('.'), it MUST be the top vertex 
of the cross-shaped piece. The algorithm then checks if the rest of 
the cross can fit within the boundaries and if those cells are also empty. 
If successful, it marks them as occupied ('#'). If not, it's impossible 
to tile the board.
"""

def solve():
    # Read the size of the board
    n = int(input())
    
    # Read the grid as a 2D list of characters to allow modifications
    matrix = [list(input().strip()) for _ in range(n)]
    
    # Iterate through every cell in the grid
    for i in range(n):
        for j in range(n):
            # If we find an empty cell, it must act as the top of a cross piece
            if matrix[i][j] == '.':
                
                # 1. Check boundary conditions for the cross piece:
                #    - i+2 < n: Bottom of the cross stays within the board
                #    - j+1 < n: Right of the cross stays within the board
                #    - j-1 >= 0: Left of the cross stays within the board 
                #      (Crucial in Python to avoid negative indexing bugs)
                if i+2 < n and j+1 < n and j-1 >= 0:
                    
                    # 2. Check if the required adjacent cells are also empty
                    if (matrix[i+1][j] == '.' and     # Center
                        matrix[i+2][j] == '.' and     # Bottom
                        matrix[i+1][j-1] == '.' and   # Left
                        matrix[i+1][j+1] == '.'):     # Right
                        
                        # 3. Place the cross by marking all 5 cells as occupied
                        matrix[i][j] = '#'
                        matrix[i+1][j] = '#'
                        matrix[i+2][j] = '#'
                        matrix[i+1][j-1] = '#'
                        matrix[i+1][j+1] = '#'
                    else:
                        # Found an empty cell, but adjacent cells are blocked
                        print("NO")
                        return # Exit the function immediately
                else:
                    # Found an empty cell, but placing a cross goes out of bounds
                    print("NO")
                    return # Exit the function immediately
                    
    # If the loop finishes without returning, all empty cells were successfully tiled
    print("YES")

# Standard boilerplate to call the main function
if __name__ == "__main__":
    solve()