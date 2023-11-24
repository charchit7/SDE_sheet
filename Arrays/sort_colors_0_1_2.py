# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         count_zeros = 0
#         count_ones = 0
#         count_twos = 0

#         for val in nums:
#             if val == 0:
#                 count_zeros +=1
#             elif val == 1:
#                 count_ones +=1
#             else:
#                 count_twos +=1

#         print(count_zeros, count_ones, count_twos)
#         for i in range(count_zeros):
#             nums[i] = 0
        
#         for j in range(count_zeros, count_zeros+count_ones):
#             nums[j] = 1

#         for k in range(count_zeros+count_ones, len(nums)):
#             nums[k] = 2
        

# optimal solution (DNF algorithm)

nums = [2,0,2,1,1,0]

# we use three pointers 
low = 0
mid = 0
high = len(nums)-1

while(mid<=high):

    if nums[mid] == 0:
        nums[mid], nums[low] = nums[low], nums[mid]
        mid +=1 
        low +=1

    elif nums[mid] == 1:
        mid +=1

    elif nums[mid] == 2:
        nums[high], nums[mid] = nums[mid], nums[high]
        high -=1

    
print(nums)