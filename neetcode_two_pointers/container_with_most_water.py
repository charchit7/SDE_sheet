# https://leetcode.com/problems/container-with-most-water/

nums = [1,8,6,2,5,4,8,3,7]


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # res = 0

        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):

        #         area = (j-i) * min(height[i], height[j])
        #         res = max(area, res)
            
        # return res

        i, j = 0, len(height) -1

        water = 0
        while i < j:
            area = (j-i) * min(height[i], height[j])
            water = max(area, water)

            if height[i] < height[j]:
                i +=1
            else:
                j -=1
        
        return water