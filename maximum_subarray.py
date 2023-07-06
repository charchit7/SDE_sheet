# kadane's algorithm

nums = [-2,1,-3,4,-1,2,1,-5,4]

len_arr = len(nums)

max_res = -float('inf')
for i in range(len_arr):
    sub_arr = []
    for j in range(i,len_arr):
        sub_arr.append(nums[j])
        total = 0
        for k in range(i,j):
            total += nums[k]
        max_res = max(total, max_res)

# print(max_res)


# above method is brute force method
# TC : O(N^3)

# we can improve the above algorithm by just removing the third loop because we already have 
# the results stored before

for i in range(len_arr):
    for j in range(i, len_arr):
        summ = 0
        for k in range(i, j+1):
            summ += nums[k]

        maxi = max(max_res, summ)

# print(maxi)
# TC: N(N^2)

# now we go to optimal approach
# Using Kadane's Algorithm
 
maximum = -float('inf')
final_sum = 0

for i in range(len_arr):
    final_sum = final_sum + nums[i]

    if final_sum > maximum:
        maximum = final_sum 

    # two condition : first is if the sum is < 0, we drop everything and start again,
    # this will help in two cases, 1st : Keep track of the starting point 
    # second : this will help in summation

    if final_sum < 0:
        final_sum = 0
    
# print(maximum)


# one follow up question can be, can you print the subarray which holds the best sum?
# if you notice the sum is getting 0 if it's a begineeing in a way, right.
# so that is your start. and end will also be that where the sum is starting again.

maximum = -float('inf')
final_sum = 0

# to track the subarray
start = -1
end = -1

for i in range(len_arr):
    
    if final_sum ==0:
        start = i

    final_sum = final_sum + nums[i]

    if final_sum > maximum:
        maximum = final_sum
        start = start 
        end = i # why putting here, because the end will stop at the max sum, right? this keeps track of the subarray
    
    if final_sum < 0:
        final_sum = 0

print(nums[start:end+1])