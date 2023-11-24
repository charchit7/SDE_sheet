class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # take 1 sorting, O(nlogn)
        sorted_arr = sorted(nums)
        for i in range(1,len(sorted_arr)):
            if sorted_arr[i-1] == sorted_arr[i]:
                return True
        return False

        # take 2, hashset, optimal O(n)
        hashset = set()
        for val in nums:
            if val in hashset:
                return True
            hashset.add(val)
        
        return False