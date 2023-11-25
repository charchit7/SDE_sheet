# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # check1, not optimal 
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             print(nums[i] + nums[j])
        #             return [i,j]

        # check2, hashmap, optimal
        
        hashmap = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], idx]
            else:
                hashmap[val] = idx