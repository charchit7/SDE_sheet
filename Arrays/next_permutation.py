# from itertools import permutations
# arr = [1,2,3]
# print(list(permutations(arr)))

# you can tell about the interviewer about the itertool library 
# it's complexity is also O(N)

# brute force method 
## generate all the permutations 
## select the permutations which is bigger than the previous one.
## TC : O(N!) * O(N)


# better way
arr = [1,2,3]

#first task is to find the break point 
idx = -1 
for i in range(len(arr)-2,-1,-1):
    if arr[i] < arr[i+1]:
        idx = i
        break

# one case where the array has no breakpoint so we just return that array in reverse!
# think why!!!
if idx == -1:
    sorted(arr)

# second task is to find the first element which is greater than the break point
for i in range(len(arr)-1,idx+1,-1):
    if arr[i] > arr[idx]:
        # print(arr[i])
        arr[i], arr[idx] = arr[idx], arr[i]
        break

# third thing is to sort the array just after the break point
arr[idx+1:] = sorted(arr[idx+1:])
print(arr)

