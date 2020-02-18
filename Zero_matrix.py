def setZeroes(matrix):
    points = [[i,j] for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 0]
    for i, a in enumerate(points):
        for k in range(len(matrix[0])):
            matrix[a[0]][k] = 0
        for k in range(len(matrix)): 
            matrix[k][a[1]] = 0
def display_matrix(matrix):
    for x in range(0,i):
        for y in range(0,j):
            print(matrix[x][y],end=' ')
        print('')
i=int(input())
j=int(input())
matrix=[[] for k in range(0,j)]
for k in range(j):
    matrix[k]=[int(m) for m in input().split()]
setZeroes(matrix)
display_matrix(matrix)