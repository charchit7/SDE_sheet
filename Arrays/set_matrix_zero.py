# brute force method 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        r = len(matrix)
        c = len(matrix[0])
        print(r, c)

        # mark row and col function
        def markRow(idx):
            for i in range(c):
                if matrix[idx][i] != 0:
                    matrix[idx][i] = float('inf')
        
        def markCol(idx):
            for j in range(r):
                if matrix[j][idx] !=0:
                    matrix[j][idx] = float('inf')


        for i in range(r):
            for j in range(c):
                # print(matrix[r][c])
                if matrix[i][j] == 0:
                    # mark the points
                    # let's mark the points as -1 because putting zeros will lead you to get 
                    # change the later 0's
                    markRow(i)
                    markCol(j)
        # now just traverse the array and mark all the -1 to zeros
        # print(matrix)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] =0

        # return matrix

# better method
# in better method best way is to create an array which keeps track of the 0's present in the array
# in this way we reduce the time complextity from O(n^3) to O(n^2) but introducing the 
# space complexity to O(n^2)

rows_array = [0]*r
columns_array = [0]*c

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 0:
            rows_array[i] = 1
            columns_array[j] = 1

for i in range(r):
    for j in range(c):
        if rows_array[i] or columns_array[j]:
            matrix[i][j] = 0       

# optimal method
# in this method we try to create the array in array itself. So, that we can reduce the memory space.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        col0 = 1
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                   matrix[i][0] = 0            
                   if j != 0:
                       matrix[0][j] = 0
                   else:
                       col0 = 0

        # Set rows and columns to zero based on marked values
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
            
        if matrix[0][0] == 0:
            for j in range(c):
                matrix[0][j] = 0
            
        if col0 == 0:
            for i in range(r):
                matrix[i][0] = 0
