# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums.sort()  # O(nlogn) time complexity
        
        current_streak = 1
        max_streak = 1
        
        for i in range(1, len(nums)):
            # to check distinct elements
            if nums[i] != nums[i - 1]:
                # to check for consecutive approach
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    max_streak = max(max_streak, current_streak)
                    current_streak = 1

        return max(max_streak, current_streak)

# optimal method 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) ==1:
            return 1

        sett = set(nums)
        longest = 0

        for val in nums:
            if (val -1) not in sett:
                length = 1
                while (val+length) in sett:
                    length+=1
                    longest = max(longest, length)
        
        return longest

