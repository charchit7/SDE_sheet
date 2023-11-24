# pascal traingle 
# https://leetcode.com/problems/pascals-triangle/

# Prob 1 : 
# where user gives you row and columns and asks for what element is present there.

def pascal_val(row_n, col_n):

    # base case when the the n = 1
    res = 1
    
    # we do this for general methodology for finding such cases
    row_n = row_n -1
    col_n = col_n -1

    # generally the problem breaks down to using nCr formula which we can reduce to small form as well to
    # reduce the complexity of the number.
    # time completxity : O(r) 
    # space complexiy : O(1)

    for i in range(col_n):
        # these two condition is breakdown of the nCr formula to small cases.
        res = res * (row_n-i)
        res = res / (i + 1)

    return res


# if __name__ ==  "__main__":
#     # for i in range(6):
#     print(pascal_val(3, 2))


# next problem is to print the rows values given the data, for example given in the problem
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1

# if you want to interviewer asks you to print the last row, that will be, 1 5 10 10 5 1.

# this code gives you both the variant the second one and the final pascal traingle generate one!
class Solution:

    def generate_pascal_rows(self, row):

        ans = 1
        res_arr = [1]

        for col in range(1,row):

            ans = ans * (row-col)
            ans = ans / col
            res_arr.append(int(ans))
        
        return res_arr

    def generate(self, numRows: int) -> List[List[int]]:
        res_arr = []
        for i in range(1, numRows+1):
            res_arr.append(self.generate_pascal_rows(i))
        
        return res_arr