# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        number_of_times_appear = {}
        bucket_arr = [[] for i in range(len(nums)+1)]
        print(bucket_arr)

        for val in nums:
            number_of_times_appear[val] = 1+ number_of_times_appear.get(val, 0)

        for key, val in number_of_times_appear.items():
            bucket_arr[val].append(key)


        res = []
        for i in range(len(bucket_arr)-1,0,-1):
            for val in bucket_arr[i]:
                res.append(val)
                if len(res) == k:
                    return res