# https://leetcode.com/problems/3sum/description/


# optimal solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize the list to store the triplets
        answer = []
        
        # Sort the input array to simplify the process of finding triplets
        nums.sort()

        # Iterate through the array
        for i in range(len(nums)):

            # Remove duplicate values
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize two pointers, one starting from the next element after i, and the other from the end of the array
            j = i + 1
            k = len(nums) - 1

            # Use two pointers to find triplets
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                # If the sum is less than 0, move the left pointer to the right
                if total_sum < 0:
                    j += 1

                # If the sum is greater than 0, move the right pointer to the left
                elif total_sum > 0:
                    k -= 1

                # If the sum is 0, add the triplet to the answer list
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    answer.append(temp)

                    # Move pointers and skip duplicates
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            
        # Return the final list of unique triplets
        return answer

r'''
The function threeSum uses two pointers to find unique triplets in the sorted array that sum to zero.

The outer loop iterates through each element in the array.

Duplicate values are skipped to avoid duplicate triplets.

Two pointers (j and k) are initialized to find the other two elements in the triplet.

The inner while loop uses the two pointers to search for triplets and skip duplicates.

If a triplet is found, it is added to the answer list.

The function returns the list of unique triplets.



'''
