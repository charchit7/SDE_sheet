# https://leetcode.com/problems/merge-sorted-array/description/


nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6]
n = 3

# pythonic way
# nums1[:m] = nums1[:m]
# nums1[m:] = nums2[:n]
# nums1.sort()
# 
# print(nums1)

# brute force way!
# declare the pointers
left = 0
right = 0

# declare the array where we will store the answer
ans_arr = []
while left < m and right < n:
    if nums1[left] <= nums2[right]:
        ans_arr.append(nums1[left])
        left +=1
    else:
        ans_arr.append(nums2[right])
        right+=1

while left < m:
    ans_arr.append(nums1[left])
    left +=1

while right < n:
    ans_arr.append(nums2[right])
    right +=1


for i in range(n+m):
    nums1[i] = ans_arr[i]


# gap method 

def swap_function(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]
import math

def merge(arr1, arr2, n,m):
    fulllen = m+n

    gap = math.ceil(len//2)

    # logic
    while gap > 0:
        left = 0
        right = left + gap

        while right < fulllen:
            if left < n and right >=n:
                swap_function(arr1, arr2, left, right-n)
            elif left >=n:
                swap_function(arr1, arr2, left-n, right-n)
            else:
                swap_function(arr1, arr2, left, right)
            left +=1
            right +=1

        if gap == 1:
            break

        gap = math.ceil(gap//2)
        
