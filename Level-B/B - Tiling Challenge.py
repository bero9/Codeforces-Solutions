n = int(input())

matrix = [list(input().strip()) for _ in range(n)]
k = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '.':
            if i+1<n and j+1 <n and i+2 <n:
                if matrix[i+1][j] == '.' and matrix[i+2][j] == '.' and matrix[i+1][j-1] == '.' and matrix[i+1][j+1] == '.' :
                    matrix[i][j] = '#'
                    matrix[i+1][j] = '#'
                    matrix[i+2][j] = '#'
                    matrix[i+1][j-1] ='#'
                    matrix[i+1][j+1] = '#'
                else :
                    k =False
                    break
            else :
                k =False
                break
                
    if k == False:
        print("NO") 
        break      
else:
    print("YES")