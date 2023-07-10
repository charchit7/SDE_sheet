intervals = [[1,3],[2,6],[8,10],[2,4],[15,18]]

# brute force method

#sort the array first
intervals.sort()

# then merge the intervals by checking the next elements
ans = []
for i in range(len(intervals)):
    
    start, end = intervals[i][0], intervals[i][1]


    if ans and end <=ans[-1][1]:
        continue


    for j in range(i+1, len(intervals)):
        if intervals[j][0] <= end:
            end = max(end, intervals[j][1])
        else:
            break
    
    ans.append([start,end])

print(ans)

# optimal code 
# then merge the intervals by checking the next elements
ans = []
intervals.sort()
for i in range(len(intervals)):

    if ans and end <=ans[-1][1]:
        ans.append(ans[i])

    else:
        ans[-1][1] = max(ans[-1][1], intervals[i][1]) 
       