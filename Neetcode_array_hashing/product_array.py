#  https://leetcode.com/problems/product-of-array-except-self/description/
# uses the concept of prefix and postfix

nums = [1,2,3,4]

result = [1] * len(nums)

# prefix
for i in range(1,len(nums)):
    result[i] = result[i-1] * nums[i-1]

# postfix 
postfix = 1
for i in range(len(nums) -1, -1, -1):
    result[i] = result[i] * postfix
    postfix = postfix * nums[i]

print(result)