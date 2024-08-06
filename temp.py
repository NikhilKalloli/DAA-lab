def schedule(intervals):

    n = len(intervals)
    intervals.sort(key=lambda x : x[1])
    dp = [0]*n

    dp[0] = intervals[0][2]
    
    for i in range(1, n):
        value_include = intervals[i][2]
        j = helper(intervals, i)

        if j!=-1:
            value_include+= dp[j]

        value_exclude = dp[i-1]

        dp[i] = max(value_exclude, value_include)
    return dp[n-1]


def helper(intervals, current):
    for j in range(current-1, -1,-1):
        if intervals[j][1] <= intervals[current][0]:
            return j
    return -1
    


n = int(input("Number of intervals: "))
intervals = []

for i in range(n):
    interval = map(int, input("Enter (start, end , value): ").split())
    intervals.append([interval])

print(schedule(intervals))