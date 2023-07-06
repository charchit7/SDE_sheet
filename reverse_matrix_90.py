matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)
# first step is to transpose the matrix
for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
print(matrix)

# second step is to reverse the matrix
for i in range(len(matrix)):
    matrix[i].reverse()
print(matrix)


    