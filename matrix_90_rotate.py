N=4
def matrix_90_rotate(matrix):
    for x in range(0,int(N/2)):
        for y in range(x,N-x-1):
            temp=matrix[x][y]
            matrix[x][y]=matrix[y][N-x-1]
            matrix[y][N-x-1]=matrix[N-x-1][N-y-1]
            matrix[N-x-1][N-y-1]=matrix[N-y-1][x]
            matrix[N-y-1][x]=temp
def display_matrix(matrix):
    for i in range(0,N):
        for j in range(0,N):
            print(matrix[i][j],end=' ')
        print('')
matrix=[[] for i in range(N)]
for i in range(N):
    matrix[i]=[int(j) for j in input().split()]
matrix_90_rotate(matrix)
display_matrix(matrix)
